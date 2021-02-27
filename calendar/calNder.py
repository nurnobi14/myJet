from tkinter import*
import calendar
screen1 = Tk()
screen1.title('MyCaLenDar')
screen1.geometry("500x300")
screen1.configure(background = "teal")

def calendars():
    screen2 = Tk()
    screen2.title("calendar")
    screen2.geometry("800x800")
    year= int(i1.get())
    see= calendar.calendar(year)
    t=Label(screen2, text=see,font="Consolas 12 bold",fg='blue',bg='pink')
    t.grid(row=4, column=1, padx=35)
    screen2.mainloop()

def Exit():
    screen1.destroy()

t1 =Label(screen1,text='INTERNATIONAL CALENDAR',font=("Arial",20,'bold'),fg='white',bg='teal').place(x=50,y=10)
t2 =Label(screen1,text='Enter year',font=("Arial",15,'bold'),fg='white',bg='black').place(x=40,y=120)
i1=Entry(screen1,font=("Arial",15,'bold'),fg='blue',bg="lightblue",width=10)
i1.place(x=160,y=120,height=31)

b1= Button(screen1,text="go and see",font=('Arial',15,'bold'),activebackground='green',bg='blue',fg='white',command=calendars).place(x=277,y=120,height=31)
 
b2= Button(screen1,text="Exit?",font=('Arial',15,'bold'),bg='orange',fg='white',activebackground='red',command=Exit).place(x=190,y=160,height=31)
 
t2 =Label(screen1,text='made by :Md Nurnobi Hossain',font=("Arial",10,'bold'),fg='white',bg='teal').place(x=10,y=250)
t2 =Label(screen1,text='Powered By: PyTHoN',font=("Arial",8,'bold'),fg='yellow',bg='teal').place(x=350,y=270)
screen1.mainloop()