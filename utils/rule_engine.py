import re

# Fraud keyword dictionary with weights
FRAUD_KEYWORDS = {
    "otp": 20,
    "verify": 15,
    "urgent": 15,
    "bank": 10,
    "account": 10,
    "suspend": 15,
    "click": 10,
    "link": 10,
    "prize": 20,
    "lottery": 20,
    "winner": 15,
    "kyc": 15,
    "update": 10,
    "password": 15,
    "call now": 15,
    "limited time": 15,
    "free": 10,
    "reward": 15
}

# Detect URLs
def contains_link(text):
    url_pattern = r"http[s]?://|www\."
    return bool(re.search(url_pattern, text.lower()))

# Main rule-based analysis
def rule_based_score(message):
    message_lower = message.lower()
    score = 0
    detected_keywords = []

    for word, weight in FRAUD_KEYWORDS.items():
        if word in message_lower:
            score += weight
            detected_keywords.append(word)

    # If link present → increase risk
    if contains_link(message):
        score += 25
        detected_keywords.append("suspicious_link")

    # Cap score at 100
    score = min(score, 100)

    return score, detected_keywords

def detect_fraud_type(message):
    msg = message.lower()

    if "otp" in msg or "verify" in msg:
        return "OTP Scam"

    if "bank" in msg or "account" in msg or "kyc" in msg:
        return "Banking Scam"

    if "lottery" in msg or "prize" in msg or "winner" in msg:
        return "Lottery/Reward Scam"

    if "link" in msg or "click" in msg:
        return "Phishing Link"

    if "call" in msg:
        return "Impersonation Scam"

    return "General Suspicious Message"