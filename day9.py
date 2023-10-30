# student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74,}

# student_grades = {}

# for key in student_scores:
#     if int(student_scores[key])>=91:
#         student_scores[key] = "Outstanding"
#     elif 81 <= int(student_scores[key]) <= 90:
#         student_scores[key] = "Exceedes Expectations"
#     elif 71 <= int(student_scores[key]) <= 80:
#         student_scores[key] = "Acceptable" 
#     elif int(student_scores[key])<=70:
#         student_scores[key] = "Fail" 

# for key in student_scores:
#     print(key)
#     print(student_scores[key])



# world = [
# {
#     'country': 'France',
#     'visitis': 12,
#     'citys': ['Paris', 'Lille']
# },
# ]
# add_new_country = ("Ukraine", 100, ['Kiev', 'Lviv'])
# def anc():
#     adnc={}
#     adnc['country'] = add_new_country[0]
#     adnc['visitis'] = add_new_country[1]
#     adnc['citys'] = add_new_country[2]
#     world.append(adnc)
# anc()
# print(world)




auct={}
def auction():
    a=input("Welcome to the secret auction program!\nWhat is your name?: ")
    b=int(input("What's your bid?: "))
    auct[a] = b

auction()
print(auct)

while input("Are there any athers players? yes/no: ") != "no":
    auction()
    print(auct)

else:
    pass

# auct={"w": 12, "e": 113, "f": 10,}

def winer():
    winner={}
    list=0
    for player in auct:
        if auct[player] >= list:
            list = auct[player]
            winner['player'] = player
            winner['bid'] = auct[player]

        else:
            pass

    print(f"The winer is {winner['player']}, with a bid {winner['bid']}")

winer()


