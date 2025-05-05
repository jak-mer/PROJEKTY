"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Merta
email: merta.arch@gmail.com
"""
# Zdrojové texty:
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
]

#################################### Vstupní proměnné:
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
cara = "-"*40
pocet_textu = len(TEXTS)

#################################### Zadání uživatelského jména a hesla:
prihlasovaci_jmeno = input("username:")
heslo = input("password:")

#################################### Ověření uživatelského jména a hesla:
if prihlasovaci_jmeno in uzivatele and uzivatele[prihlasovaci_jmeno] == heslo: 
    print(cara)
    print(
f"""Welcome to the app, {prihlasovaci_jmeno} 
We have {pocet_textu} texts to be analyzed."""
)
    print(cara)
else:
    print("unregistered user, terminating the program..")
    quit()

#################################### Vyber textu a chybové hlášky:
vyber_textu = (input(f"Enter a number btw. 1 and {len(TEXTS)} to select:"))

rozsah = tuple(range(1, pocet_textu + 1)) # tuple = (1, 2, 3, ...)

# Kontrola vstupu
if not vyber_textu.isdigit():
    print("Input not a number, terminating the program..")
    print(cara)
    quit()
else:
    vyber_textu = int(vyber_textu)  # Převod na celé číslo
    if vyber_textu not in range(1, pocet_textu + 1):
        print(f"Number {vyber_textu} is not in range, terminating the program..")
        print(cara)
        quit()

print(cara)

#################################### Vytvoření seznamu jednotlivých slov z textu:
surova_slova = TEXTS[vyber_textu - 1].split()

#################################### Odstranění interpunkce a očištění textu
#################################### + slovníková komprehenze

odstranit_znaky = str.maketrans("", "", ",.:;")
vycistena_slova = [slovo.translate(odstranit_znaky) for slovo in surova_slova]

""" Původní verze:
vycistena_slova = []
for slovo in surova_slova:
    ocistene_slovo = slovo.strip(",.:;")
    vycistena_slova.append(ocistene_slovo)
    """

#################################### Počet slov ve vybraném textu:
pocet_slov = len(vycistena_slova)

print(f"There are {pocet_slov} words in the selected text.")

#################################### Nastavení proměnných a seznamů pro jednotlivé kategorie:
slova_s_velkym_pismenem = list()
slova_kapitalky = list()
slova_mala = list()
slova_cisla = list()

#################################### Sjednocená smyčka:
for slovo in vycistena_slova:
    if slovo.istitle():
        slova_s_velkym_pismenem.append(slovo)
        
    elif slovo[:].isupper():
        slova_kapitalky.append(slovo)

    elif slovo[:].islower():
        slova_mala.append(slovo)

    elif slovo[:].isnumeric():
        cislo = int(slovo)
        slova_cisla.append(cislo)

#################################### Délky jednotlivých seznamů:
pocet_slov_s_velkym_pismenem = len(slova_s_velkym_pismenem)
pocet_slov_kapitalkama = len(slova_kapitalky)
pocet_slov_mala = len(slova_mala)
pocet_slov_cisla = len(slova_cisla)
soucet_cisel = sum(slova_cisla)

#################################### Vytištění výsledků:
print(f"There are {pocet_slov_s_velkym_pismenem} titlecase words.")
print(f"There are {pocet_slov_kapitalkama} uppercase words.")
print(f"There are {pocet_slov_mala} lowercase words.")
print(f"There are {pocet_slov_cisla} numeric strings.")
print(f"The sum of all the numbers {soucet_cisel}.")

#################################### Hlavička sloupcového grafu:
print(cara)
print("LEN|   OCCURENCES       |NR.")
print(cara)

#################################### Délky slov a počet jejich výskytů:
#################################### Slovník pro uložení délek slov a jejich počtu
delky_slov = {}

for slovo in vycistena_slova:
    delka = len(slovo)
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1

#################################### Výstup formátovaný podle požadavků:
for delka, pocet in sorted(delky_slov.items()):
    hvezdicky = "*" * pocet
    print(f"{delka:>3}|{hvezdicky:<20}|{pocet}")