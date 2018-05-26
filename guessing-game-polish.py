from random import randint
import time
 
#Coded by KBJay')
ls_poz = [1,2,3,4]           # Lista poziomow
def menu():
    print('***MENU***')      # Menu poziomow
    print('----------')
    print('Wybierz poziom trudnosci:')
    print('1. Latwy')
    print('2. Sredni')
    print('3. Trudny')
    print('4. Koszmarny')
 
menu()
print('')
wybor = input('Wybieram: ')
try:
    wybor = int(wybor)
except ValueError:         							# Sprawdzenie czy wprowadzony poziom trudnosci jest intem
    print('----------')
    print('[!] Blad. Podaj liczbe z zakresu [1-4]')
   
def Proby():              							
# Funkcja odpowiadajaca za zgadywanie
    x = 1                  							
# X utworzony tylko po to, aby miec warunek w petli while
    il_los = 0
    while x > 0:
        los = input('Zgaduje ze to: ')   			
# Uzytkownik zgaduje liczbe
        il_los = int(il_los) +1 
# Licznik, pod koniec dzieki niemu, uzytkownik wie za ktorym razem trafil w wygrana liczbe
        print('----------')
       
        try:
            los = int(los)
# Weryfikacja czy liczba ktora uzytkownik podaje, jako prawdopodobna jest intem
 
        except ValueError:
            print('[!] Blad. Podaj liczbe z okreslonego wczesniej zakresu')
            print('')
            continue
# Jesli uzytkownik jako prawdopodobna liczbe przykladowo tekst
       
        if los < wynik:
            print('Za malo')
            print('')
            continue
# Jesli prawdopodbna liczba zdefiniowana przez uzytkownika jest mniejsza od tej wygranej
           
        if los > wynik:
            print('Za duzo')
            print('')
            continue          
# Jesli prawdopodbna liczba zdefiniowana przez uzytkownika jest wieksza od tej wygranej  
 
        if los == wynik and wybor != 4:
            print('Gratulacje udalo Ci sie! Byla to twoja ' + str(il_los) + ' proba. Sproboj jeszcze raz z trudniejszym poziomem')
# Jesli prawdopodbna liczba zdefiniowana przez uzytkownika jest liczba wygrana: 
         
        if los == wynik and wybor == 4:
            print('Wow. Jestes niesamowity, gratulacje, byla to twoja ' + str(il_los) + ' proba!')
# Jesli prawdopodbna liczba zdefiniowana przez uzytkownika jest liczba wygrana, a poziom trudnosci jest ustawiony jako 'Koszmarny' 
        time.sleep(2)
        print('')
        exit()
       
if wybor == 1:
    wynik = randint(1,10)
    wynik = int(wynik)
    print('Pomyslalem sobie liczbe z zakresu [1-10]. Zgadnij co to za liczba')
   
if wybor == 2:
    wynik = randint(1,50)
    wynik = int(wynik)
    print('Pomyslalem sobie liczbe z zakresu [1-50]. Zgadnij co to za liczba')
 
if wybor == 3:
    wynik = randint(1,100)
    wynik = int(wynik)
    print('Pomyslalem sobie liczbe z zakresu [1-100]. Zgadnij co to za licba')
 
if wybor == 4:
    wynik = randint(1,1000)
    wynik = int(wynik)
    print('Pomyslalem sobie liczbe z zakresu [1-1000]. Zgadnij co to za liczba')
   
if wybor not in ls_poz:
    print('[!] Blad. Podano niedozwolony poziom trudnosci. Wybierz poziom z zakresu [1-4]')
 
Proby()
