# Week 2 – ML-Based Chatbot using TF-IDF + Logistic Regression
# Reuses preprocessing from Week 1
import sys
import os

# Add the project root so Python can find nlp_scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#  import Week 1 preprocessing function
from nlp_scripts.preprocess import preprocess_text
from nlp_scripts import preprocess


# ---  Helper to normalize text using Week 1 preprocessing ---
def normalize(text):
    processed = preprocess_text(text)
    # Use lemmas if available, otherwise tokens
    lemmas = processed.get("lemmas", processed.get("tokens", []))
    return " ".join([w.lower() for w in lemmas if isinstance(w, str)])


# --- Load training data (intents.json at project root) ---
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

patterns, tags = [], []

for intent in data["intents"]:
    for p in intent["patterns"]:
        patterns.append(normalize(p))
        tags.append(intent["tag"])


# --- Train TF-IDF + Logistic Regression model ---
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)
model = LogisticRegression(max_iter=200)
model.fit(X, tags)


# ---Function: generate chatbot response ---
def chatbot_response(user_input):
    X_test = vectorizer.transform([normalize(user_input)])
    predicted_tag = model.predict(X_test)[0]

    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])
    return "Sorry, I don't understand yet."


# --- Chat loop ---
if __name__== "__main__":
    print("Chatbot : Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.lower() in ("bye", "exit", "quit"):
            print("Chatbot : Goodbye!")
            break
        print("Chatbot :", chatbot_response(user))