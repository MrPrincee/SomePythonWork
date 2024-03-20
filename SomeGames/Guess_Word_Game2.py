import random


world_value = ['naruto', 'luffy']
word_hint = ['rasengan', 'Gum-Gum']


def play():
    guess_list = []
    word_list = []
    guess_word = random.choice(world_value)
    guess_word_index = world_value.index(guess_word)
    for k in guess_word:
        word_list.append(k)
    for _ in guess_word:
        guess_list.append('*')
    guess_string = '  '.join(guess_list)
    print(guess_string)
    print(f'Hint: {word_hint[guess_word_index]}')
    while '*' in guess_list:
        guess_string = '  '.join(guess_list)
        print(guess_string)
        guess = input('Guess: ')
        if guess in guess_word:
            guess_quantity = guess_word.count(guess)
            if guess_quantity == 1:
                guess_index = guess_word.index(guess)
                guess_list[guess_index] = guess
                continue
            elif guess_quantity > 1:
                i = 0
                while i < len(word_list):
                    if word_list[i] == guess:
                        guess_list[i] = guess
                        i += 1
                        continue
                    else:
                        i += 1
                        continue
                continue

        else:
            print('Input is not in word!')
            continue
    else:
        print('-----------')
        print(guess_word)
        print('-----------')
        print('You Won!')
        print('-----------')


play()