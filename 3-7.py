# 3.program do zmiany 2 wart zmiennych

x = 7
y = 34
z = 0 # dodatkowa zmienna
print("przed zmiana: x=", x, "y=", y)

# zmiana wart
z = x
x = y
y = z

print("po zmiana: x=", x, "y=", y)


# 4. zmienia z km/h na ms/s

speed_kmh = 70
speed_ms = speed_kmh * 0.2778
print(speed_kmh, "km/h = ", speed_ms, "m/s")


# 5. kalkulator przekatna prost

import math  # modul math

a = 5  # dl 1 boku
b = 8  # dl 2 boku 

# oblicznie za pomoca pitagorasa
przekatna = math.sqrt(a**2 + b**2)

# Wyświetlenie wyniku
print("dlugosc przekatna:", przekatna)


# 6. odleglosc

import math 

# podaj wzrost w m
wysokosc = float(input("podaj wysokosc obserwatora w metrach: "))

# odleglosc horyzont ze wzoru d = 3,57 * √h
odleglosc = 3.57 * math.sqrt(wysokosc)

# wynik
print(f"odległosc do horyzontu z wysokości {wysokosc} m wynosi: {odleglosc:.2f} km")

# odleglosc horyzontu dla 1.7 m (wzrost osoby) i 20 m (wysokosc okna hotelowego)
odleglosc_na_plazy = 3.57 * math.sqrt(1.7)
odleglosc_z_okna = 3.57 * math.sqrt(20)

# wyniki dla 2 przykladow
print(f"na plazy (wzrost 1.7 m): {odleglosc_na_plazy:.2f} km")
print(f"z okna hotelu (wysokosc 20 m): {odleglosc_z_okna:.2f} km")


# 7. populacja ludzi 

populacja_swiata = 8000000000  # calkowaita populacja
populacja_pn = 7200000000     # polkula polnocna
populacja_ps = populacja_swiata - populacja_pn  # polkula poludniowa

# odsetka polkoli polnocnej
odsetek_pn = (populacja_pn / populacja_swiata) * 100

# odetka poludniowa
odsetek_ps = (populacja_ps / populacja_swiata) * 100

print("Populacja świata: ", populacja_swiata)
print("Populacja półkuli północnej: ", populacja_pn)
print("Odsetek populacji półkuli północnej: ", round(odsetek_pn, 2), "%")

print("Populacja półkuli południowej: ", populacja_ps)
print("Odsetek populacji półkuli południowej: ", round(odsetek_ps, 2), "%")


# 8. srednia ocen

math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print(average)