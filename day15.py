all_milk = 200
all_coffee = 100
all_watter = 300

all_money=0

set=[
{
    "name": "capuchino",
    "money": 30,
    "milk": 30,
    "coffee": 30,
    "watter": 10
},
{   
    "name": "expresso",
    "money": 25,
    "milk": 0,
    "coffee": 20,
    "watter": 40

},
{   
    "name": "latte",
    "money": 40,
    "milk": 70,
    "coffee": 20,
    "watter": 10

}
]
def money(variant):
    ten_coin=int(input("how many coin (0.10)? "))
    haf_coin=int(input("how many coin (0.50)? "))
    One_coin=int(input("how many coin (1.0)? "))
    Two_coin=int(input("how many coin (2.0)? "))
    Five_coin=int(input("how many coin (5.0)? "))
    Ten_coin=int(input("how many coin (10.0)? "))

    summ=float(ten_coin*0.10+haf_coin*0.50+One_coin+Two_coin*2+Five_coin*5+Ten_coin*10)
    if summ < set[variant]["money"]:
        asc=input("there is not enough money. do you want to add money?(no/yes): ")
        if asc=="yes":
            money()
        elif asc=="no":
            print(f"there is your money: {summ}$")
    elif summ >= set[variant]["money"]:
        odd_money = summ - set[variant]["money"]

        print(f"there is your odd money: {odd_money}")
        new_money=all_money + set[variant]["money"]
    return new_money

def counting(money,milk,coffee,watter):
    global all_money
    global all_milk
    global all_coffee
    global all_watter
    all_money=money
    all_milk-=milk
    all_coffee-=coffee
    all_watter-=watter



contin=True
while contin:

    asc=input("what do you whant to buy? (expresso/capuchino/latte): ")

    if asc == "report":
        print(f"Watter: {all_watter}ml\nMilk: {all_milk}ml\nCoffee: {all_coffee}g\n\nMoney: {all_money}$")
    elif asc == "capuchino":
        n=0
        if all_milk<set[n]["milk"] or all_coffee<set[n]["coffee"] or all_watter<set[n]["watter"]:
            print("sorry, coffee mashine does't have enough of some ingredients...\nwould you change your reqest?")
        elif all_milk>=set[n]["milk"] and all_coffee>=set[n]["coffee"] and all_watter>=set[n]["watter"]:
            counting(money(n),set[n]["milk"],set[n]["coffee"],set[n]["watter"])
    elif asc == "expresso":
        n=1
        if all_milk<set[n]["milk"] or all_coffee<set[n]["coffee"] or all_watter<set[n]["watter"]:
            print("sorry, coffee mashine does't have enough of some ingredients...\nwould you change your reqest?")
        elif all_milk>=set[n]["milk"] and all_coffee>=set[n]["coffee"] and all_watter>=set[n]["watter"]:
            counting(money(n),set[n]["milk"],set[n]["coffee"],set[n]["watter"])
    elif asc == "latte":
        n=2
        if all_milk<set[n]["milk"] or all_coffee<set[n]["coffee"] or all_watter<set[n]["watter"]:
            print("sorry, coffee mashine does't have enough of some ingredients...\nwould you change your reqest?")
        elif all_milk>=set[n]["milk"] and all_coffee>=set[n]["coffee"] and all_watter>=set[n]["watter"]:
            counting(money(n),set[n]["milk"],set[n]["coffee"],set[n]["watter"])
    elif asc == "no":
        contin=False
    

#report
#check resursers
#procerss coins
#check transaction sucsesful?