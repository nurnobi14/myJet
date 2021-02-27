from tkinter import*
import random

scrn=Tk()
scrn.geometry('400x400')
scrn.title('DiceRoller')

dice1=PhotoImage(file="1.png")
dice2=PhotoImage(file="2.png")
dice3=PhotoImage(file="3.png")
dice4=PhotoImage(file="4.png")
dice5=PhotoImage(file="5.png")
dice6=PhotoImage(file="6.png")

Dice=[dice1,dice2,dice3,dice4,dice5,dice6]

def Roller():
    print("DICING ROLL")
    d=random.choice(Dice)
    t=Label(scrn,image=d)
    t.place(x=100,y=35)

def Exit():
    print('game exit')
    scrn.destroy()

b=Button(scrn,text="Roll Dice",font=('Arial',20),bg='#5C0C4F',fg='orange',cursor="hand2",command=Roller)
b.place(x=130,y=310)
exit_game=Button(scrn,text="exit?",font=('Arial',12),bg='orange',fg='#5C0C4F',cursor="hand2",command=Exit)
exit_game.place(x=300,y=325)
