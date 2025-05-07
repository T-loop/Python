from collections import defaultdict
import math

# Trainingsdaten
training_data = [
    ("gut gut toll", "positiv"),
    ("schlecht schlecht schlecht", "negativ"),
    ("gut schlecht schlecht", "negativ"),
    ("toll gut", "positiv"),
]

def train(trainarray, texttopredict):
    word_counts = {
        "positiv": defaultdict(int),
        "negativ": defaultdict(int),
    }
    class_counts = {"positiv": 0, "negativ": 0}
    total_words = {"positiv": 0, "negativ": 0}
    vocabulary = set()

    # Trainingsdaten verarbeiten
    for text, label in trainarray:
        words = text.split()
        class_counts[label] += 1
        total_words[label] += len(words)
        for word in words:
            word_counts[label][word] += 1
            vocabulary.add(word)

    # Vorhersage vorbereiten
    words_to_predict = texttopredict.split()
    results = {}

    for label in ["positiv", "negativ"]:
        # Start mit log(P(Klasse))
        log_prob = math.log(class_counts[label] / sum(class_counts.values()))
        for word in words_to_predict:
            # Laplace-Glättung
            word_frequency = word_counts[label][word]
            word_prob = (word_frequency + 1) / (total_words[label] + len(vocabulary))
            log_prob += math.log(word_prob)
        results[label] = log_prob

    # Höchste Wahrscheinlichkeit auswählen
    predicted_class = max(results, key=results.get)
    return predicted_class

# Beispiel
print(train(training_data, "gut toll i am jhon wick schlecht schlecht"))        # Erwartet: positiv
print(train(training_data, "schlecht schlecht"))  # Erwartet: negativ
