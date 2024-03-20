import random


p1_total_score = 0
p2_total_score = 0


def visual(current_dice, current_score, total_score):
    if current_score == 0 and total_score == 0:
        print('-------------------')
        print(f'Dice Score:{current_dice}\n'
              f'You lost your progress!')
        print('-------------------')
    elif current_dice == 0 and current_score == 0:
        print('-------------------')
        print(f'You saved you score!\n'
              f'You total score is: {total_score}')
        print('-------------------')
    elif total_score == 0:
        print('-------------------')
        print(f'Dice Score:{current_dice}\n'
              f'Your current score:{current_score}')


def game():
    global p1_total_score
    global p2_total_score
    p1_score = 0
    p2_score = 0
    print('-------------------')
    end_point = int(input('Choose winning score: '))
    print('-------------------')

    while True:
        while True:
            print('-------------------')
            print(f'P1 plays\n'
                  f'1: Dice\n'
                  f'2: Pass&Save')
            print('-------------------')
            p1_choice = int(input('Choose: '))
            print('-------------------')
            if p1_choice == 1:
                p1_dice = random.randrange(1, 6)
                if p1_dice == 1:
                    p1_score = 0
                    visual(p1_dice, 0, 0)
                    break
                else:
                    p1_score = p1_score + p1_dice * 2
                    visual(p1_dice, p1_score, 0)
                    continue
            elif p1_choice == 2:
                p1_total_score += p1_score
                p1_score = 0
                visual(0, 0, p1_total_score)
                break
            else:
                print('-------------------')
                print(f'Wrong command!\n'
                      f'Choose 1 or 2')
                print('-------------------')

        while True:
            print('-------------------')
            print(f'P2 plays\n'
                  f'1: Dice\n'
                  f'2: Pass&Save')
            print('-------------------')
            p2_choice = int(input('Choose: '))
            print('-------------------')
            if p2_choice == 1:
                p2_dice = random.randrange(1, 6)
                if p2_dice == 1:
                    p2_score = 0
                    visual(p2_dice, 0, 0)
                    break
                else:
                    p2_score = p2_score + p2_dice * 2
                    visual(p2_dice, p2_score, 0)
            elif p2_choice == 2:
                p2_total_score += p2_score
                p2_score = 0
                visual(0, 0, p2_total_score)
                break
            else:
                print('-------------------')
                print(f'Wrong command!\n'
                      f'Choose 1 or 2')
                print('-------------------')
        if p1_total_score > end_point or p2_total_score > end_point:
            if p1_total_score > p2_total_score:
                print('-------------------')
                print('Game Over!')
                print('-------------------')
                print(f'P1 total score:{p1_total_score}\n'
                      f'P2 total score:{p2_total_score}\n')
                print('-------------------')
                print('P1 Won!')
                print('-------------------')
            elif p1_total_score < p2_total_score:
                print('-------------------')
                print('Game Over!')
                print('-------------------')
                print(f'P1 total score:{p1_total_score}\n'
                      f'P2 total score:{p2_total_score}\n')
                print('-------------------')
                print('P2 Won!')
                print('-------------------')
            elif p1_total_score == p2_total_score:
                print('-------------------')
                print('Game Over!')
                print('-------------------')
                print(f'P1 total score:{p1_total_score}\n'
                      f'P2 total score:{p2_total_score}\n')
                print('-------------------')
                print("It's a Draw!")
                print('-------------------')
            break
        else:
            continue


game()