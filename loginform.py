from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import openpyxl
from openpyxl import workbook
root=Tk()
root.geometry("1400x700+50+50")
root.resizable(1,1)
root.title("Coursera(Login page)")
root.iconbitmap("C:\\Users\\Shiwansh\\Downloads\\coursera-logo.ico")
root.config(bg="grey17")


#Labeling
"""page title"""
lbl=Label(root,text="LogIn Coursera", borderwidth="10",font=('gadugi',20,'bold'),fg="white",bg="dodgerblue4")
lbl.place(x="690",y="215",width="300",height="100")
#user inputs
lbl1=Label(root,text="Username:",borderwidth="4", font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl1.place(x="600",y="345")
#user password
lbl11=Label(root,text="Password:", borderwidth="4",font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl11.place(x="600",y="445")
#line
"""leftline"""
lb112=Label(root,bg="grey24")
lb112.place(x="550",y="330",width="2",height="299")
"""rightline"""
lb1121=Label(root,bg="grey24")
lb1121.place(x="1110",y="327",width="2",height="300")
"""upperline"""
lbl11212=Label(root,bg="grey24")
lbl11212.place(x="550",y="327",width="560",height="2")
"""bottomline"""
lbl112122=Label(root,bg="grey24")
lbl112122.place(x="550",y="627",width="560",height="2")

"""functions"""
def log():
    user=a.get()
    pas=b.get()
    file=openpyxl.load_workbook("C:\\Users\\Shiwansh\\OneDrive\\Desktop\\registration.xlsx")
    sheet=file.active
    for row in sheet.rows:
        f=0
        if (row[0].value==str(user))and (row[1].value==pas):
            f=1
            break
        else:
            f=0

    if f==1:
        messagebox.showinfo("Login Sucessfully")
    else:
        messagebox.showinfo("Incorrect username or password")
    a.set()
    b.set()


#Entry
"""usernamentry"""
a= StringVar()
ent=Entry(root,borderwidth="8",font=("Ariel",20),fg="black",bg="silver",textvariable=a)
ent.place(x="750",y="346",width="200",height="50")
"""passwordentry"""
b= StringVar()
ent1=Entry(root,borderwidth="8",font=("Ariel",20),fg="black",bg="silver",show="*",textvariable=b)
ent1.place(x="750",y="446",width="200",height="50")

#Buttons
""" loginButtons"""
but=Button(root,text="Login",font=("Ariel",20),activebackground="white",bg="grey",fg="black",command=log)
but.place(x=800,y=530,width=100,height=50)

#CANVAS
"""upperstrip"""
can=Canvas(root,width="2000",height="200",bg="Dodgerblue4")
can.grid(row="0",column="0")
can.create_text("780","100",font=("bold italic",90),text="WELCOME",fill="grey19")

#MENU
dmenu=Menu(root)
sub1=Menu(dmenu,tearoff="0")
sub2=Menu(dmenu,tearoff="0")
"""File menu"""
sub1.add_command(label="reload")
sub1.add_command(label="reviews")
sub1.add_command(label="help")
sub1.add_separator()
sub1.add_command(label="exit")
dmenu.add_cascade(label="file",menu=sub1)
"""option menu"""
sub2.add_command(label="reference")
sub2.add_command(label="FAQs")
sub2.add_command(label="contact us")
sub2.add_command(label="open new tab")
dmenu.add_cascade(label="options",menu=sub2)
root.config(menu=dmenu)

root.mainloop()
