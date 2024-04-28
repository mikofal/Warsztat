import random

while True:

    def return_random_letter():
        letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','z')
        i=random.randint(0,len(letters)-1)
        return letters[i]

    def return_random_big_letter():
        big_letters=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','Y','Z')
        i=random.randint(0,len(big_letters)-1)
        return big_letters[i]

    def return_random_special_character():
        special_characters=('!','@','#','$','%','^','&','*')
        i=random.randint(0,len(special_characters)-1)
        return special_characters[i]


    def return_random_number():
        numbers=('1','2','3','4','5','6','7','8','9','0')
        i=random.randint(0,len(numbers)-1)
        return numbers[i]


    def return_random_index(length):
        return random.randint(0,length-1)

    length=int(input('Prosze podac dlugosc hasla '))

    if length < 8:
        print("HASLO NIE MOZE BYC KROTSZE NIZ 8 ZNAKOW!")
        exit(1)

    password = ''

    for i in range(length):
        password+=return_random_letter()
        
    password_list=list(password)

    security_level = 0

    if length<=10:
        security_level=2
    elif length>10 and length<15:
        security_level=3
    else:
        security_level=4

    for i in range(security_level):
        password_list[return_random_index(length)]=return_random_special_character()
        password_list[return_random_index(length)]=return_random_big_letter()
        password_list[return_random_index(length)]=return_random_number()

    modified_password = ''.join(password_list)

    print("Twoje haslo to: " + modified_password)
