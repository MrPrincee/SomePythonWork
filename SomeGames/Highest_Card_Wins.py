import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Quinn', 'King', 'Ace']
p1_score = 0
p2_score = 0


def scores(x, y):
    global p1_score
    global p2_score
    if x > y:
        p1_score += 1
    elif x == y:
        p1_score += 1
        p2_score += 1
    else:
        p2_score += 1


def game():
    global cards
    global p1_score
    global p2_score
    while len(cards) > 1:
        input('P1: Hit to play')
        random_card = random.choice(cards)
        index1 = cards.index(random_card)
        cards.remove(random_card)
        input('P2: Hit to play')
        print("------------------")
        random_card2 = random.choice(cards)
        index2 = cards.index(random_card2)
        cards.remove(random_card2)
        print(f'P1:{random_card}\nP2:{random_card2}')
        print("------------------")
        scores(index1, index2)
        print(f'P1-Score:{p1_score}\nP2-Score:{p2_score}')
        print("------------------")
    if p1_score > p2_score:
        print('P1 is Winner!')
        print("------------------")
    elif p1_score == p2_score:
        print("It's A Draw!!!")
        print("------------------")

    else:
        print('P2 is Winner!')
        print("------------------")


game()