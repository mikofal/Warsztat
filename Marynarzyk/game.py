import random
import time

print("Witaj w grze!")
def AI():
    reka=["papier","kamien","nozyce"]
    return random.choice(reka)

y_score=0
ai_score=0
bron=""
while True:
    print("--------------------------------------------------------------------------------------------------------")
    print("ZBROJOWNIA:")
    print("1-Kamień\n 2-Papier\n 3-Nożyce\n")
    choice=input("Wybierz swoją broń:\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if choice=='1':
        bron="kamien"
    elif choice=='2':
        bron="papier"
    elif choice=='3':
        bron="nozyce"
    else:
        print("Zły wybór")
    
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
    print("WYNIK:")
    print(y_score,"-",ai_score)
    time.sleep(1)
    if y_score==3:
        print("WYGRAŁEŚ!!!")
        break
    if ai_score==3:
        print("PRZEGRAŁEŚ!")
        break
