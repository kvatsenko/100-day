import random


#random num
# def random_v():
#     list_=["kristiano ronaldo","nikita","andrey","maki","kostya"]
#     variant=random.choice(list_)

#     return variant




#dictionari
variant = [
{
    "name": "kristiano ronaldo",
    "discription": "just footboler",
    "score": 200000
    }, 
{
    "name": "nikita",
    "discription": "classmate",
    "score": 3000
    },
{
    "name": "andrey",
    "discription": "friend",
    "score": 120
    },
{
    "name": "maki",
    "discription": "i",
    "score": 1200
    },
{
    "name": "kostya",
    "discription": "groupmate",
    "score": 400
    },
{
    "name": "anya",
    "discription": "future wife",
    "score": 1300
    }
]

#cicle for variant
# variants=[]
# for i in range(2):
#         card = random_v()
#         variants.append(card)
# print(variants)

#function with dictionary


# contin=True
# while contin:


#printble format
score = 0
def printble(account):
    acc_name_a= account["name"]
    acc_discription= account["discription"]
    return f"{acc_name_a}, {acc_discription}, from Ukraine"

def check(guess, folowers_a, folowers_b):
        if folowers_a > folowers_b:
            return guess=="a"
        else:
            return guess=="b"
game_continue=True
account_b=random.choice(variant)
while game_continue:
     
    #random acc for game
    account_a=account_b
    account_b=random.choice(variant)

    if account_a == account_b:
        account_b=random.choice(variant)

    print(f"compare A: {printble(account_a)}")
    print("( VS )")
    print(f"compare B: {printble(account_b)}")

    #check if user corect
    acc_score_a= account_a["score"]
    acc_score_b= account_b["score"]

    guess=input("who has more folowers? a/b: ")
    corect=check(guess, acc_score_a, acc_score_b)
    
    if corect:
        score+=1
        print(f"you are right! your score is {score}")
    else:
        print(f"that's wrong. your score is {score}")
        game_continue=False

     



    # variants=[]
    # for i in range(2):
    #     card = random_v()

    #     variants.append(card)
        


    # print(variants)

    # score=0
    # choise=input(f"which have more folowers? 'a' if {variants[0]} or 'b' if {variants[1]}: ")


    # if choise=="a":
    #     if variant[variants[0]] > variant[variants[1]]:
    #         score=+1
    #         print(score)
    #     elif variant[variants[0]] < variant[variants[1]]:
    #         print("you lose.")
    #         contin=False
    # elif choise=="b":
    #     if variant[variants[0]] > variant[variants[1]]:
    #         print("you lose.")
    #         contin=False
    #     elif variant[variants[0]] < variant[variants[1]]:
    #         score=+1
    #         print(score)
            
    