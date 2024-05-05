import random
import os
import time
import importlib

module=importlib.import_module("rysunki")
def dic():
    owoce = ["banan", "gruszka", "jabłko", "śliwka", "arbuz", "malina", "truskawka", "kiwi", "winogrono", "mandarynka"]
    kolory = ["czerwony", "zielony", "żółty", "fioletowy", "pomarańczowy", "granatowy", "różowy", "brązowy", "czarny", "biały"]
    pojazdy = ["samochód", "rower", "motocykl", "autobus", "ciężarówka", "tramwaj", "skuter", "taksówka", "pociąg", "helikopter"]
    animals = ["pies", "kot", "ptak", "ryba", "królik", "koń", "słoń", "tygrys", "żółw", "wąż"]
    professions = ["lekarz", "nauczyciel", "informatyk", "kucharz", "architekt", "policjant", "inżynier", "sprzedawca", "dziennikarz", "piekarz"]
    electronics = ["telewizor", "telefon", "komputer", "konsola", "kamera", "słuchawki", "głośniki", "router", "smartwatch"]
    foods = ["pizza", "spaghetti", "sałatka", "hamburger", "sushi", "kanapka", "schabowy", "pierogi", "ryż", "kurczak"]
    drinks = ["woda", "herbata", "kawa", "sok", "cola", "piwo", "wino", "whisky", "mleko", "koktajl"]
    countries = ["Polska", "Niemcy", "Francja", "Włochy", "Hiszpania", "Chiny", "Japonia", "Brazylia", "Australia"]
    sports = [ "koszykówka", "siatkówka", "tenis", "łyżwiarstwo", "pływanie", "bieganie", "narciarstwo", "golf"]
    furniture = ["stół", "krzesło", "sofa", "łóżko", "szafa", "komoda", "biurko", "toaletka", "regał", "lampa"]
    tools = ["młotek", "śrubokręt", "wkrętarka", "piła", "klucz", "nożyczki", "pilnik", "szczypce", "kombinerki", "łom"]
    plants = ["drzewo", "kwiat", "trawa", "krzew", "kwiatostan", "liść", "paproć", "pnącze", "porost"]
    category=["owoce", "kolory", "pojazdy", "zwierzęta", "zawody", "kraje", "sporty", "meble", "elektronika", "jedzenie", "napoje", "narzędzia", "rośliny"]
    random_kategory=random.choice(category)
    if random_kategory=="kolory":
        random_word=random.choice(kolory)
    elif random_kategory=="owoce":
        random_word=random.choice(owoce)
    elif random_kategory=="pojazdy":
        random_word=random.choice(pojazdy)
    elif random_kategory=="zwierzęta":
        random_word=random.choice(animals)
    elif random_kategory=="zawody":
        random_word=random.choice(professions)
    elif random_kategory=="kraje":
        random_word=random.choice(countries)
    elif random_kategory=="napoje":
        random_word=random.choice(drinks)
    elif random_kategory=="sporty":
        random_word=random.choice(sports)
    elif random_kategory=="meble":
        random_word=random.choice(furniture)
    elif random_kategory=="elektronika":
        random_word=random.choice(electronics)
    elif random_kategory=="jedzenie":
        random_word=random.choice(foods)
    elif random_kategory=="narzędzia":
        random_word=random.choice(tools)
    elif random_kategory=="rosliny":
        random_word=random.choice(plants)
    return random_kategory,random_word


def start_game():
    used_letters=[]
    category,word=dic()
    zycia=5
    word_length=len(word)
    tab=['_' for _ in range(word_length)]
    while True:
        if zycia==4:
            print(module.rys6)
        elif zycia==3:
            print(module.rys5)
        elif zycia==2:
            print(module.rys3)
        elif zycia==1:
            print(module.rys4)
        elif zycia==0:
            print(module.rys2)
            print("Poprawne hasło: ", word)
            menu_interface()
            break
        print("Kategoria: ",category)
        print("Pozostałe życia: ", zycia)
        print("Użyte literki: "," ".join(used_letters))
        print(' '.join(tab))
        literka=input("Wpisz literę ")
        used_letters.append(literka)

        position=[]
        index=0
        if len(literka)==1 and literka.isalpha():
            if literka in word:
                while True:
                    try:
                        index=word.index(literka,index)
                        position.append(index)
                        index+=1
                    except ValueError:
                        break
                for index in position:
                    tab[index]=literka
            else:
                zycia-=1
            if not "_" in tab:
                os.system('cls')
                print("Kategoria: ",category)
                print("Pozostałe życia: ",zycia)
                print(' '.join(tab))
                print("WYGRAŁEŚ!")
                menu_interface()
            os.system("cls")

        else:
            print("błąd!")
            time.sleep(1)
            os.system("cls")

print("WITAJ W GRZE!")
def menu_interface():
    menu=input("1-Zagraj\n2-Wyjdź z gry\n")
    while True:
        if menu=='1':
            os.system("cls")
            start_game()
            break
        elif menu=='2':
            exit(1)
        else:
            print("błąd")
            menu_interface()

menu_interface()