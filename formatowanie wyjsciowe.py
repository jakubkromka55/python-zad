# 1.

name = "Adam"
age = 22
height = 182

# Drukowanie danych ucznia
print(f"My name is {name}")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age + 6} years old.")


# 2. dochod rodziny na osobe

# dochod ojca matki liczba osob
father_income = 5450
mother_income = 4920
family_members = 5

# calkowity dochod rodziny
total_income = father_income + mother_income

# dochod na osobe
income_per_person = total_income / family_members

# wynik w czytelnej formie
print(f'Total family income is {total_income} PLN, and income per person is {income_per_person:.2f} PLN.')


# 3. 

a = 3
b = 5

# wyrazenia z wynikami
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')  # wynik dzielenia zaokroglony do 2 miejsc po ,
