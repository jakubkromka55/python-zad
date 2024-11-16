# 1. Program sprawdzający czy osoba jest zwolniona z płacenia podatków w Polsce

# wiek z klw
age = int(input('Enter age: '))

# czy zwolniona
no_tax = age <= 26

print(f'Exemption from paying taxes: {no_tax}')


# 2. dlugosc hasla

password = input('Enter password: ')

# czy >=8
password_ok = len(password) >= 8

print(f'Password length is valid: {password_ok}')


# 3. czy liczba parzysta

number = int(input('Enter number: '))

# czy parzysta (reszta z dzielenia przez 2 wynosi 0)
even = number % 2 == 0

print(f'Number is even: {even}')


# 4. czy można sciac
import math

circumference = float(input('Enter tree circumference in cm: '))

# srednica drzewa
diameter = circumference / math.pi

# czy mozna
tree_can_be_cut = diameter >= 50

print(f'Tree can be cut down: {tree_can_be_cut}')


# 5. czy pojazd z krk

car_number = input('Enter car registration number: ')

# sprawdza kk lub kr
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"

print(f'Car is from Krakow: {is_krakow}')

# 6. czy predkosc dozwolona

speed = int(input('Enter vehicle speed in km/h: '))

# czy dozwolona w przedziale
is_valid_speed = 40 <= speed <= 140

print(f'Is the speed valid? {is_valid_speed}')



#7. losowanie
import random

# Generowanie losowej liczby całkowitej w zakresie od 5 do 10
random_number = random.randint(5, 10)

print(random_number)


#8. 
import random

# 3 rzuty
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

# obliczanie
total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f'First roll: {dice_roll_1}')
print(f'Second roll: {dice_roll_2}')
print(f'Third roll: {dice_roll_3}')
print(f'Total sum of rolls: {total}')



# 9.
import random

# Generowanie wyniku rzutu kostką
dice_roll = random.randint(1, 6)

# sprawdza czy 1 lub 6
special_number = dice_roll == 1 or dice_roll == 6

print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')



# 10. 
import random

# rzyca kostka
computer = random.randint(1, 6)

# swoj typ liczby
you = int(input('Guess the number (from 1 to 6): '))

# sprawdza czy odgadł
if you == computer:
    print('You won: True')
else:
    print('You won: False')











