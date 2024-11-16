# +
print(7 + 4)

# srednia 2 liczb
print((30 + 10) / 2)

# potegowanie
print(2 ** 3)

# porownanie
print(7 > 5)

# pole kola
r = 4
obszar = 3.14159 * r * r
print(obszar)

# zaokrog 2 miejsc po ,
print(round(obszar, 2))

# laczenie imienia i nazwiska
imie = "Mary"
nazwisko = "Brown"
pelna_nazwa = imie + ' ' + nazwisko
print(pelna_nazwa)

# dlugosc nazwiska i imienia
print(len(pelna_nazwa))

# pole trojkata a=5 h=4
a = 5
h = 4
pole_trojkata = 0.5 * a * h
print(pole_trojkata)

# srednia arytmetyczna zaokrąglona 2 miejsc po ,
srednia = (7 + 12 + 31) / 3
print(round(srednia, 2))


# BMI kalkulator
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')
