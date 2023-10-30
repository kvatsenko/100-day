import random

all_cards=["2♠️", "2♣️", "2♦️", "2♥️", "3♠️", "3♣️", "3♦️", "3♥️", "4♠️", "4♣️", "4♦️", "4♥️", "5♠️", "5♣️", "5♦️",
            "5♥️", "6♠️", "6♣️", "6♦️", "6♥️", "7♠️", "7♣️", "7♦️", "7♥️", "8♠️", "8♣️", "8♦️", "8♥️", "9♠️", "9♣️",
              "9♦️", "9♥️", "10♠️", "10♣️", "10♦️", "10♥️", "J♠️", "J♣️", "J♦️", "J♥️", "Q♠️", "Q♣️", "Q♦️", "Q♥️",
                "K♠️", "K♣️", "K♦️", "K♥️", "A♠️", "A♣️", "A♦️", "A♥️"]

new_all_cards=["2♠️", "2♣️", "2♦️", "2♥️", "3♠️", "3♣️", "3♦️", "3♥️", "4♠️", "4♣️", "4♦️", "4♥️", "5♠️", "5♣️", "5♦️",
            "5♥️", "6♠️", "6♣️", "6♦️", "6♥️", "7♠️", "7♣️", "7♦️", "7♥️", "8♠️", "8♣️", "8♦️", "8♥️", "9♠️", "9♣️",
              "9♦️", "9♥️", "10♠️", "10♣️", "10♦️", "10♥️", "J♠️", "J♣️", "J♦️", "J♥️", "Q♠️", "Q♣️", "Q♦️", "Q♥️",
                "K♠️", "K♣️", "K♦️", "K♥️", "A♠️", "A♣️", "A♦️", "A♥️"]
cards_values={
    "2♠️": 2,
    "2♣️": 2,
    "2♦️": 2,
    "2♥️": 2,
    "3♠️": 3,
    "3♣️": 3,
    "3♦️": 3,
    "3♥️": 3,
    "4♠️": 4,
    "4♣️": 4,
    "4♦️": 4,
    "4♥️": 4,
    "5♠️": 5,
    "5♣️": 5,
    "5♦️": 5,
    "5♥️": 5,
    "6♠️": 6,
    "6♣️": 6,
    "6♦️": 6,
    "6♥️": 6,
    "7♠️": 7,
    "7♣️": 7,
    "7♦️": 7,
    "7♥️": 7,
    "8♠️": 8,
    "8♣️": 8,
    "8♦️": 8,
    "8♥️": 8,
    "9♠️": 9,
    "9♣️": 9,
    "9♦️": 9,
    "9♥️": 9,
    "10♠️": 10,
    "10♣️": 10,
    "10♦️": 10,
    "10♥️": 10,
    "J♠️": 10,
    "J♣️": 10,
    "J♦️": 10,
    "J♥️": 10,
    "Q♠️": 10,
    "Q♣️": 10,
    "Q♦️": 10,
    "Q♥️": 10,
    "K♠️": 10,
    "K♣️": 10,
    "K♦️": 10,
    "K♥️": 10,
    "A♠️": 11,
    "A♣️": 11,
    "A♦️": 11,
    "A♥️": 11
}

def get_card():
    global all_cards
    element = random.choice(all_cards)
    index = all_cards.index(element)
    all_cards = all_cards[:index] + all_cards[index+1 :]
    return element

computers_coice=[]
players_coice=[]
def random_card():
    for i in range(0, 2):
        card = get_card()
        players_coice.append(card)

    for i in range(0, 2):
        card = get_card()
        computers_coice.append(card)

random_card()

comp_score=cards_values[computers_coice[0]] + cards_values[computers_coice[1]]

def your_game_score():
    contin=True
    while contin:
        your_score = 0
        for card in players_coice:
            your_score += cards_values[card]
        print(f"computer's card is {computers_coice[1]}")
        print(f"{players_coice}, value: {your_score}")
        if your_score > 21:
            break
        question=input("do you want more cards? yes/no: ")
        if question == "yes":
            players_coice.append(get_card())

        elif question == "no":
            contin = False


    print(your_score)
    return your_score

def final():
    your_score = your_game_score()
    if 21 >= your_score > comp_score or comp_score > 21 >= your_score:
        print("you win!")
        print(f"computer's score was {comp_score}")
    elif 21 >= comp_score > your_score or your_score > 21 >= comp_score:
        print("you lose!")
        print(f"computer's score was {comp_score}")
    elif comp_score == your_score:
        print("draw")

final()

# while input("do you want to play again? yes/no: ") == "yes":
#     computers_coice.clear()
#     players_coice.clear()
#     for arr in all_cards:
#         new_all_cards.extend(arr)

#     all_cards = list(set(new_all_cards))
#     random_card()
#     comp_score=cards_values[computers_coice[0]] + cards_values[computers_coice[1]]
#     final()
