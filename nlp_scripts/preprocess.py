import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Make sure NLTK looks here
nltk.data.path.append(r'C:\nltk_data')

# Download punkt if missing
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt', download_dir=r'C:\nltk_data')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stems = [stemmer.stem(w) for w in tokens]
    lemmas = [lemmatizer.lemmatize(w) for w in tokens]
    return {"tokens": tokens, "stems": stems, "lemmas": lemmas}

if __name__ == "__main__":
    sentence = "Hello! I am learning how to build a chatbot."
    result = preprocess_text(sentence)
    print("Tokens:", result["tokens"])
    print("Stems:", result["stems"])
    print("Lemmas:", result["lemmas"])