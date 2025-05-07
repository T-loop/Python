import json
from collections import defaultdict
import math

# Laden der JSON-Datei mit Texten und Labels
with open("info.json", "r") as file:
    filetoload = json.load(file)

# Struktur: [{"text": "gut und schlecht", "label": "positiv"}, ...]

# Vorbereitung der Daten
informatikdic = {}
for entry in filetoload:
    text = entry["text"]
    label = entry["label"]
    informatikdic[text] = label

# Training
def train(data):
    word_counts = defaultdict(lambda: defaultdict(int))
    class_counts = defaultdict(int)
    total_words = defaultdict(int)
    vocabulary = set()

    for text, label in data.items():
        words = text.split()
        class_counts[label] += 1
        total_words[label] += len(words)

        for word in words:
            word_counts[label][word] += 1
            vocabulary.add(word)

    return word_counts, class_counts, total_words, vocabulary

# Vorhersagefunktion
def predict(text, word_counts, class_counts, total_words, vocabulary):
    words = text.split()
    total_docs = sum(class_counts.values())
    class_probs = {}

    for label in class_counts:
        # Prior: P(Klasse)
        log_prob = math.log(class_counts[label] / total_docs)

        for word in words:
            # Wahrscheinlichkeit mit Laplace Glättung
            word_freq = word_counts[label][word]
            word_prob = (word_freq + 1) / (total_words[label] + len(vocabulary))
            log_prob += math.log(word_prob)

        class_probs[label] = log_prob

    return max(class_probs, key=class_probs.get)

# Trainieren
word_counts, class_counts, total_words, vocabulary = train(informatikdic)

# Beispiel-Vorhersage
textbeingpredict = "ich bin glücklich und zufrieden"
result = predict(textbeingpredict, word_counts, class_counts, total_words, vocabulary)
print("Vorhersage:", result)
