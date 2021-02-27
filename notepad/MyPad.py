from tkinter import*
from tkinter import filedialog
from tkinter import scrolledtext 

scrn=Tk()
scrn.geometry('600x650')
scrn.title('PadPro')
scrn.resizable(0,1)

def save_file():
    print('saving mode')
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    text=str(t.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    print('file opening')
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    c=file.read()
    t.insert(INSERT,c)

def clear_all():
    print('file clear')
    t.delete(1.0,END)
    
def Exit():
    print('File closed!')
    scrn.destroy()

b1=Button(scrn,text="Save File",font=('Arial',10),fg='#330019',bd=0,cursor='hand2',command=save_file)
b1.place(x=20,y=20)

b2=Button(scrn,text="Open File",font=('Arial',10),fg='#330019',bd=0,cursor='hand2',command=open_file)
b2.place(x=100,y=20)

b3=Button(scrn,text="Clear All",font=('Arial',10),fg='#330019',bd=0,cursor='hand2',command=clear_all)
b3.place(x=180,y=20)

b4=Button(scrn,text="Exit ?",font=('Arial',10,'bold'),cursor='hand2',fg='white',bg='red',command=Exit)
b4.place(x=540,y=20)

t=scrolledtext.ScrolledText(scrn,width=92,height=40,bg='white',fg='black',font=('Arial',12),wrap=WORD)
t.place(x=5,y=60)

scrn.mainloop()