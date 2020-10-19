#PROTOTYPOWY PLIK PROJEKTOWY
def wybierz_rodzaj_przelicznika():
    jaki_przelicznik = input()
    if jaki_przelicznik == "CF":
        print("Przeliczasz Celcjusze na Farenheity")
        C_na_F() 
    elif jaki_przelicznik == "FC":
        print("Przeliczasz Farenheity na Celcjusze")
        F_na_C() 
    else:
        print("Źle wprowadzone dane spróbuj ponownie!")
        wybierz_rodzaj_przelicznika()

def C_na_F():
    Celcjusze = input("Podaj ilość stopni celcjusza: ")
    try:
        Celcjusze = float(Celcjusze) #zamieniamy celcjusze na liczbę
        wynik = 32 + 9/5 * Celcjusze #przeliczamy używając wzoru
        wynik = round(wynik,2) #zaokrąglenie wyniku do 2 miejsc po przecinku
        print(Celcjusze,"°C = ",wynik,"°F") #wypisanie wyniku
    except ValueError: #jeśli podane stopnie nie dają się zamienić na liczbę z przecinkiem podaj jeszcze raz
        print("Złe dane spróbuj jeszcze raz")
        C_na_F()
        
def F_na_C():
    Fahrenheity = input("Podaj ilość stopni fahrenheita: ")
    try:
        Fahrenheity = float(Fahrenheity) #zamieniamy farenheity na liczbę
        wynik = 5/9 * (Fahrenheity - 32) #przeliczamy używając wzoru
        wynik = round(wynik,2) #zaokrąglenie wyniku do 2 miejsc po przecinku
        print(Fahrenheity,"°F = ",wynik,"°C") #wypisanie wyniku
    except ValueError: #jeśli podane stopnie nie dają się zamienić na liczbę z przecinkiem podaj jeszcze raz
        print("Złe dane spróbuj jeszcze raz")
        F_na_C()


print("- - - WDI moduł 1 zadanie 5 - - -")
print("Aby przeliczyć °C na °F wpisz CF")
print("Aby przeliczyć °F na °C wpisz FC")
wybierz_rodzaj_przelicznika()
