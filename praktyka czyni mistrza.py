# 2. 
import math

# Determinowanie wartości promienia i liczby pi
r = float(input("Enter the radius of the circle: "))
pi = math.pi  # Pi is a constant value available in the math module

# Obliczanie pola
area = pi * r ** 2

# Obliczanie obwodu
circumference = 2 * pi * r

print(f'Radius: {r}')
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')



# 3.
# Program, który odczytuje temperaturę w stopniach Celsjusza z klawiatury.
# Następnie oblicza i drukuje temperaturę w Kelvinach oraz Fahrenheitach.

# temp w c
celsius = float(input("Enter temperature in Celsius: "))

# temp z c na k
kelvin = celsius + 273.15

# temp z c na f
fahrenheit = (celsius * 9/5) + 32

print(f'Temperature in Celsius: {celsius}°C')
print(f'Temperature in Kelvin: {kelvin:.2f} K')  # .2f - dwie liczby po przecinku
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} °F')


# 4. drukuje wzrost w cm i w stopach i calach.

cm = 191  

# obliczenie liczby stóp
feet = cm // 40.38

# obliczenie liczby cali
remaining_cm = cm % 40.38
inches = remaining_cm // 2.54

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')


# 5. odczytuje kod swift

swift = input('Enter SWIFT code: ')
bank_code = swift[:4]
country_code = swift[4:6]

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')


# 6. koszt transportu towaru

distance = int(input('Enter distance in km: '))  # Odległość w km
fuel_price = float(input('Enter fuel price per liter: '))  # Cena paliwa za litr
fuel_consumption = float(input('Enter fuel consumption per 100 km (liters): '))  # Zużycie paliwa na 100 km

# całkowite zużycie paliwa na dystansie
total_fuel_consumption = (fuel_consumption / 100) * distance  # Zużycie paliwa na całą trasę

# Całkowity koszt paliwa
total_cost = total_fuel_consumption * fuel_price  # Całkowity koszt paliwa

print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total transport cost: {total_cost:.2f} pln')  



# 7.liczby dziesiętnej na system binarny i szesnastkowy

number = int(input('Enter number: '))

# system binarny i szesnastkowy
binary_number = bin(number)
hexadecimal_number = hex(number)

print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')







