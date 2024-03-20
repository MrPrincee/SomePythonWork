empty = '-'
list1 = [empty, empty, empty]
list2 = [empty, empty, empty]
list3 = [empty, empty, empty]
main_list = [empty, empty, empty]


player1 = 'X'
player2 = 'O'
player1_score = 0
player2_score = 0
f = int(input('How many round do you want to play?:'))
i = 0


def list_chooser(x):
    if x == 1:
        return list1
    elif x == 2:
        return list2
    elif x == 3:
        return list3


def visual():
    print(f'|{list1[0]}| |{list1[1]}| |{list1[2]}|')
    print(f'|{list2[0]}| |{list2[1]}| |{list2[2]}|')
    print(f'|{list3[0]}| |{list3[1]}| |{list3[2]}|')


def player2_win():
    if (list1[0] == player2 and list1[1] == player2) and list1[2] == player2:
        return True

    elif (list2[0] == player2 and list2[1] == player2) and list2[2] == player2:
        return True

    elif (list3[0] == player2 and list3[1] == player2) and list3[2] == player2:
        return True

    elif (list1[0] == player2 and list2[0] == player2) and list3[0] == player2:
        return True

    elif (list1[1] == player2 and list2[1] == player2) and list3[1] == player2:
        return True

    elif (list1[2] == player2 and list2[2] == player2) and list3[2] == player2:
        return True

    elif (list1[0] == player2 and list2[1] == player2) and list3[2] == player2:
        return True

    elif (list1[2] == player2 and list2[1] == player2) and list3[0] == player2:
        return True
    else:
        return False


def game():
    global list1
    global list2
    global list3
    global main_list
    global f
    global player1_score
    global player2_score
    global i
    global empty
    global player1
    global player2
    visual()
    while True:

        if (empty not in list1) and (empty not in list2) and (empty not in list3):
            print('-----------------')
            print("It's A draw!")
            print('-----------------')
            list1 = [empty, empty, empty]
            list2 = [empty, empty, empty]
            list3 = [empty, empty, empty]
            i += 1
            pass
        elif i < f:
            pass
        elif i == f:
            print("---------------")
            print('Game Over!')
            print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
            if player1_score > player2_score:
                print("---------------")
                print('Player1 Won!')
                print("---------------")
                break
            elif player1_score < player2_score:
                print("---------------")
                print('Player2 Won!')
                print("---------------")
                break
            else:
                print("---------------")
                print("It's a Draw!")
                print("---------------")
                break
        player1_row = int(input('Which row:'))
        player1_place = int(input('Which place:'))
        if list_chooser(player1_row)[player1_place-1] == player1 or list_chooser(player1_row)[player1_place - 1] == \
                player2:
            print('-----------------')
            print('Already placed Choose different one!')
            print('-----------------')
            game()
        else:
            list_chooser(player1_row)[player1_place - 1] = player1
        visual()

        if (list1[0] == player1 and list1[1] == player1) and list1[2] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        elif (list2[0] == player1 and list2[1] == player1) and list2[2] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        elif (list3[0] == player1 and list3[1] == player1) and list3[2] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        elif (list1[1] == player1 and list2[1] == player1) and list3[1] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break

        elif (list1[0] == player1 and list2[0] == player1) and list3[0] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break

        elif (list1[2] == player1 and list2[2] == player1) and list3[2] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        elif (list1[0] == player1 and list2[1] == player1) and list3[2] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        elif (list1[2] == player1 and list2[1] == player1) and list3[0] == player1:
            print(f'Round over!!\nPlayer 1 Win')
            if i < f:
                i += 1
                player1_score += 1
                print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                list1 = [empty, empty, empty]
                list2 = [empty, empty, empty]
                list3 = [empty, empty, empty]
                pass
            else:
                if player1_score > player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player1 Won')
                    break
                elif player1_score < player2_score:
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    print('Player2 Won')
                    break
                else:
                    print("It's a Draw!!")
                    break
        else:
            while True:
                if (empty not in list1) and (empty not in list2) and (empty not in list3):
                    break
                else:
                    pass
                player2_row = int(input('Which row:'))
                player2_place = int(input('Which place:'))
                if list_chooser(player2_row)[player2_place - 1] == player2 or list_chooser(player2_row)[player2_place-1] == player1:
                    print('-----------------')
                    print('Already placed Choose different one!')
                    print('-----------------')
                    visual()
                    continue
                else:
                    list_chooser(player2_row)[player2_place - 1] = player2
                    visual()
                    break
            player2_win()
            if player2_win() == True:
                print(f'Round over!!\nPlayer 2 Win')
                if i < f:
                    i += 1
                    player2_score += 1
                    print(f'Player1 Score:{player1_score}\nPlayer2 Score:{player2_score}')
                    list1 = [empty, empty, empty]
                    list2 = [empty, empty, empty]
                    list3 = [empty, empty, empty]
                    pass
                else:
                    return game()
            else:
                continue


game()