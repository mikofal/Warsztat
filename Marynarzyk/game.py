import random
import time
import os


def AI():
    reka=["papier","kamien","nozyce"]
    return random.choice(reka)


def start_game():
    os.system('cls')
    y_score=0
    ai_score=0
    bron=""
    while True:
        os.system('cls')
        print("WYNIK:")
        print(y_score,"-",ai_score)
        print("ZBROJOWNIA:")
        print("1-Kamień\n2-Papier\n3-Nożyce\n")
        choice=input("Wybierz swoją broń: ")
        if len(choice)==1 and choice.isdigit() and (choice=='1' or choice=='2' or choice=='3'):
            if choice=='1':
                bron="kamien"
            elif choice=='2':
                bron="papier"
            elif choice=='3':
                bron="nozyce"
            
            komputer=AI()
            print("Twoja broń:",bron)
            time.sleep(1)
            print("Wybor AI:",komputer)
            time.sleep(1)
            if bron==komputer:
                print("REMIS!")

            elif bron=="kamien":
                if komputer=="papier":
                    print("ojj nie udało się")
                    ai_score+=1
                elif komputer=="nozyce":
                    print("ZDOBYWASZ PUNKT!")
                    y_score+=1
            

            elif bron=="papier":
                if komputer=="nozyce":
                    print("ojj nie udało się")
                    ai_score+=1
                elif komputer=="kamien":
                    print("ZDOBYWASZ PUNKT!")
                    y_score+=1
        

            elif bron=="nozyce":
                if komputer=="kamien":
                    print("ojj nie udało się")
                    ai_score+=1
                elif komputer=="papier":
                    print("ZDOBYWASZ PUNKT!")
                    y_score+=1
            time.sleep(1)
            if y_score==3:
                print("WYGRAŁEŚ!!!")
                time.sleep(1)
                menu_interface()
                break
            if ai_score==3:
                print("PRZEGRAŁEŚ!")
                time.sleep(1)
                menu_interface()
                break
        else:
            print("błędny wybór")
            time.sleep(1)


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