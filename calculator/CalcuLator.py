from tkinter import*

def comm(event):
    global scvalues
    tct=event.widget.cget("text")
    if tct=="=":
        if scvalues.get().isdigit():
            value=int(scvalues.get())
            
        else:
            value=eval(ib.get())
         
        scvalues.set(value)
        ib.update()
        
    elif tct=='C':
        scvalues.set("")
        ib.update()
    else:
        scvalues.set(scvalues.get()+tct)
        ib.update()

#for screen:
screen = Tk()
screen.title('My Calculator')
screen.geometry('312x324')
screen.resizable(0,0)

scvalues = StringVar("")

#frame part start
input_frame= Frame(screen,width=312,height=54)
input_frame.pack(side=TOP)
btm_frame1=Frame(screen,width=312,height=15,bg='grey')
btm_frame1.pack(side=TOP)
btm_frame=Frame(screen,width=312,height=5,bg='grey')
btm_frame.pack(side=TOP)
btm_frame2=Frame(screen,width=312,height=5)
btm_frame2.pack(side=TOP)
btm_frame3=Frame(screen,width=312,height=5)
btm_frame3.pack(side=TOP)
btm_frame4=Frame(screen,width=312,height=5)
btm_frame4.pack(side=TOP)
#End frame part

#inputBox top most frame part start
ib=Entry(input_frame,font=('Arial',33),bg='#7D9E7D',textvariable=scvalues,width=300)
ib.pack()
#inputBox top most frame part End

#start clear button
c=Button(btm_frame1,text='C',fg='#DCF1F5',bg='#000033',cursor='hand2',width=33,height=3)
c.bind('<Button-1>',comm)
c.pack(side=LEFT)
#End clear button

#start 4 button in third frame
div=Button(btm_frame1,text='/',fg='#DCF1F5',bg='#000033',cursor='hand2',width=12,height=3)
div.bind('<Button-1>',comm)
div.pack(side=LEFT)

b1=Button(btm_frame,text='1',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b1.bind("<Button-1>",comm)
b1.pack(side=LEFT)

b2=Button(btm_frame,text='2',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b2.bind("<Button-1>",comm)
b2.pack(side=LEFT)

b3=Button(btm_frame,text='3',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b3.bind("<Button-1>",comm)
b3.pack(side=LEFT)

mi=Button(btm_frame,text='-',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
mi.bind("<Button-1>",comm)
mi.pack(side=LEFT)

b4=Button(btm_frame2,text='4',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b4.bind("<Button-1>",comm)
b4.pack(side=LEFT)

b5=Button(btm_frame2,text='5',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b5.bind("<Button-1>",comm)
b5.pack(side=LEFT)

b6=Button(btm_frame2,text='6',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b6.bind("<Button-1>",comm)
b6.pack(side=LEFT)

mu=Button(btm_frame2,text='*',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
mu.bind("<Button-1>",comm)
mu.pack(side=LEFT)

b7=Button(btm_frame3,text='7',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b7.bind("<Button-1>",comm)
b7.pack(side=LEFT)

b8=Button(btm_frame3,text='8',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b8.bind("<Button-1>",comm)
b8.pack(side=LEFT)

b9=Button(btm_frame3,text='9',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b9.bind("<Button-1>",comm)
b9.pack(side=LEFT)

ad=Button(btm_frame3,text='+',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
ad.bind("<Button-1>",comm)
ad.pack(side=LEFT)

b0=Button(btm_frame4,text='0',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b0.bind("<Button-1>",comm)
b0.pack(side=LEFT)

b00=Button(btm_frame4,text='00',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
b00.bind("<Button-1>",comm)
b00.pack(side=LEFT)

dot=Button(btm_frame4,text='.',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
dot.bind("<Button-1>",comm)
dot.pack(side=LEFT)

eq=Button(btm_frame4,text='=',fg='#DCF1F5',bg='#000033',cursor='hand2',width=10,height=3)
eq.bind("<Button-1>",comm)
eq.pack(side=LEFT)
#eND 4 button in third frame

screen.mainloop()