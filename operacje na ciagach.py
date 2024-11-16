# 1. oblicza liczba znakow w imieniu itd

# Zprzechowuje imioe nazwisko
imie = 'Robert'   
nazwisko = 'Kubica' 

# liczenie znakow
znaki_w_imieniu = len(imie)
znaki_w_nazwisku = len(nazwisko)
pelne_imie = imie + ' ' + nazwisko
znaki_w_pelnym_imieniu = len(pelne_imie)

# wymik
print(f'Twoje imię ma {znaki_w_imieniu} znaków')
print(f'Twoje nazwisko ma {znaki_w_nazwisku} znaków')
print(f'Twoje pełne imię ma {znaki_w_pelnym_imieniu} znaków')

# 2. wyswietlla inicjaly

imie = 'Robert'       
nazwisko = 'Kubica'    

print(imie[0] + nazwisko[0])

# 3. skrot uczelni

uniwersytet = "Krakow University of Economics"

print(uniwersytet[0] + uniwersytet[7] + uniwersytet[21])

# 4. szczegolne inf o pracowniku

employee = "Mr. John May, born on 1998-02-16"

# wyciaganie danych
imie = employee[4:8]
nazwisko = employee[9:12]
data_urodzenia = employee[21:]
inicjaly = imie[0] + nazwisko[0]

print(f'Name: {imie}')
print(f'Surname: {nazwisko}')
print(f'Born: {data_urodzenia}')
print(f'Initials: {inicjaly}')


# 5. formatowanie nr tel

phone = input('Enter phone number: ')

formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]

print(f'Phone number: {formatted_phone}')

# 6. drukuje reprezentacji num znak

# Drukowanie kodów numerycznych dla znaków
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')


# 7. z liter imienia


name = 'Kuba' 

# Przechodzimy przez każdą literę w imieniu i drukujemy jej kod numeryczny
for letter in name:
    print(f'The letter {letter} has a code {ord(letter)}')



# 8. obl liczby liter miedzy dwiema literami

first = input('Enter first letter: ')
last = input('Enter last letter: ')

# kody num liter
first_letter_code = ord(first)
last_letter_code = ord(last)

# obliczenie liczby liter między nimi
number_of_letters = abs(last_letter_code - first_letter_code) - 1

print(f'Between {first} and {last} is {number_of_letters} letters')


# 9. Program do konwersji kodów znaków na odpowiadające im znaki

print(chr(67), chr(111), chr(111), chr(108), chr(33))



# 10. string manipulation

movie = "The Lord of the Rings: The Return of the King"

# Drukowanie liczby znaków w tytule
print('Number of characters: ', len(movie))

# Drukowanie tytułu w dużych literach
print('Title in capital letters: ', movie.upper())

# Drukowanie tytułu w małych literach
print('Title in small letters: ', movie.lower())

# Liczenie, ile razy występuje samogłoska "e" w tytule
print('The letter "e" appears: ', movie.count('e'))

# Szukanie, gdzie w tekście znajduje się słowo "Lord"
print('The word "Lord" is at position: ', movie.find('Lord'))

# Szukanie, gdzie w tekście znajduje się słowo "dragon"
print('The word "dragon" is at position: ', movie.find('dragon'))






