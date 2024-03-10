# PROJEKT : KALULATOR BMI
# DATA    : 16.11.2023
# KODOWAL : Kamil Sulewski

import datetime
x = datetime.datetime.now()

print("WITAM W KALKULATORZE BMI")
przywitaj = "Cześć"
imie = input("Podaj imię: ")
print(przywitaj+" "+imie+" mamy godzine: "+x.strftime("%H:%M"))
waga = input("Podaj swoja wage w kg: ")
wzrost = input ("OK to podaj jeszcze swoj wzrost w cm: ")
print()
bmi= "Twoje BMI to: "

waga2= waga.replace(",",".")
wzrost2= wzrost.replace(",",".")



szer = 44

try:
    if  0<float(waga2) and 0<float(wzrost2):
        wyliczenie = float(waga2) / ((float(wzrost2)*0.01)**2)
        print(bmi, round(wyliczenie, 2))
    if 16 > wyliczenie >0 :
        print()
        print("OJEJ Twoje BMI swiadczy o skrajnym wyglodzeniu :(")
        print("Zalecamy szybki kontakt z pomoca medyczna!")
    elif 16 <= wyliczenie <= 16.99 :
        print("Ups... Twoje BMI wskazuje na wychudzenie :(")
        print("Zachecamy do poszukania pomocy")
    elif 17 <= wyliczenie <= 18.49 :
        print()
        print("NIEDOWAGA")
        print("Zmien swoje nawyki zywieniowe i zadbaj o zdrowie")
    elif 18.5 <= wyliczenie <= 22.99 :
        print()
        print("BRAWO! JEST DOBRZE :)")
        print("Pamietaj o posilkach a zachowasz dobry wskaznik ;)")
    elif 23 <= wyliczenie <= 24.99 :
        print()
        print("BRAWO! JEST DOBRZE :)")
        print("Uwazaj na kalorie  by zachowac dobry wskaznik ;)")
    elif 25 <= wyliczenie <= 27.49 :
        print()
        print("Lekka nadwaga")
        print("Zmien swoje nawyki zywieniowe i zadbaj o zdrowie")
    elif 27.5 <= wyliczenie <= 29.99 :
        print()
        print("Wyrazna NADWAGA")
        print("Zmien swoje nawyki zywieniowe, troche ruchu i zadbaj o zdrowie")
    elif 30 <= wyliczenie <= 34.99 :
        print()
        print("Ups... Twoje BMI wskazuje na otylosc I stopnia")
        print("Zachecamy do poszukania pomocy")
    elif 35 <= wyliczenie <= 39.99 :
        print()
        print("Jest ZLE!")
        print("Twoje BMI wskazuje na otylosc II stopnia")
        print("Potrzebujesz  lekarza :(")
    elif 40 <= wyliczenie :
        print()
        print(":( OJEJ  Cierpisz na otylosc III stopnia! ")
        print("Stanowczo potrzebna pomoc medyczna! :(")
    if  0<wyliczenie :
        print("-" * szer)
        print("|  BMI     |     Osoba        |    Data    |")
        print("*" * szer)
        print("|{:6.2f}    | {:16s} | {:10s} |".format(round(wyliczenie, 2), imie, x.strftime("%d.%m.%Y")))
        print("-" * szer)
except ValueError :
    print()
    print("Podales dane w sposob niepoprawny!")
    print("A jako wage podales: " + waga)
    print("Jako wzrost podales: "+ wzrost)
    print("Zacznij na nowo!")
except :
    print()
    print("Wartosci WAGA i WZROST  musza byc dodatnie!")
    print("Zacznij na nowo!")

input()
