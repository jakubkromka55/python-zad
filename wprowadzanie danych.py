# 1.

# pobiera imie i nazwisko drukuje pelne imie

# dane od uzytkownika
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

# laczenie imienia i nazwiska
full_name = first_name + ' ' + last_name

# wynik
print(f'Your first name is {first_name} and your last name is {last_name}.')
print(f'And your full name is {full_name}.')


# 2. obliczanie objetosci i powierzchni szes

# dlugosc boku
cube_side_string = input('Enter cube side: ')

# ciag na liczbe calkowita
cube_side = int(cube_side_string)

# obj i powierz
cube_volume = cube_side ** 3  # objętosc szescianu: a^3
cube_surface_area = 6 * (cube_side ** 2)  # powierzchnia szescianu: 6 * a^2

# wynik
print(f'The volume of a cube with side {cube_side} is {cube_volume}.')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}.')


# 3. obl obj i powierz prostopadl

# dane a b c
a = float(input('Enter the length of side a: '))
b = float(input('Enter the length of side b: '))
c = float(input('Enter the length of side c: '))

# obj
volume = a * b * c

# pole
area = 2 * (a * b + b * c + c * a)

# wynik
print(f'The volume of the cuboid with sides {a}, {b}, and {c} is {volume}.')
print(f'The surface area of the cuboid with sides {a}, {b}, and {c} is {area}.')


# 4. vat

# brutto
brutto = float(input('podaj kwote z vat: '))

# obl netto
netto = brutto / 1.23

# vat obl
vat = brutto - netto

# wynik z 2 miejsc po ,
print(f'bez vat: {netto:.2f}')
print(f'vat (23%): {vat:.2f}')


# 5.cena po rabacie


# dane
price_before_discount = float(input('podaj cene przed rabatem: '))
discount = float(input('podaj procent rabatu: '))

# po rabacie
price_after_discount = price_before_discount * (1 - discount / 100)

# roznica przed i po rabacie
price_difference = price_before_discount - price_after_discount

# wynik 2 miejsc po ,
print(f'cena przed rabatem: {price_before_discount:.2f}')
print(f'rabat: {discount:.2f}%')
print(f'cena po rabacie: {price_after_discount:.2f}')
print(f'roznica: {price_difference:.2f}')

