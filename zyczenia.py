import datetime

rok = datetime.datetime.now().year

imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = rok - rok_urodzenia
spersonalizowana_wiadomosc = input("Wpisz spersonalizowaną wiadomość: ")
imie_nadawcy = input("Podaj imię nadawcy: ")

print("-" *50)
print(f"""
{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin! \n
{spersonalizowana_wiadomosc} \n
{imie_nadawcy}
""")
print("-" *50)
