from os import system
import time
from random import seed
from random import randint

seed(time.time())

while True:
    while True:
        system('cls')
        value = randint(1, 3)
        print(value)
        print ("Gra w papier-kamień-nożyce. Wpisz:\n1. Papier\n2. Kamień\n3. Nożyce")
        txt = input()
        if txt != "1" and txt !="2" and txt != "3":
            system('cls')
            print("Wpisz poprawną wartość")
        elif txt == "1" or "2" or "3":
            break

    if int(txt) == value:
        print("Remis")
        input()
    elif int(txt) == 1 and value == 2 or int(txt) == 2 and value == 3 or int(txt) == 3 and value == 1:
        print("Wygrana")
        break
    else:
        print("Przegrana")
        input()
