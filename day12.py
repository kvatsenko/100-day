numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,]
import random
num=random.choice(numbers)


def asc():
    complexity=input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard: ")
    if complexity =="easy":
        lifes = 15
    elif complexity =="hard":
        lifes = 5

    num=random.choice(numbers)
    while lifes !=0:
        variant=int(input("your guess: "))

        if int(variant) == num:
            print("you win!")
            break

        elif int(variant) > num:
            print("lower!")
            lifes=lifes-1
            print(f"your num of lifes: {lifes}")

        elif int(variant) < num:
            print("higer!")
            lifes=lifes-1
            print(f"your num of lifes: {lifes}")
asc()

while input("do you want play again?: ") != "no":
    asc()
# incorect=7
# life=6
# while life != 0:
#     variant=input("your guess: ").lower()


#     # Clearing the Screen
#     os.system('cls')

#     for j in range(len(list[0])):
#         if word[j] == variant:
#             display[j] = variant
    
#     if "_" not in display:
        
#         print("you win!")
#         life=0
        
#     if variant not in list[0]:
#         life = life-1
#         print(incorect_pictures[life])
#         print(f"your lifes equals {life}")    

#     print(display)