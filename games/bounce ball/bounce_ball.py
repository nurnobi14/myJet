from tkinter import*
import random
from tkinter import messagebox

sc2=Tk()
sc2.geometry('400x400+350+150')
sc2.config(background='black')

def start_game():
    sc2.destroy()
    bat_game()

def bat_game():
    scrn=Tk()
    scrn.geometry("750x650+150+10")
    scrn.title("Bounce Ball")
    scrn.config(background="white")
    score=StringVar("")
    score.set('0')
    sc=0
    sc=int(score.get())
    c=Canvas(scrn,height=600,width=750,background='orange')
    c.pack()
    t=Label(scrn,text="YOUR SCORE :",bg="white",fg='green',font=('Arial',15))
    t.place(x=270,y=610)
    e=Entry(scrn,textvariable=score,bg='white',fg='green',bd=0,font=('Arial',15),width=3)
    e.place(x=425,y=612)
    xc=random.randint(10,600)
    yc=random.randint(300,350)
    c1=c.create_oval(xc,yc,xc+50,yc+50,fill='blue',width=2,outline='teal')
    xspeed=random.randint(4,10)
    yspeed=random.randint(4,10)
    
    rec=c.create_rectangle(400,580,600,600,fill="red")
    
    def move_r8(event):
        c.move(rec,-30,0)
    def move_l8(event):
        c.move(rec,30,0)
    
    c.bind('<Button-1>',move_r8)
    c.bind('<Button-3>',move_l8)
    
    while True:
        c.move(c1,xspeed,yspeed)
        p=c.coords(c1)
        
        if p[2] >= 750 or p[0] < 0:
            xspeed*=-1
        if p[1] <= 0:
            yspeed*=-1
        c.update()
        c.after(20)
        if (len(c.find_overlapping(p[0],p[1],p[2],p[3]))) > 1:
            score.set(int(score.get())+1)
            yspeed*=-1
            e.update()
        if p[3] > 640:
            print("game lost")
            messagebox.showinfo("SORRY","GAME IS OVER")
            scrn.destroy()
            sc=Tk()
            sc.geometry("300x300+380+180")
            sc.config(background='black')
            print("game lost")
            def restart_game():
                sc.destroy()
                bat_game()
                
            def quit_game():
                sc.destroy()
            
            b=Button(sc,text="RESTART",font=("Arial",15),bd=2,bg='yellow',fg='black',command=restart_game)
            b.place(x=100,y=70)
            b2=Button(sc,text="QUIT?",font=("Arial",15),bd=2,bg='red',fg='white',command=quit_game)
            b2.place(x=115,y=120)
            
            
            
def Exit():
    sc2.destroy()

b9=Button(sc2,text="START GAME",font=('Arial',15),bg='pink',fg='red',bd=2,command=start_game)
b9.place(x=140,y=130)
b10=Button(sc2,text="QUIT GAME",font=('Arial',15),bg='pink',fg='red',bd=2,command=Exit)
b10.place(x=149,y=200)

