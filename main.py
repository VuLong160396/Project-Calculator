from tkinter import *
from cal import *
from playsound import playsound
import threading
import time

window = Tk()
window.title('Calculator')
window.geometry('237x217')
window.resizable(width=False, height=False)

#Màn hình
display = Entry(window, font=('arial',30,'bold'), border=5, bg= 'aqua', justify=RIGHT)
display.pack(side=TOP, fill=X)

#Khai báo biến sử dụng trong các hàm
first_number = ''
second_number = ''
operator = ''

def plus(first_number, second_number):
    # if first_number.number():
    return first_number+second_number

def minus(first_number, second_number):
    return first_number-second_number

def multi(first_number, second_number):
    return first_number*second_number

def divide(first_number, second_number):
    if second_number == 0:
        raise Exception('Sai cú pháp')
    return first_number/second_number

def calculate(operator, first_number, second_number):
    if operator == "+":
        return plus(first_number, second_number)
    elif operator == "-":
        return minus(first_number, second_number)
    elif operator == "*":
        return multi(first_number, second_number)
    elif operator == "/":
        return divide(first_number, second_number)

#Hàm ấn nút
def press_num(widget, number):
    global operator, first_number, second_number
    # if widget.get() != '' :
    # display.insert(0,'')
    # playsound("Ting.mp3", block= False)

    #Ấn số tiếp theo sau khi ấn '='(kết qua của 1 phép toán trước đó) vì sau dấu bằng xóa hết first_number, second_number, operator
    if operator == '' and second_number == '' and first_number == '':
        widget.delete(0, END)
        widget.insert(0, number)
        first_number = widget.get()

    #Ấn button số lần đầu sau khi bấm toán tử
    elif operator != '' and second_number == '':  
        # widget.insert(len(widget.get()),number)
        first_number = widget.get()
        widget.delete(0, END)
        widget.insert(0, number)
        if '-' in widget.get():
            print(type(widget.get()))
        second_number = number
    
    #Dãy số của toán hạng 2(nhiều hơn 1 ký tự)
    elif second_number != '':
        widget.insert(len(widget.get()),number)
        if '-' in widget.get():
            print(type(widget.get()))
        second_number = widget.get()
    #Dãy số của toán hạng 1
    else:
        widget.insert(len(widget.get()),number)

#Hàm dấu(toán tử)
def press_operator(clicked_operator):
    # global operator
    # operator = clicked_operator
    global operator, first_number, second_number
    if first_number != '' and operator != '' and second_number != '':
        # temp = first_number
        press_equal()
        # first_number = temp
    else:
        operator = clicked_operator

#Hàm xóa trắng màn hình
def clear(widget):
    global first_number, second_number, operator

    widget.delete(0, END)
    first_number = ''
    second_number = ''
    operator = ''

#Hàm hiển thị sau khi bấm dấu '='
def press_equal():
    global operator, first_number, second_number
    display.delete(0, END)
    if first_number != ''and second_number != '' and operator != '':
        #Kiểm tra số thập phân hay số nguyên:
        if calculate(operator, float(first_number), float(second_number)) == int(calculate(operator, float(first_number), float(second_number))): 
            # print('Số nguyên')
            display.insert(0, int(calculate(operator, float(first_number), float(second_number))))
        else:
            # print('Số thập phân')
                display.insert(0, (calculate(operator, float(first_number), float(second_number))))
    else:
        clear(display)

    first_number = ''
    second_number = ''
    operator = ''
    # playsound('Ting.mp3')

#Hàm tính phần trăm (%)
def press_change_value():
    if '-' not in display.get():
        display.insert(0,'-')
    elif '-' in display.get():
        display.delete(-1)






def press_per():
    global operator, first_number, second_number
    first_number = ''
    second_number = ''
    operator = ''
    if display.get() != '':
        first_number = display.get()
        display.delete(0, END)
        display.insert(0,round(float(first_number)/100,2))
        first_number = ''
    else:
        pass

'''#__________________________________________

#Vấn đề vẫn bị hiển thị ra số có 1.0 hay 2.0 => kiểm tra số nguyên hay số thập phân
# a = float(input("number:"))
# if int(a)== a:
#     print('số nguyên')
# else:
#     print('số thập phân')

#05/10/21
#Xử lý được vấn đề sau khi bấm dấu '=' thì ấn 1 số mới sẽ xóa đi kết quả của phép toán trước đó mà thay vào số vừa ấn
#b1 sau khi ấn '=' xóa toàn bộ first_number, second_number, operator và khi ấn nhập số mới thì gán first_number == widget.get() chính là số vừa nhập
#Vấn đề: phần xử lý hàm change_value ký tự '+/-'
#Thay đổi giá trị của widget.get()
#==> Phương án xử lý theo kiểu chỉ nhân giá trị của widget.get() với -1

7/10 Vấn đề gặp phải sau khi ấn change_value (+/-) thì mới hiển thị số âm chưa hiển thị được số dương => Tạo sao cho ấn mà ẩn hiện dấu '-' trên màn hình

12/10 Đã ẩn hiện được dấu '-' nhưng khi thực hiện phép tính với số hạng thứ 2 có dấu '-' thì chưa được

13/10 Chưa xử lý được dấu trừ ở số hạng thứ 2, và phép tính 2 số thập phân vẫn bị chưa làm tròn

Hàm press_operater():
    khi thực hiện liên tục tính toán mà k ấn dấu '=', thì các operator thực hiện như dấu bằng tuy nhiên chỉ được 1 lần do sau khi gọi hàm press_equal() thì số hạng và operator đã bị xóa hết
#__________________________________________'''



frame1 = Frame(window)
frame1.pack(fill=X)


button_AC = Button(frame1, text='AC',width=6, command= lambda: clear(display), border=5)
button_AC.grid(row=0, column=0)


button_value = Button(frame1, text='+/-',width=6, border=5, command = lambda: press_change_value())
button_value.grid(row=0, column=1)

button_per = Button(frame1, text='%',width=6, border=5, command= lambda: press_per())
button_per.grid(row=0, column=2)

button_div = Button(frame1, text='÷',bg='orange',width=6, border=5, command = lambda: press_operator('/'))
button_div.grid(row=0, column=3)



button7 = Button(frame1, text='7',width=6, command= lambda: press_num(display,7), border=5)
button7.grid(row=1, column=0)

button8 = Button(frame1, text='8',width=6, command= lambda: press_num(display,8), border=5)
button8.grid(row=1, column=1)

button9 = Button(frame1, text='9',width=6, command= lambda: press_num(display,9), border=5)
button9.grid(row=1, column=2)

button_x = Button(frame1, text='x',bg='orange',width=6, border=5, command = lambda: press_operator('*'))
button_x.grid(row=1, column=3)


button4 = Button(frame1, text='4',width=6, command= lambda: press_num(display,4), border=5)
button4.grid(row=2, column=0)

button5 = Button(frame1, text='5',width=6, command= lambda: press_num(display,5), border=5)
button5.grid(row=2, column=1)

button6 = Button(frame1, text='6',width=6, command= lambda: press_num(display,6), border=5)
button6.grid(row=2, column=2)

button_minus = Button(frame1, text='-',bg='orange',width=6, border=5, command = lambda: press_operator('-'))
button_minus.grid(row=2, column=3)


button1 = Button(frame1, text='1',width=6, command= lambda: press_num(display,1), border=5)
button1.grid(row=3, column=0)

button2 = Button(frame1, text='2',width=6, command= lambda: press_num(display,2), border=5)
button2.grid(row=3, column=1)

button3 = Button(frame1, text='3',width=6, command= lambda: press_num(display,3), border=5)
button3.grid(row=3, column=2)

button_plus = Button(frame1, text='+',bg='orange',width=6, border=5, command = lambda: press_operator('+'))
button_plus.grid(row=3, column=3)


frame2 = Frame(window)
frame2.pack(side=LEFT)

button0 = Button(frame1, text='0',width=15, command= lambda: press_num(display,0), border=5)
button0.grid(row=4, columnspan=2)

button_point = Button(frame1, text='.',width=6, command= lambda: press_num(display,'.'), border=5)
button_point.grid(row=4, column=2)

button_eq = Button(frame1, text='=',width=6, bg='orange', border=5, command= lambda: press_equal())
button_eq.grid(row=4, column=3)


window.mainloop()







