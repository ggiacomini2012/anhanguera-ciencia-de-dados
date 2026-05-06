import spacy
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load SpaCy model for Portuguese
# try:
#     nlp = spacy.load("pt_core_news_sm")
# except:
#     import subprocess
#     subprocess.run(["python", "-m", "spacy", "download", "pt_core_news_sm"])
#     nlp = spacy.load("pt_core_news_sm")

text = "A inteligência artificial está transformando rapidamente as nossas vidas diárias. Os computadores estão aprendendo a processar a linguagem natural de forma eficiente!"

print("--- TEXTO ORIGINAL ---")
print(text)
print("\n")

# Usaremos NLTK e um pouco de SpaCy. SpaCy é melhor para Lematização e POS Tagging em PT-BR.
import subprocess
try:
    nlp = spacy.load("pt_core_news_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "pt_core_news_sm"])
    nlp = spacy.load("pt_core_news_sm")

doc = nlp(text)

print("--- 1. SEGMENTAÇÃO (Sentenças e Palavras) ---")
print("Sentenças:")
for i, sent in enumerate(doc.sents):
    print(f"[{i+1}] {sent.text}")

print("\nPalavras (Tokens):")
tokens = [token.text for token in doc if not token.is_punct]
print(tokens)
print("\n")

print("--- 2. MARCAÇÃO MORFOSSINTÁTICA (POS Tagging) ---")
for token in doc:
    if not token.is_punct:
        print(f"{token.text:15} -> {token.pos_}")
print("\n")

print("--- 3. NORMATIZAÇÃO (Stopwords, Stemming e Lematização) ---")
stop_words = set(stopwords.words('portuguese'))
stemmer = SnowballStemmer('portuguese')

filtered_tokens = []
stemmed_tokens = []
lemmatized_tokens = []

for token in doc:
    if not token.is_punct and token.text.lower() not in stop_words:
        filtered_tokens.append(token.text)
        stemmed_tokens.append(stemmer.stem(token.text))
        lemmatized_tokens.append(token.lemma_)

print(f"Sem Stopwords : {filtered_tokens}")
print(f"Stemming      : {stemmed_tokens}")
print(f"Lematização   : {lemmatized_tokens}")

