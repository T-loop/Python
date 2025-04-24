def tagebuch_eintrag_schreiben():
    with open("tagebuch.txt", "a") as datei:  # 'a' = an Datei anhängen
        while True:
            eintrag = input("Eintrag (leer zum Beenden): ")
            if eintrag.strip() == "":
                break
            datei.write(eintrag + "\n")
        print("Einträge gespeichert.\n")


def tagebuch_anzeigen():
    try:
        with open("tagebuch.txt", "r") as datei:
            inhalt = datei.read()
            print("\n--- Dein Tagebuch ---")
            print(inhalt)
            print("---------------------\n")
    except FileNotFoundError:
        print("Noch keine Einträge vorhanden.\n")


# 🔄 Hauptmenü-Schleife
while True:
    print("📝 Tagebuch-Menü:")
    print("1 - Neuen Eintrag hinzufügen")
    print("2 - Tagebuch anzeigen")
    print("3 - Beenden")

    auswahl = input("Wähle eine Option: ")

    if auswahl == "1":
        tagebuch_eintrag_schreiben()
    elif auswahl == "2":
        tagebuch_anzeigen()
    elif auswahl == "3":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte 1, 2 oder 3 eingeben.\n")
