# Coded by KBJay
from random import randint
import time

print('----------')
ls_lvl = [1,2,3,4]           # List of difficulty levels
def menu():
    print('***MENU***')
    print('----------')
    print('Select difficulty level:')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    print('4. Horror')
 
menu()
print('')
selected_level = input("I'm choosing: ")
try:
    slected_level = int(selected_level)
    
# Checking: Is selected level a integer
except ValueError: 
# Checking if it's not then an error message appears 
    print('----------')
    print('[!] Error. Select number from 1 to 4')
   
def Tries():
	
    cn_try = 0  # Count of tries
    while True:
        guess = input('I think it is: ')
        cn_try = int(cn_try) +1
# Counting how many times user have tried to guess
        print('----------')
       
        try:
            guess = int(guess)
# Checking: Is the guessed number by user is a integer
 
        except ValueError:
# If it's not then an error message appears

            print("[!] Error. Guessed number isn't a number")
            print('')
            continue
       
        if guess < win_number:
# If the number guessed by user number is smaller than the winning number:
			
            print('Not enough')
            print('')
            continue
           
        if guess > win_number:
# Or if the guessed by user number is greater than the winning number:
            print('Too much')
            print('')
            continue
           
        if guess == win_number and selected_level != 4:
# If the user won, and the difficulty level is not the hardest one, app is congratulating, saying which try it was, and suggesting to try higher difficulty level

            print('Congratulations you win! It was your ' + str(cn_try) + ' try. Try again with higher difficulty level')
           
        if guess == win_number and selected_level == 4:
# If the user won on the highest level, app is congratulationg, and saying which try it was
            print("Wow. You're insane, congratulations, it was your " + str(cn_try) + " try!")
           
        time.sleep(2)
        print('')
        exit()
       
if selected_level == 1:
	win_number = randint(1,10)
    win_number = int(win_number)
    print('I thought about number from range [1-10]. Guess what number is it')
   
if selected_level == 2:
    win_number = randint(1,50)
    win_number = int(win_number)
    print('I thought about number from range [1-50]. Guess what number is it')
 
if selected_level == 3:
    win_number = randint(1,100)
	win_number = int(win_number)
    print('I thought about number from range [1-100]. Guess what number is it')
 
if selected_level == 4:
    win_number = randint(1,1000)
    win_number = int(win_number)
    print('I thought about number from range [1-1000]. Guess what number is it')
   
if selected_level not in ls_lvl:
    print("[!] Error. You've selcted prohibited difficulty level. Select from [1-4]")
 
Tries()
