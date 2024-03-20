import sqlite3
import requests
import json
import random

user_id_list = []
name_list = []
surname_list = []
salary_list = []
rank_list = []
mail_list = []

conn = sqlite3.connect('Employee.sqlite')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE employees
# (id INTEGER,
# name VARCHAR(50),
# surname VARCHAR(100),
# mail VARCHAR(50),
# rank INTEGER,
# salary FLOAT);''')


# გამოყენებულია რენდომ იუსერების API : https://dummyapis.com/dummy/employee

# url = "https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001"
# req = requests.get(url)
# req1 = json.loads(req.text)

# for i in req1:
#     user_id_list.append(i["id"])
#     name_list.append(i["firstName"])
#     surname_list.append(i["lastName"])
#     mail_list.append(i["email"])
#     salary_list.append(i["salary"])
#     rank_list.append(random.randrange(1, 9))


# for j in user_id_list:
#
#     j_index = user_id_list.index(j)
#     cursor.execute('INSERT INTO employees(id,name,surname,mail,rank,salary) VALUES (?,?, ?, ?, ?, ?)',
#                    (user_id_list[j_index], name_list[j_index], surname_list[j_index],
#                     mail_list[j_index], rank_list[j_index],
#                     salary_list[j_index]))
#     conn.commit()


def delete_employee(user_id):
    conn4 = sqlite3.connect('Employee.sqlite')

    cursor4 = conn4.cursor()

    cursor4.execute(f"DELETE FROM employees WHERE id = {user_id}")

    conn4.commit()
    conn4.close()


def all_info(value):
    conn2 = sqlite3.connect('Employee.sqlite')
    cursor2 = conn2.cursor()
    cursor2.execute(f"SELECT {value} FROM employees")
    record = cursor2.fetchall()
    list_for_info = []
    for f in record:
        current_value = f[0]
        list_for_info.append(current_value)
    return list_for_info


def update_employee(change_value, id_emp, new_value):
    conn5 = sqlite3.connect('Employee.sqlite')
    cursor5 = conn5.cursor()
    cursor5.execute(f"UPDATE employees SET {change_value}=? WHERE id=?", (new_value, id_emp))
    conn5.commit()
    conn5.close()


class Employee:
    def __init__(self, name, surname, mail, rank, salary):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.rank = rank
        self.salary = salary


def play():
    print("--------------------------------")
    print('Choose Employee')
    print('1: Select Employee by ID')
    print('2: Add Employee')
    print('3: See all Employees')
    print("--------------------------------")
    try:
        choose = int(input('Choose: '))
    except ValueError:
        print("--------------------------------")
        print("Only Numbers are allowed!")
        print("--------------------------------")
        play()
    print("--------------------------------")

    while True:
        try:
            if choose == 1:
                conn1 = sqlite3.connect('Employee.sqlite')
                cursor1 = conn1.cursor()
                print("--------------------------------")
                try:
                    employee_id = int(input('Employee ID: '))
                except ValueError:
                    print("--------------------------------")
                    print("Only Numbers are allowed!")
                    print("--------------------------------")
                    continue

                print("--------------------------------")
                employee = cursor1.execute(f'''SELECT name, surname , mail, rank, salary FROM employees WHERE id = {
                employee_id};''')
                employee_fetched = employee.fetchall()
                employee_info = employee_fetched[0]
                name = employee_info[0]
                surname = employee_info[1]
                mail = employee_info[2]
                rank = employee_info[3]
                salary = employee_info[4]
                employee_object = Employee(name, surname, mail, rank, salary)
                conn1.commit()
                conn1.close()
                while True:
                    try:
                        print("Employee control")
                        print("--------------------------------")
                        print("1: Employee Info")
                        print("2: Change Employee information")
                        print('3: Delete Employee')
                        print("--------------------------------")
                        choose1 = int(input('Choose:'))
                        print("--------------------------------")
                        if choose1 == 1:
                            print('Employee Info:')
                            print("--------------------------------")
                            print(f'ID: {employee_id}')
                            print(f'Name: {employee_object.name}')
                            print(f'Surname: {employee_object.surname}')
                            print(f'Mail: {employee_object.mail}')
                            print(f'Rank: {employee_object.rank}')
                            print(f'Salary: {employee_object.salary}')
                            print("--------------------------------")
                            continue
                        elif choose1 == 2:
                            print("Update Options")
                            print("--------------------------------")
                            print("1: Name")
                            print("2: Surname")
                            print('3: Mail')
                            print('4: Rank')
                            print('5: Salary')
                            print("--------------------------------")
                            try:
                                while True:
                                    print("--------------------------------")
                                    choose2 = int(input('Choose:'))
                                    print("--------------------------------")
                                    if choose2 == 1:
                                        name_for_update = input('Enter new Name: ')
                                        update_employee('name', employee_id, name_for_update)
                                        print("--------------------------------")
                                        print('Employee updated succesfully!')
                                        print("--------------------------------")
                                        play()
                                    elif choose2 == 2:
                                        surname_for_update = input('Enter new Surname: ')
                                        update_employee('surname', employee_id, surname_for_update)
                                        print("--------------------------------")
                                        print('Employee updated succesfully!')
                                        print("--------------------------------")
                                        play()
                                    elif choose2 == 3:
                                        mail_for_update = input('Enter new Mail: ')
                                        update_employee('mail', employee_id, mail_for_update)
                                        print("--------------------------------")
                                        print('Employee updated succesfully!')
                                        print("--------------------------------")
                                        play()
                                    elif choose2 == 4:
                                        rank_for_update = input('Enter new Rank: ')
                                        update_employee('rank', employee_id, rank_for_update)
                                        print("--------------------------------")
                                        print('Employee updated succesfully!')
                                        print("--------------------------------")
                                        play()
                                    elif choose2 == 5:
                                        salary_for_update = input('Enter new Salary: ')
                                        update_employee('salary', employee_id, salary_for_update)
                                        print("--------------------------------")
                                        print('Employee updated succesfully!')
                                        print("--------------------------------")
                                        play()
                                    else:
                                        print("--------------------------------")
                                        print('Wrong command!')
                                        print("--------------------------------")
                                        continue
                            except ValueError:
                                print("--------------------------------")
                                print("Only Numbers are allowed!")
                                print("--------------------------------")
                                continue

                        elif choose1 == 3:
                            delete_employee(employee_id)
                            print("--------------------------------")
                            print('Employee deleted succesfully!')
                            print("--------------------------------")
                            play()
                        elif choose1 == 4:
                            pass
                        else:
                            print("--------------------------------")
                            print('Wrong Command')
                            print('Try Again!')
                            print("--------------------------------")
                            continue

                    except ValueError:
                        print("--------------------------------")
                        print('Wrong Value!')
                        print('Try Numbers!')
                        print("--------------------------------")
                        continue
            elif choose == 2:
                conn2 = sqlite3.connect('Employee.sqlite')
                cursor2 = conn2.cursor()
                user_id = int(input('Enter employee id: '))
                if user_id in all_info('id'):
                    print("--------------------------------")
                    print("This id is already used!!")
                    print("Try Other Id!!")
                    print("--------------------------------")
                    continue
                else:
                    user_id = str(user_id)

                name = input('Enter employee name: ')
                surname = input('Enter employee surname: ')
                mail = input('Enter employee mail: ')
                rank = input('Enter employee rank(from 1-9): ')
                salary = input('Enter Salary: ')
                cursor2.execute('INSERT INTO employees(id,name,surname,mail,rank,salary) VALUES (?,?, ?, ?, ?, ?)',
                                (user_id, name, surname,
                                 mail, rank,
                                 salary))
                print("--------------------------------")
                print('Employee added succesfully')
                print("--------------------------------")
                conn2.commit()
                conn2.close()
                play()
            elif choose == 3:
                conn8 = sqlite3.connect('Employee.sqlite')
                conn8.cursor()
                all_name = all_info('name')
                all_id = all_info('id')
                print("--------------------------------")
                print("----ALL USER ID----")
                print("Name:Id")
                for k in all_name:
                    k_index = all_name.index(k)
                    print(f'{all_name[k_index]}:{all_id[k_index]}')
                print("--------------------------------")
                play()

        except IndexError:
            print("--------------------------------")
            print('Employee Did not found!')
            print("--------------------------------")
            continue


play()