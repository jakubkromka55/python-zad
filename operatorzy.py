# wyrazenia do obliczenia
wyniki = {
    "3 * 2 + 1": 3 * 2 + 1,
    "5 + 10 * 5": 5 + 10 * 5,
    "4 + 4 / 2 ** 2": 4 + 4 / 2 ** 2,
    "4 % 3 % 2 % 1": 4 % 3 % 2 % 1,
    "1 + 2 % 3 ** 4 * 5": 1 + 2 % 3 ** 4 * 5,
    "Prawda != Fałsz": True != False,
}

# wyswietlenie wynikow
for wyrazenie, wynik in wyniki.items():
    print(f"{wyrazenie} = {wynik}")

##

# poprawione wartosci do sprawdzenia
wyniki = [
    50,                        # int całk
    149.17,                    # float zmienn
    4 * 7,                     # int
    4.0 * 7,                   # float
    "Uniwersytet Ekonomiczny w Krakowie",  # str 
    True,                      # bool logiczne
    2 > 5                      # bool
]

# wyswietlanie typow danych
for wynik in wyniki:
    print(f"Wartosc: {wynik}, {type(wynik)}")

