import random


def game():
    chance = 0
    print(f'-----------------\n'
          f'Game difficulty:\n'
          f'1:Easy:30 try\n'
          f'2:Medium:20 try\n'
          f'3:Hard:10 try\n'
          f'-----------------')
    while True:
        difficulty = int(input('Choose Game difficulty:'))
        if difficulty == 1:
            chance = 30
            break
        elif difficulty == 2:
            chance = 20
            break
        elif difficulty == 3:
            chance = 10
            break
        else:
            print(f'-----------------\n'
                  f'Wrong Difficulty!\n'
                  f'Try Again!\n'
                  f'-----------------')
            continue

    cows = 0
    bulls = 0
    secret_num = random.randrange(1000, 9999)
    secret_num = str(secret_num)
    secret_num_list = []
    guess_list = []
    print(f'-----------------\n'
          f'You are given secret code try to guess it\n'
          f'Cows represent correct number at correct place\n'
          f'Bulls represent correct number at incorrect place\n'
          f'-----------------')
    while chance > 0:
        guess = input('Guess the number(Number should be between 1000-9999):')

        if guess != secret_num:
            for i in str(secret_num):
                secret_num_list.append(i)
            for j in guess:
                guess_list.append(j)
            for k, m in zip(guess_list, secret_num_list):
                if k == m and k in guess_list[guess_list.index(k):]:
                    cows += 1
                    bulls = bulls - 1
                elif k == m and k not in guess_list[guess_list.index(k):]:
                    cows += 1
                elif k != m and k in secret_num_list:
                    bulls += 1

                if bulls < 0:
                    bulls = 0
                elif bulls > 0 or bulls == 0:
                    pass

            print(f'Cows:{cows} Bulls:{bulls}')
            bulls = 0
            cows = 0
            guess_list = []
            chance -= 1
            print(f'-----------------\n'
                  f'Chances left:{chance}\n'
                  f'-----------------')
            continue
        else:
            print(f'You are correct Secret number was:{secret_num}')
            break
    print(f'-----------------\n'
          f'You Lost!\n'
          f'Try Again!\n'
          f'Secret code was: {secret_num}\n'
          f'-----------------')


game()