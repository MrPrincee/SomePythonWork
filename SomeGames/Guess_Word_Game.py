import random


words = ['BANANA', 'APPLE', 'STRAWBERRY', 'WINE', 'CHEESE', 'PEACH']

guess_word = random.choice(words)
my_list = []
my_list2 = []
player1_score = 0
player2_score = 0
for i in guess_word:
    my_list.append(i)

print(my_list)


def play():
    i = 0
    global player1_score
    global player2_score
    while my_list != my_list2:
        player1 = input('P1-Guess the word: ')
        if player1 in my_list:
            while i < len(my_list):
                if my_list[i] == player1:
                    my_list.remove(player1)
                else:
                    i += 1
            round_score = 1 * guess_word.count(player1)
            player1_score += round_score
            print(my_list)
            print(f'P1 SCORE - {player1_score}')
            print(f'P2 SCORE - {player2_score}')
            i = 0
        elif player1 not in my_list:
            print('Wrong! Try again')
        player2 = input('P2-Guess the word: ')
        if player2 in my_list:
            while i < len(my_list):
                if my_list[i] == player2:
                    my_list.remove(player2)
                else:
                    i += 1
            print(my_list)
            round_score2 = 1 * guess_word.count(player2)
            player2_score += round_score2
            i = 0
            print(f'P1 SCORE - {player1_score}')
            print(f'P2 SCORE - {player2_score}')
        elif player2 not in my_list:
            print('Wrong! Try again')


play()


if player1_score > player2_score:
    print(f'Game over\n P1 Score - {player1_score}\n P2 Score - {player2_score}\n P1 WON!!')
elif player2_score > player1_score:
    print(f'Game over\n P1 Score - {player1_score}\n P2 Score - {player2_score}\n P1 WON!!')
elif player2_score == player1_score:
    print(f'Game over\n P1 Score - {player1_score}\n P2 Score - {player2_score}\n IT IS DRAW!!')