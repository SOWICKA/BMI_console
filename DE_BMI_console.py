# PROJEKT: BMI-RECHNER
# DATUM: 16.11.2023
# CODIERT VON: Kamil Sulewski

import datetime
x = datetime.datetime.now()

print("WILLKOMMEN BEIM BMI-RECHNER")
begruesse = "Hallo"
name = input("Geben Sie Ihren Namen ein: ")
print(begruesse+" "+name+" es ist jetzt "+x.strftime("%H:%M"))
gewicht = input("Geben Sie Ihr Gewicht in kg ein: ")
groesse = input("OK, geben Sie nun Ihre Größe in cm ein: ")
print()
bmi = "Ihr BMI ist: "

gewicht2 = gewicht.replace(",", ".")
groesse2 = groesse.replace(",", ".")

breite = 44

try:
    if 0 < float(gewicht2) and 0 < float(groesse2):
        berechnung = float(gewicht2) / ((float(groesse2) * 0.01) ** 2)
        print(bmi, round(berechnung, 2))
    if 16 > berechnung > 0:
        print()
        print("OH JE, Ihr BMI deutet auf extremes Untergewicht hin :(")
        print("Wir empfehlen einen schnellen Kontakt mit medizinischer Hilfe!")
    elif 16 <= berechnung <= 16.99:
        print("Ups... Ihr BMI weist auf Untergewicht hin :(")
        print("Suchen Sie bitte Hilfe")
    elif 17 <= berechnung <= 18.49:
        print()
        print("UNTERGEWICHT")
        print("Ändern Sie Ihre Essgewohnheiten und achten Sie auf Ihre Gesundheit")
    elif 18.5 <= berechnung <= 22.99:
        print()
        print("GUT GEMACHT! ES GEHT IHNEN GUT :)")
        print("Denken Sie an Mahlzeiten, um einen guten Indikator zu behalten ;)")
    elif 23 <= berechnung <= 24.99:
        print()
        print("GUT GEMACHT! ES GEHT IHNEN GUT :)")
        print("Achten Sie auf Kalorien, um einen guten Indikator zu behalten ;)")
    elif 25 <= berechnung <= 27.49:
        print()
        print("Leichtes Übergewicht")
        print("Ändern Sie Ihre Essgewohnheiten und achten Sie auf Ihre Gesundheit")
    elif 27.5 <= berechnung <= 29.99:
        print()
        print("Deutliches ÜBERGEWICHT")
        print("Ändern Sie Ihre Essgewohnheiten, etwas Bewegung und achten Sie auf Ihre Gesundheit")
    elif 30 <= berechnung <= 34.99:
        print()
        print("Ups... Ihr BMI weist auf Adipositas Grad I hin")
        print("Suchen Sie bitte Hilfe")
    elif 35 <= berechnung <= 39.99:
        print()
        print("ES IST SCHLECHT!")
        print("Ihr BMI weist auf Adipositas Grad II hin")
        print("Sie benötigen einen Arzt :(")
    elif 40 <= berechnung:
        print()
        print(":( OH NEIN, Sie leiden an Adipositas Grad III!")
        print("Dringend medizinische Hilfe erforderlich! :(")
    if 0 < berechnung:
        print("-" * breite)
        print("|  BMI     |     Person        |    Datum    |")
        print("*" * breite)
        print("|{:6.2f}    | {:16s} | {:10s} |".format(round(berechnung, 2), name, x.strftime("%d.%m.%Y")))
        print("-" * breite)
except ValueError:
    print()
    print("Sie haben die Daten auf eine nicht korrekte Weise eingegeben!")
    print("Als Gewicht haben Sie eingegeben: " + gewicht)
    print("Als Größe haben Sie eingegeben: "+groesse)
    print("Beginnen Sie von Neuem!")
except:
    print()
    print("Die Werte GEWICHT und GRÖSSE müssen positiv sein!")
    print("Beginnen Sie von Neuem!")

input()

