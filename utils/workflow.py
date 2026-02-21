import joblib
from utils.rule_engine import rule_based_score
from utils.rule_engine import rule_based_score, detect_fraud_type

# Load trained model + vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def ml_probability(message):
    X = vectorizer.transform([message])
    prob = model.predict_proba(X)[0][1]  # Probability of class 1 (fraud)
    return prob * 100  # convert to percentage

def final_analysis(message):
    # Rule-based score
    rule_score, keywords = rule_based_score(message)

    # ML score
    ml_score = ml_probability(message)

    # Weighted final score
    final_score = (0.4 * rule_score) + (0.6 * ml_score)

    # Classification
    if final_score < 30:
        risk_level = "Low Risk"
    elif final_score < 70:
        risk_level = "Suspicious"
    else:
        risk_level = "High Risk Scam"

    # Explanation + Safety tips
    if risk_level == "High Risk Scam":
        explanation = (
            "This message shows strong indicators of fraud such as urgency, "
            "requests for sensitive information (OTP/bank details), or suspicious links."
        )
        tips = [
            "Do NOT click on any links",
            "Do NOT share OTP, passwords, or bank details",
            "Block and report the sender",
            "Contact official bank/support directly if unsure"
        ]

    elif risk_level == "Suspicious":
        explanation = (
            "This message contains some suspicious patterns. "
            "It may be a scam attempt. Verify authenticity before taking action."
        )
        tips = [
            "Verify sender identity from official sources",
            "Avoid clicking unknown links",
            "Do not share personal or banking details",
            "Check spelling/grammar and urgency cues"
        ]

    else:
        explanation = (
            "No strong fraud indicators detected. "
            "However, always stay cautious with unknown messages."
        )
        tips = [
            "Avoid sharing personal information",
            "Be cautious with unknown links",
            "Verify unexpected requests"
        ]
    
    fraud_type = detect_fraud_type(message)
    
    return {
    "rule_score": round(rule_score, 2),
    "ml_score": round(ml_score, 2),
    "final_score": round(final_score, 2),
    "risk_level": risk_level,
    "fraud_type": fraud_type,
    "keywords": keywords,
    "explanation": explanation,
    "tips": tips
}