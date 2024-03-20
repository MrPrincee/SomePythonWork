from tkinter import *


def submit():
    result = entry.get()
    result = str(result)

    if ('*' in result) and ('/' in result):
        entry.delete(0,END)
        all_lists = []
        for j in range(result.count('*')+result.count('/') + 1):
            new_list = []

            all_lists.append(new_list)

        indices = []
        for index, char in enumerate(str(result)):
            if char == "*" or char == '/':
                indices.append(index)
        i = 0
        while i < (len(all_lists) - 1):
            for k in str(result):
                all_lists[i].append(k)
                if str(result).index(k) in indices:
                    i += 1
                    continue

        m = 0
        final_value = 1
        first = ''
        second = ''
        third = ''
        while m < (len(all_lists)-1):
            if '*' in all_lists[m]:
                if final_value == 1:
                    for k in all_lists[m]:
                        if k != '*':
                           first += k
                    final_first = first
                    for f in all_lists[m+1]:
                        if f != '*' and f != '/':
                            second += f
                    final_second = second
                    current_value = int(final_first)*int(final_second)
                    final_value = current_value * final_value
                    first = ''
                    second = ''
                    if m < (len(all_lists)-1):
                        m += 1
                        continue
                    else:
                        break
                else:
                    for k in all_lists[m+1]:
                        if k !='*' and k !='/':
                            first += k
                    final_value = final_value* int(first)
                    first = ''
                    if m < (len(all_lists)-1):
                        m += 1
                        continue
                    else:
                        break

            elif '/' in all_lists[m]:
                if final_value == 1:
                    for k in all_lists[m]:
                        if k != '/':
                           first += k
                    for f in all_lists[m+1]:
                        if f != '*' and f != '/':
                            second += f
                    final_value = int(first)/int(second)
                    first = ''
                    second = ''
                    if m < (len(all_lists)-1):
                        m += 1
                        continue
                    else:
                        break
                else:
                    for k in all_lists[m + 1]:
                        if k != '*' and k != '/':
                            first += k
                    final_value = final_value / int(first)
                    first = ''
                    if m < (len(all_lists) - 1):
                        m += 1
                        continue
                    else:
                        break

            elif ('/' not in all_lists[m]) and ('*' not in all_lists[m]):
                last_list = all_lists[len(all_lists)-1]
                for i in last_list:
                    third = third + str(i)
                if '*' in all_lists[m-1]:
                    final_value = final_value * int(third)
                    break
                elif '/' in all_lists[m-1]:
                    final_value = final_value / int(third)
                    break
        label = Label(window, text=f'Result:{final_value}')
        label.pack()
    elif '*' in result:
        parts = result.split('*')
        if len(parts) == 2:
            first_half = parts[0]
            second_half = parts[1]
            first_half = int(first_half)
            second_half = int(second_half)
            mult = first_half * second_half
            label = Label(window, text=f'Result:{mult}')
            label.pack()
            entry.delete(0, END)
        elif len(parts) > 2:
            mult_result = 0
            parts_list = []
            for i in range(len(parts)):
                parts_list.append(int(parts[i]))
            j = 0
            if len(parts_list) > 0:
                while j < (len(parts_list)-1):
                    if mult_result == 0:
                        mult_result = parts_list[j] * parts_list[j+1]
                        j += 1
                    elif mult_result > 0:
                        mult_result = mult_result * parts_list[j+1]
                        j += 1
                    continue

            label = Label(window, text=f'Result:{mult_result}')
            label.pack()

        else:
            entry.delete(0,END)
            label = Label(window, text=f'Wrong syntax')
            label.pack()

    elif '/' in result:
        parts = result.split('/')
        try:
            if len(parts) == 2:
                first_half = parts[0]
                second_half = parts[1]
                first_half = int(first_half)
                second_half = int(second_half)
                mult = first_half / second_half
                label = Label(window, text=f'Result:{mult}')
                label.pack()
                entry.delete(0, END)
            elif len(parts) > 2:
                div_result = 0
                parts_list = []
                for i in range(len(parts)):
                    parts_list.append(int(parts[i]))
                print(parts_list[0])
                print(parts_list[1])
                print(parts_list[2])
                j = 0
                if len(parts_list) > 0:
                    while j < (len(parts_list)-1):
                        if div_result == 0:
                            div_result = parts_list[j] / parts_list[j+1]
                            j += 1
                        elif div_result > 0:
                            div_result = div_result / parts_list[j+1]
                            j += 1
                        continue


                label = Label(window, text=f'Result:{div_result}')
                label.pack()
            else:
                entry.delete(0, END)
                label = Label(window, text=f'Wrong syntax')
                label.pack()

        except ZeroDivisionError:
            label = Label(window, text="Can't Divide with 0")
            label.pack()
            entry.delete(0,END)
    elif '+' in result:
        final_result = eval(result)
        label = Label(window, text=f'Result:{final_result}')
        label.pack()
    elif '-' in result:
        final_result = eval(result)
        label = Label(window, text=f'Result:{final_result}')
        label.pack()
    elif '-' and '+':
        final_result = eval(result)
        label = Label(window, text=f'Result:{final_result}')
        label.pack()


    else:
        entry.delete(0,END)
        label = Label(window, text="Can't work with this values!")
        label.pack()


def submit_with_eval():
    result = entry.get()
    final_result = eval(result)
    label = Label(window, text=f'Result:{final_result}')
    label.pack()

def button_min1():
    entry.insert(END,'-')

def button_p():
    entry.insert(END,'+')


def button0():
    entry.insert(END, '0')

def button1():
    entry.insert(END, '1')


def button2():
    entry.insert(END, '2')


def button3():
    entry.insert(END, '3')


def button4():
    entry.insert(END, '4')


def button5():
    entry.insert(END, '5')


def button6():
    entry.insert(END, '6')

def button7():
    entry.insert(END, '7')

def button8():
    entry.insert(END, '8')

def button9():
    entry.insert(END, '9')

def button_m():
    entry.insert(END, '*')

def button_d():
    entry.insert(END,'/')


window = Tk()
window.title("Calculator")
window.geometry("200x500")

frame = Frame(master=window, height=200, bg='black')
frame.pack(fill=X)

entry = Entry(frame)
entry.pack(fill=BOTH, expand=True, padx=10, pady=20)

frame2 = Frame(master=window,height=300,bg='red')

button_1 = Button(frame2, text='1',width=5,height=3,borderwidth=3,command=button1)
button_1.place(x=10,y=10)

button_2 = Button(frame2, text='2',width=5,height=3,borderwidth=3,command=button2)
button_2.place(x=70,y=10)

button_3 = Button(frame2, text='3',width=5,height=3,borderwidth=3,command=button3)
button_3.place(x=130,y=10)

button_4 = Button(frame2, text='4',width=5,height=3,borderwidth=3,command=button4)
button_4.place(x=10,y=70)

button_5 = Button(frame2, text='5',width=5,height=3,borderwidth=3,command=button5)
button_5.place(x=70,y=70)

button_6 = Button(frame2, text='6',width=5,height=3,borderwidth=3,command=button6)
button_6.place(x=130,y=70)

button_7 = Button(frame2, text='7',width=5,height=3,borderwidth=3,command=button7)
button_7.place(x=10,y=130)

button_8 = Button(frame2, text='8',width=5,height=3,borderwidth=3,command=button8)
button_8.place(x=70,y=130)

button_9 = Button(frame2, text='9',width=5,height=3,borderwidth=3,command=button9)
button_9.place(x=130,y=130)

button_0 = Button(frame2, text='0',width=5,height=3,borderwidth=3,command=button0)
button_0.place(x=70,y=190)

button_mult = Button(frame2, text='*',width=5,height=3,borderwidth=3,command=button_m)
button_mult.place(x=10,y=190)

button_div = Button(frame2, text='/',width=5,height=3,borderwidth=3,command=button_d)
button_div.place(x=130,y=190)

button_s = Button(frame2,text='Submit',width=5,height=2,borderwidth=3,command=submit)
button_s.place(x=70,y=250)

button_plus = Button(frame2,text='+',width=5,height=2,borderwidth=3,command=button_p)
button_plus.place(x=10,y=250)

button_min = Button(frame2,text='-',width=5,height=2,borderwidth=3,command=button_min1)
button_min.place(x=130,y=250)

frame2.pack(fill=X)

window.mainloop()

