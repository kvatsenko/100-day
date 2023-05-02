import random
# randomIntegeter = random. randint (1, 10)
# print (randomIntegeter)
# randomFloat = random. random () * 5
# print (randomFloat)
# love_score = random. randint (1, 100)
# print (f"Your love score is {love_score}%")


# a = (input("what do you chouse Head or Tail? ")).lower()
# b = random.randint (1, 2)
# if a == "head":
#     s=1
#     if s == b:
#         print("you win!")
#     else:
#         print("you lose")
# elif a == "tail":
#     s=2
#     if s == b:
#         print("you win!")
#     else:
#         print("you lose")
# else:
#     print("idk")
# print(b)

# str_inp = input("enter the names splits the coma: ")
# op = str_inp.split(",")
# b = random.randint (1, len(op))
# print(op[b-1])

row1=[".",".","."]
row2=[".",".","."]
row3=[".",".","."]
map=[row1,row2,row3]


x=input("enter your coordinates: ")


map[int(x[1])-1][int(x[0])-1]='x'

print(f"{row1}\n{row2}\n{row3}")




# a=int(input(" welcome to the game! \n1 - paper \n2 - rock \n3 - scissors \n Your variant: "))
# b = random.randint (1,3)
# if a==1:
#     if b == 1:
#         print(b)
#         print("draw!")
#     elif b==2:
#         print(b)
#         print("you win!")
#     else:
#         print(b)
#         print("you lose!")
# elif a ==2:
#     if b==2:
#         print(b)
#         print("draw!")
#     elif b==3:
#         print(b)
#         print("you win!")
#     else:
#         print(b)
#         print("you lose!")
# elif a==3:
#     if b==3:
#         print(b)
#         print("draw!")
#     elif b==1:
#         print(b)
#         print("you win!")
#     else:
#         print(b)
#         print("you lose!")
# else:
#     print("idk")

    

