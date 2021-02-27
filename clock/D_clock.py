from tkinter import*
import datetime
import time

scrn = Tk()
scrn.title('Digital Clock')
scrn.geometry('500x400')
scrn.resizable(1,1)
scrn.configure(background='black')
t=Label(scrn,text='ourclock.com',font=('Arial',12),fg='lightblue',bg='black')
t.place(x=190,y=1)
t1=Label(scrn,text='My|Time',font=('Arial',20,'bold'),fg='lightblue',bg='black')
t1.place(x=180,y=20)

def Clockpart():
    t2=time.strftime('%I:%M:%S %p')
    t3=Label(scrn, text=t2,font=('ds digital',40,'bold'),fg='light green',bg='black')
    t3.after(200,Clockpart)
    t3.place(x=80,y=190)
    t4=datetime.date.today()
    t5=Label(scrn, text=t4.year,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=80,y=90)
    t6=Label(scrn, text=t4.month,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=240,y=90)
    t7=Label(scrn, text=t4.day,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=305,y=90)
    t8=Label(scrn, text='YEAR',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=90,y=145)
    t_brk=Label(scrn, text=' ',font=('ds digital',15,'bold'),bg='lightblue',width=30).place(x=50,y=180,height=1) #extra_line adding_for linegap
    t_brk2=Label(scrn, text=' ',font=('ds digital',15,'bold'),bg='lightblue',width=30).place(x=50,y=183,height=1)
    t9=Label(scrn, text='MONTH',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=215,y=145)
    t10=Label(scrn, text='DATE',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=305,y=145)
    t11=Label(scrn, text='HOUR',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=80,y=250)
    t12=Label(scrn, text='MIN',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=165,y=250)
    t13=Label(scrn, text='SEC',font=('ds digital',15,'bold'),fg='green',bg='black').place(x=235,y=250)
    t14 =Label(scrn,text='Made by :Md Nurnobi Hossain',font=("Arial",10,'bold'),fg='white',bg='black').place(x=10,y=340)
    t15=Label(scrn,text='Powered By: PyTHoN',font=("Arial",8,'bold'),fg='yellow',bg='black').place(x=380,y=376)
    
Clockpart()
scrn.mainloop()