from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import sqlite3 as sql

def valid():
    try:
        con=sql.connect("databases/db.sqlite3")
        cur=con.cursor()
        data=cur.execute("select * from login_auth")
        uid=e1.get()
        passwd=e2.get()
        e1.delete(0,END)
        e2.delete(0,END)
    except con.Error:
        print("error..")
    else:
        #usnms=[d[0] for d in data]
        if (uid,passwd) in data:
            messagebox.showinfo("welcome","successful login!")
        else:
            messagebox.showerror("invalid login","either credentials are wrong or you have not registered.")
    finally:
        cur.close()
        con.close()

root=Tk()
root.geometry("500x500")
root.title("authorizing entry")
l1=Label(root,text="username: ")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="password: ")
l2.grid(row=1,column=0)
e2=Entry(root,show="*")
e2.grid(row=1,column=1)
btn=Button(root,text="login",command=valid)
btn.grid(row=2,column=0)
root.mainloop()