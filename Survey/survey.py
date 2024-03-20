import random
import csv

survey_questions = ['Who your target market is?', 'How you should price your products?', 'Why visitors leave your web?',
                    'What is stopping people from buying from you?', 'Who is best actor?', 'Your Favorite film?',
                    'Where are you from?', 'What is your name?', 'How old are you?']

file = open("survey.csv", "w", newline="\n", encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(["User", "Question", "Answer"])


def survey():
    quantity = 0
    all_questions = []
    user = input("Enter your name: ")
    while quantity < 5:
        questions = random.choice(survey_questions)
        if questions in all_questions:
            quantity += 0
            continue
        else:
            print(questions)
            answer = input('Your answer:')
            all_questions.append(questions)
            file.write(user+','+questions+','+answer+','+'\n')
            quantity += 1

        if quantity < 5:
            continue
        else:
            print('----------------------------------------------')
            print('Survey has ended, Thank you for your response!')
            print('----------------------------------------------')
            break


survey()