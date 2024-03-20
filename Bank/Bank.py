import sqlite3

conn = sqlite3.connect("Bank.sqlite")

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE users
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(50),
# surname VARCHAR(100),
# password VARCHAR(50),
# loan FLOAT,
# mail VARCHAR(50),
# money FLOAT);''')


# Name
cursor = cursor.execute('SELECT name FROM users')
length = len(cursor.fetchall())

cursor2 = cursor.execute('SELECT name FROM users')
all_title = cursor2.fetchmany(length)

title_list = []

for i in all_title:
    content = str(i)
    title_list.append(content)

# Password
password_cursor = cursor.execute('SELECT password FROM users')
password_length = len(password_cursor.fetchall())

password_cursor2 = cursor.execute('SELECT password FROM users')
all_password = password_cursor2.fetchmany(password_length)

password_list = []

for j in all_password:
    password = str(j)
    password_list.append(password)

logged_acc = []
account_info = []

# Money
money_cursor = cursor.execute('SELECT money FROM users')
money_length = len(money_cursor.fetchall())

money_cursor2 = cursor.execute('SELECT money FROM users')
all_money = money_cursor2.fetchmany(money_length)

money_list = []

for k in all_money:
    money = str(k)
    money_list.append(money)

all_money_list = []

for f in range(len(money_list)):
    selected_value = money_list[f]
    sliced_value = selected_value[1:(len(selected_value)-2)]
    if sliced_value == 'None':
        sliced_value = 0
        all_money_list.append(sliced_value)
    else:
        all_money_list.append(sliced_value)


# Loan
loan_cursor = cursor.execute('SELECT loan FROM users')
loan_length = len(loan_cursor.fetchall())

loan_cursor2 = cursor.execute('SELECT loan FROM users')
all_loan = loan_cursor2.fetchmany(loan_length)

loan_list = []


for m in all_loan:
    loan = str(m)
    loan_list.append(loan)

all_loan_list = []

for q in range(len(loan_list)):
    selected_value2 = loan_list[q]
    sliced_value2 = selected_value2[1:(len(selected_value2)-2)]
    if sliced_value2 == 'None':
        sliced_value2 = 0
        all_loan_list.append(sliced_value2)
    else:
        all_loan_list.append(sliced_value2)


class Bank:
    def register(self):
        print('------------------------')
        name = input("Enter Your name: ")
        surname = input('Enter your surname: ')
        password2 = input('Enter your Password:')
        mail = input('Enter your Mail: ')
        print('------------------------')
        while '@' not in mail:
            print('------------------------')
            print('Invalid Mail: ')
            print('------------------------')
            mail = input('Enter Your mail:')

        cursor.execute('INSERT INTO users(name,surname,password,mail) VALUES (?, ?, ?, ?)',
                       (name, surname, password2, mail))
        conn.commit()
        if True:
            print('------------------------')
            print('User Registered successfully')
            print('------------------------')
        conn.close()

    def login(self):
        global title_list
        global logged_acc
        global account_info

        while True:
            print('------------------------')
            login_name = input('Name:')
            password1 = input('Password:')
            print('------------------------')
            formatted_name = f"('{login_name}',)"
            formatted_password = f"('{password1}',)"
            if formatted_name in title_list:
                money_index = title_list.index(formatted_name)
                loan_index = title_list.index(formatted_name)
                if (formatted_password in password_list) and title_list.index(formatted_name) ==\
                        password_list.index(formatted_password):
                    logged_acc.append(formatted_name)
                    logged_acc.append(formatted_password)
                    logged_acc.append(all_money_list[money_index])

                    account_info.append(login_name)
                    account_info.append(password1)
                    account_info.append(all_money_list[money_index])
                    account_info.append((all_loan_list[loan_index]))
                    print('------------------------')
                    print('Succesfully logged in')
                    print('------------------------')

                    return True

                else:
                    print('Wrong Password')
            else:
                print('Wrong Login!')
                continue

    def main(self):
        global account_info
        global title_list
        global all_loan_list
        while True:
            print('------------------------')
            print(f'Choose Command:\n'
                  f'1:Account Info\n'
                  f'2:Withdraw\n'
                  f'3:Insert money\n'
                  f'4:Make Loan\n'
                  f'5: Log out')
            print('------------------------')
            choice2 = int(input('Choose Command: '))
            print('------------------------')
            if choice2 == 1:
                print(f'name: {account_info[0]}, password: {account_info[1]}, money: {account_info[2]},'
                      f' loan: {account_info[3]}')
                continue
            elif choice2 == 2:
                logged_user_index = title_list.index(logged_acc[0])
                logged_user_money = all_money_list[logged_user_index]
                logged_user_money = float(logged_user_money)
                withdraw_money = int(input('How much you want to withdraw?: '))
                withdraw_money = float(withdraw_money)
                if logged_user_money > 0 and logged_user_money >= withdraw_money:
                    new_balance1 = logged_user_money - withdraw_money
                    all_money_list[logged_user_index] = str(new_balance1)
                    account_info[2] = new_balance1
                    print('------------------------')
                    print(f'Withdraw successful!\n'
                          f'Your new balance is {new_balance1}')
                    print('------------------------')
                    conn4 = sqlite3.connect("Bank.sqlite")
                    cursor4 = conn4.cursor()
                    sql_query = f"UPDATE users SET money = {new_balance1} WHERE name = ('{account_info[0]}')"
                    cursor4.execute(sql_query)
                    conn4.commit()
                    conn4.close()
                    continue
                else:
                    print('------------------------')
                    print(f'Your Balance is not enough\n'
                          f'Your Balance is: {logged_user_money}')
                    print('------------------------')
                    continue
            elif choice2 == 3:
                logged_user_index = title_list.index(logged_acc[0])
                logged_user_money = all_money_list[logged_user_index]
                logged_user_money = float(logged_user_money)
                print('------------------------')
                insert_money = float(input('How much money do you want to insert?: '))
                print('------------------------')
                new_balance = logged_user_money + insert_money
                all_money_list[logged_user_index] = str(new_balance)
                account_info[2] = new_balance
                conn3 = sqlite3.connect("Bank.sqlite")
                cursor3 = conn3.cursor()
                sql_query = f"UPDATE users SET money = {new_balance} WHERE name = ('{account_info[0]}')"
                cursor3.execute(sql_query)
                conn3.commit()
                conn3.close()
                print('------------------------')
                print('Balance added Succesfully!')
                print('------------------------')
            elif choice2 == 4:
                while True:
                    try:
                        print(f'1:Take Loan\n'
                                f'2:Pay loan')
                        des = int(input('Choose:'))
                        if des == 1:
                            print('------------------------')
                            take_loan = float(input('How Much do you want to take?: '))
                            print('------------------------')
                            logged_user_index = title_list.index(logged_acc[0])
                            logged_user_money = all_money_list[logged_user_index]
                            logged_user_money = float(logged_user_money)
                            logged_user_loan = all_loan_list[logged_user_index]
                            new_loan = take_loan + float(logged_user_loan)
                            account_info[3] = new_loan
                            conn1 = sqlite3.connect("Bank.sqlite")
                            cursor1 = conn1.cursor()
                            sql_query = f"UPDATE users SET loan = {new_loan} WHERE name = ('{account_info[0]}')"
                            cursor1.execute(sql_query)
                            conn1.commit()
                            conn1.close()

                            new_balance1 = logged_user_money + take_loan
                            all_money_list[logged_user_index] = str(new_balance1)
                            account_info[2] = new_balance1
                            conn7 = sqlite3.connect("Bank.sqlite")
                            cursor7 = conn7.cursor()
                            sql_query = f"UPDATE users SET money = {new_balance1} WHERE name = ('{account_info[0]}')"
                            cursor7.execute(sql_query)
                            conn7.commit()
                            conn7.close()
                            print('------------------------')
                            print("You took loan succesfully")
                            print(f'Your loan is {account_info[3]}')
                            print('------------------------')
                            break

                        elif des == 2:
                            logged_user_index = title_list.index(logged_acc[0])
                            logged_user_loan = all_loan_list[logged_user_index]
                            logged_user_loan = float(logged_user_loan)
                            pay = float(input('How much do you want to pay?:'))
                            if logged_user_loan >= pay:
                                payed_loan = logged_user_loan - pay
                                conn8 = sqlite3.connect("Bank.sqlite")
                                cursor8 = conn8.cursor()
                                sql_query = f"UPDATE users SET loan = {payed_loan} WHERE name = ('{account_info[0]}')"
                                cursor8.execute(sql_query)
                                conn8.commit()
                                conn8.close()
                                account_info[3] = payed_loan
                                print('------------------------')
                                print("Loan payed succesfully")
                                print(f'Your loan is {account_info[3]}')
                                print('------------------------')
                                break
                            else:
                                print('------------------------')
                                print("You don't have that much loan!")
                                print(f'Your loan is {account_info[3]}')
                                print('------------------------')
                                continue

                        else:
                            print('------------------------')
                            print('Wrong command!')
                            print('------------------------')
                            continue
                    except ValueError:
                        print('------------------------')
                        print('!ValueError!\n'
                              'Only numbers Allowed!\n'
                              '!ValueError!')
                        print('------------------------')
                        continue

            elif choice2 == 5:
                print('Logged out')
                account_info = []
                return play(Bank)


def play(Bank):
    while True:
        print('------------------------')
        print(f'Welcome!\n'
              f'1:Log in\n'
              f'2:Register')
        print('------------------------')
        try:
            choice = int(input('Choose: '))
            if choice == 1:
                while True:
                    if Bank.login(0):
                            Bank.main(0)

                    else:
                        print('False')
            elif choice == 2:
                print('2')
                Bank.register(0)
            else:
                print('------------------------')
                print('Wrong command')
                print('------------------------')
                continue
        except ValueError:
            print('------------------------')
            print('!ValueError!\n'
                  'Only numbers Allowed!\n'
                  '!ValueError!')
            print('------------------------')
            print('You are Logged Off!')
            print('------------------------')


play(Bank)