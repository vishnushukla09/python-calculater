from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("simple calculater")

lbl1 = Label(window,text="enter 1st number : ")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="enter 2nd number : ")
lbl2.place(x=50,y=100)

lbl3 = Label(window,text="Result :")
lbl3.place(x=120,y=150)

t1 = Entry()
t1.place(x=180 , y= 50)

t2 = Entry()
t2.place(x=180 , y= 100)

t3 = Entry()
t3.place(x=180 , y= 150)

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum = num1 + num2
  t3.insert(END,str(sum))

b1 =Button (window, text= "Add",command= add)
b1.place(x=50, y=200)

