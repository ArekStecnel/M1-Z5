import os
import requests


def wybierz_rodzaj():                                               #funkcja zależnie od tego co wpisaliśmy wykonuje określone rzeczy
    co_wyswietlamy = input()
    if co_wyswietlamy == "CF":                                      #po wpisaniu CF zamienia celcjusze na farenheity
        print("Przeliczasz Celcjusze na Farenheity")
        C_na_F() 
    elif co_wyswietlamy == "FC":                                    #po wpisaniu FC zamienia farenheity na celcjusze
        print("Przeliczasz Farenheity na Celcjusze")
        F_na_C() 
    else:                                                           #Po wpisaniu innej wartości niż FC lub CF funkcja sprawdza czy z danego "miasta" można pobrać rożne wartości
        try:
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d8cb46b72f35eb7b3563fba6ff9cd3fe&q=' + co_wyswietlamy
            json_data = requests.get(api_address).json()            #dane są pobierane z strony internetowej z plikiem o rozszerzeniu json
            temperatura_K = json_data['main']['temp']               #pobranie klucza temp z warotscią temperatury w kelwinach
            temperatura_C = temperatura_K - 273                     #zamiana kelwinów na celcjusze
            temperatura_F = 32 + 9/5 * temperatura_C                #zamiana celcjuszy na kelwiny
            print("W mieście",co_wyswietlamy, "temperatura wynosi", round(temperatura_C,2), "°C (", round(temperatura_F,2),"°F )")  #wypisanie danych
            os.system("pause")                                      #Zatrzymanie konsoli
        except KeyError:                                            #Przy błędnym wpisaniu miasta nie można odczytać danych przez co musimy ponownie wprowadzić dane 
            print("Złe dane spróbuj jeszcze raz")
            wybierz_rodzaj()


def C_na_F():                                                       #Funkcja zamieniajaca celcjusze na farenheity

    Celcjusze = input("Podaj ilość stopni celcjusza: ")             #Wprowadzamy ilość celcjuszy
    try:
        Celcjusze = float(Celcjusze)                                #zamieniamy celcjusze na liczbę
        wynik = 32 + 9/5 * Celcjusze                                #przeliczamy używając wzoru
        wynik = round(wynik,2)                                      #zaokrąglenie wyniku do 2 miejsc po przecinku
        print(Celcjusze,"°C =",wynik,"°F")                          #wypisanie wyniku
        os.system("pause")                                          #Zatrzymanie konsoli po wyświetleniu wyniku
    except ValueError:                                              #jeśli podane stopnie nie dają się zamienić na liczbę z przecinkiem podaj dane jeszcze raz
        print("Złe dane spróbuj jeszcze raz")
        C_na_F()

       
def F_na_C():                                                       #Funkcja zamieniajaca farenheity na celcjusze

    Fahrenheity = input("Podaj ilość stopni fahrenheita: ")         #Wprowadzamy ilość farenheitów
    try:
        Fahrenheity = float(Fahrenheity)                            #zamieniamy farenheity na liczbę
        wynik = 5/9 * (Fahrenheity - 32)                            #przeliczamy używając wzoru
        wynik = round(wynik,2)                                      #zaokrąglenie wyniku do 2 miejsc po przecinku
        print(Fahrenheity,"°F =",wynik,"°C")                        #wypisanie wyniku
        os.system("pause")                                          #Zatrzymanie konsoli po wyświetleniu wyniku
    except ValueError:                                              #jeśli podane stopnie nie dają się zamienić na liczbę z przecinkiem podaj dane jeszcze raz
        print("Złe dane spróbuj jeszcze raz")
        F_na_C()



print("- - - WDI moduł 1 zadanie 5 - - -")
print("Aby przeliczyć °C na °F wpisz CF")
print("Aby przeliczyć °F na °C wpisz FC")
print("Aby wyświetlić temprtaturę w danym mieście wpisz jego nazwę")
wybierz_rodzaj()
