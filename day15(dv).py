import random

database=[
    
{
    "id":0,
    "sex":"male",
    "orientation":"getero",
    "age":18,
    "name":"Kirill",
    "photo":"image234",
    "likes":[],
    "dislikes":[],
},
{
     "id":1,
    "sex":"female",
    "orientation":"getero",
    "age":18,
    "name":"Anya",
    "photo":"image345",
    "likes":[],
    "dislikes":[],
},
{
     "id":2,
    "sex":"male",
    "orientation":"getero",
    "age":20,
    "name":"David",
    "photo":"image789",
    "likes":[],
    "dislikes":[],
},
{
     "id":3,
    "sex":"female",
    "orientation":"getero",
    "age":16,
    "name":"Sveta",
    "photo":"image543",
    "likes":[],
    "dislikes":[],
},
{
     "id":4,
    "sex":"male",
    "orientation":"getero",
    "age":18,
    "name":"Olexiy",
    "photo":"image725",
    "likes":[],
    "dislikes":[],
},
{
     "id":5,
    "sex":"female",
    "orientation":"getero",
    "age":17,
    "name":"Masha",
    "photo":"image612",
    "likes":[],
    "dislikes":[],
},
{
    "id":6,
    "sex":"female",
    "orientation":"bi",
    "age":17,
    "name":"Astra",
    "photo":"image614",
    "likes":[],
    "dislikes":[7],
},

]

def registration():
    list=["male","getero",18,"kirill","image777"]
    ancet={}
    # sex=input("hello it is DV, what is your sex? (male/female): ")
    # list.append(sex)
    # ancet["sex"]=sex
    # orientation=input("what is your orientation? (bi/getero/gomo): ")
    # list.append(orientation)
    # ancet["orientation"]=orientation
    # age=int(input("how old are you?: "))
    # list.append(age)
    # ancet["age"]=age
    # ancet["name"]=input("what is your name?: ")
    # ancet["photo"]=input("plese upload some photo: ")
    # ancets.append(ancet)
    return list
reg = registration()

person = {
    "id":len(database),
    "sex":reg[0],
    "orientation":reg[1],
    "age":reg[2],
    "name":reg[3],
    "photo":reg[4],
    "likes":[],
    "dislikes":[],
}


def get_new_choice(person):
    global database
    # filter by orientation
    # bi- *
    # gay-gay/bi + man-man
    # lesb-lesb/bi + girl-girl

    # get/get/bi + girl-man/man-girl
    allowed_choice = [item for item in database if 
                person["orientation"] == "bi"
                or (person["orientation"] == "gomo" and (item["orientation"] == "gomo" or item["orientation"] == "bi") and item["sex"]== person["sex"])
                or (person["orientation"] == "getero" and (item["orientation"] == "getero" or item["orientation"] == "bi") and item["sex"]!= person["sex"])]

    allowed_choice = [item for item in allowed_choice if
                  person["orientation"] == "gomo"
                  or (person["orientation"] == "getero" and person["sex"] == "male"  and item["age"]< person["age"] )
                  or (person["orientation"] == "getero" and person["sex"] == "female"  and item["age"]> person["age"] )
                  ]
    allowed_choice = [item for item in allowed_choice if
                    item["id"] not in person["likes"] and item["id"] not in person["dislikes"] 
                    and person["id"] not in item["dislikes"] 
                  ]
    return allowed_choice

contin=True

while True:
    
    selector = get_new_choice(person)
    if len(selector) == 0:
        print("sorry, there is all users for today)")
        break
    else:
        index = random.randrange(len(selector))
        print(f"{selector[index]}")
        ans=input("how do you like this(1/0): ")
        if(ans == "1"):
            person["likes"].append(selector[index]['id'])
            #print(f"{person}")
        elif(ans == "0"):
            person["dislikes"].append(selector[index]['id'])
            #print(f"{person}")
        else:
            break
            
print(f"{person}")   

