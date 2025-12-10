import math
from collections import Counter

# Funktion, um Entropie zu berechnen (also wie unordentlich die Antworten sind)
def berechne_entropie(daten):
    label_liste = [eintrag[-1] for eintrag in daten]  # letzte Spalte = Entscheidung (z.B. "ja", "nein")
    zaehler = Counter(label_liste)  # wie oft kommt "ja" und "nein" vor?
    entropie = 0.0

    for label in zaehler:
        wahrscheinlichkeit = zaehler[label] / len(daten)  # Anteil dieses Labels
        entropie -= wahrscheinlichkeit * math.log2(wahrscheinlichkeit)  # Formel für Entropie

    return entropie

 #Funktion, um den besten Attribut (Spalte) zu finden, mit dem man die besten Fragen stellen kann
def finde_bestes_attribut(daten):
    anzahl_attribute = len(daten[0]) - 1  # letzte Spalte ist die Antwort, die überspringen wir
    grund_entropie = berechne_entropie(daten)
    bester_gain = 0.0
    bestes_attribut = -1

    # Wir schauen jede Spalte (außer der letzten) an
    for i in range(anzahl_attribute):
        werte = set([eintrag[i] for eintrag in daten])  # mögliche Werte in dieser Spalte
        neue_entropie = 0.0

        for wert in werte:
            teilmenge = [eintrag for eintrag in daten if eintrag[i] == wert]
            gewicht = len(teilmenge) / len(daten)
            neue_entropie += gewicht * berechne_entropie(teilmenge)

        informationsgewinn = grund_entropie - neue_entropie

        if informationsgewinn > bester_gain:
            bester_gain = informationsgewinn
            bestes_attribut = i

    return bestes_attribut

#  Hauptfunktion zum Erstellen des Entscheidungsbaums
def baue_baum(daten, attribut_namen):
    labels = [eintrag[-1] for eintrag in daten]

    #  Wenn alle Labels gleich sind, brauchen wir nicht weiter fragen
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    #  Wenn keine Attribute mehr übrig sind
    if len(daten[0]) == 1:
        return Counter(labels).most_common(1)[0][0]  # häufigste Antwort zurückgeben

    bestes_attribut = finde_bestes_attribut(daten)
    attribut_name = attribut_namen[bestes_attribut]

    baum = {attribut_name: {}}

    werte = set([eintrag[bestes_attribut] for eintrag in daten])

    for wert in werte:
        teilmenge = [eintrag[:bestes_attribut] + eintrag[bestes_attribut+1:] for eintrag in daten if eintrag[bestes_attribut] == wert]
        neue_attribut_namen = attribut_namen[:bestes_attribut] + attribut_namen[bestes_attribut+1:]
        baum[attribut_name][wert] = baue_baum(teilmenge, neue_attribut_namen)

    return baum

#  Unsere kleinen Beispieldaten (Wetter, Temperatur, Spielen)
daten = [
    ["sonnig", "warm", "ja"],
    ["sonnig", "kalt", "nein"],
    ["regen", "warm", "nein"],
    ["sonnig", "warm", "ja"],
    ["regen", "kalt", "nein"]
]

attribut_namen = ["Wetter", "Temperatur"]

#  Entscheidungsbaum bauen
baum = baue_baum(daten, attribut_namen)
print("hello")

# Baum anzeigen
import pprint
pprint.pprint(baum)
