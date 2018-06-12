from random import randint
import time
 
print('[i] Coded by KBJay')
print('----------')
ls_poz = [1,2,3,4]           #lista poziomow
def menu():
    print('***MENU***')
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
except ValueError:           #Sprawdzenie czy wybor jest intem
    print('----------')
    print('[!] Blad. Podaj liczbe z zakresu [1-4]')
   
def Proby():
    x = 1
    il_los = 0
    while x > 0:
        los = input('Zgaduje ze to: ')
        il_los = int(il_los) +1
        print('----------')
       
        try:
            los = int(los)
 
        except ValueError:
            print('[!] Blad. Podaj liczbe z okreslonego wczesniej zakresu')
            print('')
            continue
       
        if los < wynik:
            print('Za malo')
            print('')
            continue
           
        if los > wynik:
            print('Za duzo')
            print('')
            continue
           
        if los == wynik and wybor != 4:
            print('Gratulacje udalo Ci sie! Byla to twoja ' + str(il_los) + ' proba. Sproboj jeszcze raz z trudniejszym poziomem')
           
        if los == wynik and wybor == 4:
            print('Wow. Jestes niesamowity, gratulacje, byla to twoja ' + str(il_los) + ' proba!')
           
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
    exit()
 
Proby()
