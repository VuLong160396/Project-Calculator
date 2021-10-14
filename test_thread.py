import threading
import time
from tkinter import *
from playsound import playsound
win = Tk()
win.geometry('200x200')
win.resizable(False,False)

def sound():
    playsound('beep-07a.mp3')
    # playsound()

def display(name):
    label1 = Label(win, text=name, bg='red')
    label1.pack()

def display1(name):
    label1 = Label(win, text=name, bg='red')
    label1.pack()

def alo():
    thread2= threading.Thread(target= display('long'))
    thread1= threading.Thread(target= sound())
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    # display1('long')
    # display('alo')






# def square(number):
#     print('Calculate square of numbers')
#     for x in number:
#         time.sleep(1)
#         print('square:', x*x)

# def cube(number):
#     print('Calculate cube of numbers')
#     for x in number:
#         time.sleep(1)
#         print('Cube: ', x*x*x)
# t = time.time()
# def test():
#     arr = [1, 3, 5, 7, 9]
#     thread1 = threading.Thread(target= square, args=(arr,))
#     thread2 = threading.Thread(target= cube, args=(arr,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()
# print('Done in:', time.time() - t)

but1 = Button(win, text='button', command= lambda: alo())
but1.pack()



win.mainloop()

