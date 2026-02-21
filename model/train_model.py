import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Small built-in dataset (so no download needed)
data = {
    "text": [
        "Congratulations you won a lottery claim now",
        "URGENT! Share your OTP immediately",
        "Your bank account suspended click link",
        "Win cash prize now click here",
        "Free entry in 2 lakh prize",
        "Meeting at 5 pm today",
        "Let's have lunch tomorrow",
        "Project submission deadline extended",
        "Call me when you reach home",
        "Your order has been shipped"
    ],
    "label": [
        1,1,1,1,1,   # fraud/spam
        0,0,0,0,0    # normal
    ]
}

df = pd.DataFrame(data)

# Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Model
model = LogisticRegression()
model.fit(X, df["label"])

# Save model + vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained and saved successfully")