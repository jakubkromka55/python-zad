# 1.definicje zmiennych
company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

# wypisanie wartości i typow zmiennych
zmienne = {
    "company": company,
    "phone": phone,
    "employees": employees,
    "remote_work": remote_work,
    "big_company": big_company,
    "income": income,
    "income_per_person": income_per_person,
}

for nazwa, value in zmienne.items():
    print(f"zmienna: {nazwa}, wartosc: {value}, typ: {type(value)}")



# 2.program oblicza sume trzech licz
numer1 = 71
numer2 = 14
numer3 = 7  # Dodajemy trzecią liczbę
wynik = numer1 + numer2 + numer3  # suma trzech liczb

# wyswietlamy wyniki
print(numer1)
print(numer2)
print(numer3)  # drukujemy trzecia liczbę
print('wynik sumowania: ', wynik)  # drukujemy wynik sumy


