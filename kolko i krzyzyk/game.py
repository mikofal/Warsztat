import numpy as np
import time
import os

def start_game():
    array=np.empty((3,3),dtype='U1')
    print("Wciśnij odpowiedni klawisz: \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
    ruchy=[]
    counter=0
    while True:
        #print(array,"\n")
        while True:
            counter+=1
            player1=input("Ruch gracza 1: ")
            if player1!='0' and len(player1)==1 and player1.isdigit() and player1 not in ruchy:
                break
            else:
                continue
        ruchy.append(player1)
        if player1 =='1' and array[0,0]=="":
            array[0,0]="X"
        elif player1 =='2' and array[0,1]=="":
            array[0,1]="X"
        elif player1 =='3' and array[0,2]=="":
            array[0,2]="X"
        elif player1 =='4' and array[1,0]=="":
            array[1,0]="X"
        elif player1 =='5' and array[1,1]=="":
            array[1,1]="X"
        elif player1 =='6' and array[1,2]=="":
            array[1,2]="X"
        elif player1 =='7' and array[2,0]=="":
            array[2,0]="X"
        elif player1 =='8' and array[2,1]=="":
            array[2,1]="X"
        elif player1 =='9' and array[2,2]=="":
            array[2,2]="X"
        
        if (array[0,0]=="X" and array[0,1]=="X" and array[0,2]=="X") or (array[1,0]=="X" and array[1,1]=="X" and array[1,2]=="X") or (array[2,0]=="X" and array[2,1]=="X" and array[2,2]=="X") or (array[0,0]=="X" and array[1,0]=="X" and array[2,0]=="X") or (array[0,1]=="X" and array[1,1]=="X" and array[2,1]=="X") or (array[0,2]=="X" and array[1,2]=="X" and array[2,2]=="X") or (array[0,0]=="X" and array[1,1]=="X" and array[2,2]=="X") or (array[0,2]=="X" and array[1,1]=="X" and array[2,0]=="X"):
            os.system('cls')
            print(array,"\n")
            print("GRACZ 1 WYGRAŁ!")
            menu_interface()
            break
        os.system('cls')

        print("Wciśnij odpowiedni klawisz: \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
        print(array,"\n")
        if counter==5:
            print("REMIS")
            menu_interface()
            break
        while True:

            player2=input("Ruch gracza 2: ")
            if player2!='0' and len(player2)==1 and player2.isdigit() and player2 not in ruchy:
                break
            else:
                continue
        ruchy.append(player2)
        if player2 =='1' and array[0,0]=="":
            array[0,0]="O"
        elif player2 =='2' and array[0,1]=="":
            array[0,1]="O"
        elif player2 =='3' and array[0,2]=="":
            array[0,2]="O"
        elif player2 =='4' and array[1,0]=="":
            array[1,0]="O"
        elif player2 =='5' and array[1,1]=="":
            array[1,1]="O"
        elif player2 =='6' and array[1,2]=="":
            array[1,2]="O"
        elif player2 =='7' and array[2,0]=="":
            array[2,0]="O"
        elif player2 =='8' and array[2,1]=="":
            array[2,1]="O"
        elif player2 =='9' and array[2,2]=="":
            array[2,2]="O"
            
        
        if (array[0,0]=="O" and array[0,1]=="O" and array[0,2]=="O") or (array[1,0]=="O" and array[1,1]=="O" and array[1,2]=="O") or (array[2,0]=="O" and array[2,1]=="O" and array[2,2]=="O") or (array[0,0]=="O" and array[1,0]=="O" and array[2,0]=="O") or (array[0,1]=="O" and array[1,1]=="O" and array[2,1]=="O") or (array[0,2]=="O" and array[1,2]=="O" and array[2,2]=="O") or (array[0,0]=="O" and array[1,1]=="O" and array[2,2]=="O") or (array[0,2]=="O" and array[1,1]=="O" and array[2,0]=="O"):
            os.system('cls')
            print(array)
            print("GRACZ 2 WYGRAŁ!")
            menu_interface()
            break
        os.system('cls')
        print("Wciśnij odpowiedni klawisz: \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
        print(array,"\n")

print("WITAJ W GRZE!")
def menu_interface():
    while True:
        menu=input("1-Zagraj\n2-Wyjdź z gry\n")
        if menu=='1':
            os.system("cls")
            start_game()
            break
        elif menu=='2':
            exit(1)
        else:
            print("błąd")
            continue

menu_interface()      

    
