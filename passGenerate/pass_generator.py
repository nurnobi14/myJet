from tkinter import*
from tkinter.ttk import Combobox
import random
scrn =Tk()
scrn.title('SPG-64x')
scrn.geometry('590x400')
scrn.resizable(0,0)
scrn.configure(background='lightblue')

def generate():
    global s1
    s1.set("")
    password = " "
    length=int(c1.get())
    lowercase= 'abcdefghijklmnopqrstuvwxyz'
    uppercase= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
    mixs_case='0123456789'+lowercase+uppercase+'@#$&*'
    
    if c2.get()=='Poor':
        for i in range(0,length):
            password=password+random.choice(lowercase)
        s1.set(password)
         
    elif c2.get()=='Medium':
          for i in range(0,length):
            password=password+random.choice(uppercase)
          s1.set(password)
    elif c2.get()=='Strong':
          for i in range(0,length):
            password=password+random.choice(mixs_case)
          s1.set(password)    
         
    
def Exit():
    scrn.destroy()

s1=StringVar("")
t1=Label(scrn,text="Smart Password Generator",font=('Arial',25),fg='light blue',bg='#9933FF')
t1.place(x=100,y=6)
t2=Label(scrn,text="generated code ",font=('Arial',14),fg='yellow',bg='#660066',width=13)
t2.place(x=110,y=90)

i1=Entry(scrn,font=('Arial',14,'bold'),textvariable=s1,fg='red',bg='#202020',width=17) #password result field
i1.place(x=260,y=90,height=28)

t3=Label(scrn,text="Length ",font=('Arial',14),fg='yellow',bg='#660066',width=13)
t3.place(x=110,y=130)
t4=Label(scrn,text="strength ",font=('Arial',14),fg='yellow',bg='#660066',width=13)
t4.place(x=110,y=165)

c1=Entry(scrn,font=('Arial',14),fg='blue',width=17)#for length of code
c1.place(x=260,y=130)
c2=Combobox(scrn,font=('Arial',14),width=15) # dropdown options
c2['values']=('Poor','Medium','Strong')
c2.current(1)
c2.place(x=260,y=165)

b1 = Button(scrn,text='Generate',font=('Arial',14,'bold'),fg='white',bg='green',activebackground='blue',activeforeground='white',command=generate)
b1.place(x=260,y=210)
b2 = Button(scrn,text='Exit',font=('Arial',14,'bold'),fg='white',bg='green',activebackground='blue',activeforeground='white',command=Exit)
b2.place(x=370,y=210)

scrn.mainloop()
