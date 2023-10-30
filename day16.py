
# from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("black", "gray")
# timmy.forward(100)

# print(timmy)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
tabble = PrettyTable()
tabble.field_names = ["Pokemon Name", "Type"]
tabble.add_rows(
    [
        ["Pickachu", "Electric"],
        ["Scwirle", "Wather"],
        ["Charmander", "Fire"],
    ]
)
print(tabble)