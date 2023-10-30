import os


import random
list=["cat","mous","bird","child","dog","fish","rabbit"]
random.shuffle(list)

incorect_pictures=["""
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========""",
"""
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
=========""",
"""
   +---+
   |   |
   0   |
  /|\  |
       |
       |
=========""",
"""
   +---+
   |   |
   0   |
  /|   |
       |
       |
=========""",
"""
   +---+
   |   |
   0   |
   |   |
       |
       |
=========""",
"""
   +---+
   |   |
   0   |
       |
       |
       |
=========""",
"""
   +---+
   |   |
       |
       |
       |
       |
========="""
]

display=[]
word=" ".join(list[0]).split()

for i in list[0]:
    display+="_"

print(display)

incorect=7
life=6
while life != 0:
    variant=input("your guess: ").lower()


    # Clearing the Screen
    os.system('cls')

    for j in range(len(list[0])):
        if word[j] == variant:
            display[j] = variant
    
    if "_" not in display:
        
        print("you win!")
        life=0
        
    if variant not in list[0]:
        life = life-1
        print(incorect_pictures[life])
        print(f"your lifes equals {life}")    

    print(display)














# word=''

# output=",".join(list[0])
# # # "c a t"


# # for i in range(0,len(list[0])):
# #     word+="_"

# split_word=output.split(",")
# print(word)

# # # input_array=[]
# output = "_"
# inp = input("What letter do you choose? :")
# for i in range(0,len(list[0])):
#     if list[i] == inp:
#         word[i] = list[i]
#         print(word)

# while "_" in output:
#     letter1=input("What letter do you choose? :")
#     input_array.append(letter1) 
#     output = ""
#     for i in range(0,len(split_word)):
#         if split_word[i] in input_array:
#             output = output + split_word[i] + " "
#         else:
            

#             output = output + "_" + " "

            
#     print (output)

# print ("You Win!")


# for i in range(0,len(list[0])):
#     word+="_ "


# print("Welcome to hang man!)")
# split_word2=word.split()


# for let in range(0,10):
    
#     letter1=input("What letter do you choose? :")
#     if letter1 == split_word[let]:
#         split_word2[let] = letter1
#         print("you choose corect letter!")
#         print(split_word2)
#     else:
#         print("you choose INCORECT letter!)")
#         print(split_word2)

# # # for let in range(0,len(split_word)):
# #     letter=input("What letter do you choose? :")
# #     if letter == split_word[let]:
# #         split_word2[let] = letter
# #         print("you choose corect letter!")
# #         print(split_word2)

logo="Hello, it's encoder & decoder!"


mass_3 = [[3,2,4],[5,3,3],[8,9,3]]
mass_5 = []
for arr in mass_3:
    mass_5.extend(arr)

mass_x = list(set(mass_5))
print(mass_x)