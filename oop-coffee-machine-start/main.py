from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_marker=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()

while True:
    options=menu.get_items()
    choice=input(f"what do you want to order? ({options}): ")
    if choice =="off":
        break
    elif choice =="report":
        coffe_marker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffe_marker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_marker.make_coffee(drink)


    
