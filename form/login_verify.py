from tkinter import*
from tkinter import messagebox

scrn=Tk()
scrn.geometry('1100x650+110+20')
scrn.title('LOGIN PAGE')
scrn.resizable(0,0)
scrn.configure(background='floral white')

def Page():
    if i1.get()=="Username" and i2.get()=="Password":
        messagebox.showerror("Error", 'Please fill out this fields')
    
    elif i1.get()=="Username":
        messagebox.showerror('Error','Please Enter your Username')
    
    elif i2.get()=="Password":
        messagebox.showerror('Error','Please Enter your Password')
    
    elif i1.get()=="shuvo" and i2.get()=="1234":
        messagebox.showinfo('Congrats','your id is : shuvo and password is : 1234')
    
    elif i1.get()!="shuvo" or i2.get()!="1234":
        messagebox.showinfo('Error','Please enter your correct username or password!')

frame1=Frame(scrn,height=480,width=760,bg='white')
frame1.place(x=150,y=100)

t1=Label(frame1,text='Member Login',font=('Arial',22),bg='white',fg='black')
t1.place(x=390,y=130)

def on_entry_click(event):
    if i1.get()=="Username":
        i1.delete(0,"end")
        i1.insert(0,'')
        i1.configure(fg="black")

def on_focusOut(event):
    if i1.get()=='':
        i1.insert(0,"Username")
        i1.configure(fg="grey")


def on_entry_click1(event):
    if i2.get()=="Password":
        i2.delete(0,"end")
        i2.insert(0,'')
        i2.configure(fg="black")

def on_focusOut1(event):
    if i2.get()=='':
        i2.insert(0,"Password")
        i2.configure(fg="grey")


i1=Entry(frame1,bg="white",fg='grey',font=('Arial',15),width=15)
i1.insert(0,'Username')
i1.place(x=405,y=190)
i1.bind('<FocusIn>',on_entry_click)
i1.bind('<FocusOut>',on_focusOut)

i2=Entry(frame1,bg="white",fg='grey',font=('Arial',15),width=15)
i2.insert(0,'Password')
i2.place(x=405,y=240)
i2.bind('<FocusIn>',on_entry_click1)
i2.bind('<FocusOut>',on_focusOut1)

img1= PhotoImage(file="4.png")

t=Label(frame1,image=img1,bg='white',bd=0)
t.place(x=50,y=70)

#img=PhotoImage(file="1.png")
b1=Button(frame1,text="login",font=('Arial',10,'bold'),bg='teal',bd=0,cursor='hand2',command=Page)
b1.place(x=435,y=280)

b2=Button(frame1,text="Forget password/UserName",font=('Arial',8),bg="white",fg='red',bd=0,cursor='hand2')
b2.place(x=420,y=350)