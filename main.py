from tkinter import *
from cal import *
from playsound import playsound
# import threading
import time

#Cấu hình cửa sổ
window = Tk()
window.title('Calculator')
window.geometry('237x217')
window.resizable(width=False, height=False)

#Màn hình hiển thị
display = Entry(window, font=('arial',30,'bold'), border=5, bg= 'aqua', justify=RIGHT)
display.pack(side=TOP, fill=X)

#Khai báo biến sử dụng trong các hàm
first_number = ''
second_number = ''
operator = ''


#Hàm ấn các số
def press_num(number):
    global operator, first_number, second_number
    if display.get() != '':
        display.config(state="normal")
        # display.delete(0, END)
        if operator == '':
            display.insert(len(display.get()),number)
            first_number = display.get()
            # print(first_number)
        elif operator != '' and second_number == '':
            display.delete(0, END)
            display.insert(0,number)
            second_number = number
        elif operator != '' and second_number != '':
            display.insert(len(display.get()),number)
            second_number = display.get()
        display.config(state="disabled")
    else:
        display.config(state="normal")
        display.insert(0,number)
        first_number = display.get()
        display.config(state="disabled")

#Hàm dấu(toán tử)
def press_operator(clicked_operator):
    global operator, first_number, second_number
    if display.get() != '':
        display.config(state="normal")
        first_number = display.get()
        operator = clicked_operator
        display.config(state="disabled")
    else:
        display.config(state="normal")
        display.delete(0, END)
        first_number = ''
        second_number = ''
        operator = ''
        display.config(state="disabled")

#Hàm xóa trắng màn hình
def press_clear():
    global first_number, second_number, operator
    display.config(state="normal")
    display.delete(0, END)
    first_number = ''
    second_number = ''
    operator = ''
    playsound('button-3.mp3')

#Hàm hiển thị sau khi bấm dấu '='
def press_equal():
    # playsound('beep-07a.mp3')
    global operator, first_number, second_number
    if first_number != ''and second_number != '' and operator != '':
        display.config(state="normal")
        display.delete(0, END)
        print(f'{first_number}  {operator}  {second_number}')
        result = calculate(operator, float(first_number), float(second_number))
        print(int(result)) if result.is_integer() else print(round(result,10))
        display.insert(0, int(result)) if result.is_integer() else display.insert(0, round(result,8))
        display.config(state="disabled")
        first_number = ''
        second_number = ''
        operator = ''       
    else:
        display.delete(0, END)
        first_number = ''
        second_number = ''
        operator = ''

#Hàm hiển thị sau khi bấm dấu '.'
def press_point():
    if display.get() != '' and '.' not in display.get():
        display.config(state="normal")
        display.insert(len(display.get()),'.')
        display.config(state="disabled")

#Hàm thay đổi giá trị với (+/-)
def press_change_value():
    global first_number , second_number, operator
    if display.get() != '':
        display.config(state="normal")
        if '-' not in display.get():
            display.insert(0,'-')
            if first_number == '':
                first_number = display.get()
            elif first_number != '' and second_number == '':
                first_number = first_number * (-1)
            elif operator != '':
                # second_number = second_number * (-1)
                second_number = float(display.get())
        elif '-' in display.get():
            display.delete(-1)
        display.config(state="disabled")
        
    else:
        first_number = ''
        second_number = ''
        operator = ''

#Hàm tính phần trăm
def press_per():
    global first_number,operator,second_number

    if display.get() != '':
        display.config(state="normal")
        first_number = display.get()
        display.delete(0, END)
        second_number = ''
        operator = ''
        display.insert(0,round(float(first_number)/100,2))
        display.config(state="disabled")
    else:
        first_number = ''
        second_number = ''
        operator = ''

#Hàm thực thi các thao tác
def execute():
    frame1 = Frame(window)
    frame1.pack(fill=X)


    button_AC = Button(frame1, text='AC',width=6, command= lambda: press_clear(), border=5)
    button_AC.grid(row=0, column=0)


    button_value = Button(frame1, text='+/-',width=6, border=5, command = lambda: press_change_value())
    button_value.grid(row=0, column=1)

    button_per = Button(frame1, text='%',width=6, border=5, command= lambda: press_per())
    button_per.grid(row=0, column=2)

    button_div = Button(frame1, text='÷',bg='orange',width=6, border=5, command = lambda: press_operator('/'))
    button_div.grid(row=0, column=3)



    button7 = Button(frame1, text='7',width=6, command= lambda: press_num(7), border=5)
    button7.grid(row=1, column=0)

    button8 = Button(frame1, text='8',width=6, command= lambda: press_num(8), border=5)
    button8.grid(row=1, column=1)

    button9 = Button(frame1, text='9',width=6, command= lambda: press_num(9), border=5)
    button9.grid(row=1, column=2)

    button_x = Button(frame1, text='x',bg='orange',width=6, border=5, command = lambda: press_operator('*'))
    button_x.grid(row=1, column=3)


    button4 = Button(frame1, text='4',width=6, command= lambda: press_num(4), border=5)
    button4.grid(row=2, column=0)

    button5 = Button(frame1, text='5',width=6, command= lambda: press_num(5), border=5)
    button5.grid(row=2, column=1)

    button6 = Button(frame1, text='6',width=6, command= lambda: press_num(6), border=5)
    button6.grid(row=2, column=2)

    button_minus = Button(frame1, text='-',bg='orange',width=6, border=5, command = lambda: press_operator('-'))
    button_minus.grid(row=2, column=3)


    button1 = Button(frame1, text='1',width=6, command= lambda: press_num(1), border=5)
    button1.grid(row=3, column=0)

    button2 = Button(frame1, text='2',width=6, command= lambda: press_num(2), border=5)
    button2.grid(row=3, column=1)

    button3 = Button(frame1, text='3',width=6, command= lambda: press_num(3), border=5)
    button3.grid(row=3, column=2)

    button_plus = Button(frame1, text='+',bg='orange',width=6, border=5, command = lambda: press_operator('+'))
    button_plus.grid(row=3, column=3)


    frame2 = Frame(window)
    frame2.pack(side=LEFT)

    button0 = Button(frame1, text='0',width=15, command= lambda: press_num(0), border=5)
    button0.grid(row=4, columnspan=2)

    button_point = Button(frame1, text='.',width=6, command= lambda: press_point(), border=5)
    button_point.grid(row=4, column=2)

    button_eq = Button(frame1, text='=',width=6, bg='orange', border=5, command= lambda: press_equal())
    button_eq.grid(row=4, column=3)

#______________Hàm thực thi chính____________
if __name__ == '__main__':
    execute()

window.mainloop()
