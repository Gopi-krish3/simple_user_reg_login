from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import sqlite3 as sql

con=None

def encrypt(st):
    from hashlib import sha256
    s=sha256(st.encode())
    b=s.hexdigest()
    return b

def connect():
    global con
    if con==None:
        con=sql.connect("databases/db.sqlite3")
        print("connection created")
        btn.config(state=NORMAL)

def register():
    global con
    try:
        cur=con.cursor()
        data=cur.execute("select * from login_auth")
        uid=e1.get()
        passwd=e2.get()
        e1.delete(0,END)
        e2.delete(0,END)
    except con.Error:
        print("error..")
    else:
        i=[j[0] for j in data]
        finpass=encrypt(passwd)
        if uid=="" or passwd=="" or len(str(passwd))<4:
            messagebox.showerror("credential error","enter all the credentials")
        elif uid in i:
            messagebox.showerror("invalid","username already present!")
        else:
            st=f"insert into login_auth values('{uid}','{finpass}')"
            cur.execute(st)
            print("record entered..")
            messagebox.showinfo("success","successfully registered.")
    finally:
        cur.close()
        con.commit()

def disconnect():
    global con
    if con!=None:
        con.close()
        print("connection closed..")
        con=None
        btn.config(state=DISABLED)
    else:
        pass

root=Tk()
root.geometry("500x500")
root.title("authorizing entry")
l1=Label(root,text="username")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="password")
l2.grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)
btn1=Button(root,text="connect",command=connect)
btn1.grid(row=2,column=0)
btn=Button(root,text="register",command=register,state=DISABLED)
btn.grid(row=2,column=1)
btn2=Button(root,text="disconnect",command=disconnect)
btn2.grid(row=2,column=2)
root.mainloop()