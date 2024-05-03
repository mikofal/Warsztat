import numpy as np
import time

array=np.empty((3,3),dtype='U1')

while True:
    print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
    print("-----------------------------------------------------------------------------------------------------")
    player1=input("Ruch gracza 1\n")
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
    else:
        print("error")
    
    print(array)
    time.sleep(1)
    if (array[0,0]=="X" and array[0,1]=="X" and array[0,2]=="X") or (array[1,0]=="X" and array[1,1]=="X" and array[1,2]=="X") or (array[2,0]=="X" and array[2,1]=="X" and array[2,2]=="X") or (array[0,0]=="X" and array[1,0]=="X" and array[2,0]=="X") or (array[0,1]=="X" and array[1,1]=="X" and array[2,1]=="X") or (array[0,2]=="X" and array[1,2]=="X" and array[2,2]=="X") or (array[0,0]=="X" and array[1,1]=="X" and array[2,2]=="X") or (array[0,2]=="X" and array[1,1]=="X" and array[2,0]=="X"):
        print("GRACZ 1 WYGRAŁ!")
        break

    player2=input("Ruch gracza 2\n")
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
    else:
        print("error")
    
    if (array[0,0]=="O" and array[0,1]=="O" and array[0,2]=="O") or (array[1,0]=="O" and array[1,1]=="O" and array[1,2]=="O") or (array[2,0]=="O" and array[2,1]=="O" and array[2,2]=="O") or (array[0,0]=="O" and array[1,0]=="O" and array[2,0]=="O") or (array[0,1]=="O" and array[1,1]=="O" and array[2,1]=="O") or (array[0,2]=="O" and array[1,2]=="O" and array[2,2]=="O") or (array[0,0]=="O" and array[1,1]=="O" and array[2,2]=="O") or (array[0,2]=="O" and array[1,1]=="O" and array[2,0]=="O"):
        print("GRACZ 2 WYGRAŁ!")
        break
    print(array,"\n")
    time.sleep(1)

    
