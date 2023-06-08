from tkinter import*
from tkinter import ttk
import openpyxl
from openpyxl import workbook
#from tkinter import messagebox

root=Tk()
root.geometry("1400x700+50+50")
root.resizable(1,1)
root.title("Coursera(Signup page)")
root.iconbitmap("C:\\Users\\Shiwansh\\Downloads\\coursera-logo.ico")#location of your icon image.
root.config(bg="grey17")

"""Labeling"""
#page title

lbl=Label(root,text="Signup Coursera", font=('gadugi',20,'bold'),fg="white",bg="grey17")
lbl.place(x="670",y="185",width="250",height="100")

#user inputs
lbl1=Label(root,text="Username:",borderwidth="4", font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl1.place(x="150",y="345")

#user password
lbl11=Label(root,text="Password:", borderwidth="4",font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl11.place(x="150",y="445")
#select your gender gender
lbl12=Label(root,text="Select your gender", borderwidth="4",font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl12.place(x="668",y="332")
#Select your langauge
lbl12=Label(root,text="Select your langauage", borderwidth="4",font=('gadugi',20,'bold'),fg="white",bg="grey18")
lbl12.place(x="1005",y="330")
#line
"""1st line"""
lbl13=Label(root,borderwidth="4", font=('gadugi',20,'bold'),bg="grey28")
lbl13.place(x="600",y="310",width="2",height="245")
"""2nd line"""
lbl131=Label(root,borderwidth="4", font=('gadugi',20,'bold'),bg="grey28")
lbl131.place(x="980",y="310",width="2",height="245")


"""functons-1"""
def opt():
    if v0.get()==1:
        #st=st+v0.get()
        lbl=Label(root,text="Your option is:  Male  ")
        lbl.place(x="668",y="480")
    if v0.get()==2:
        #st=st+v0.get()
        lbl=Label(root,text="your option is: Female")
        lbl.place(x="668",y="480")

"""Entry"""
nm= StringVar()
ent=Entry(root,borderwidth="8",font=("Ariel",20),fg="black",bg="silver",textvariable=nm)
ent.place(x="305",y="346",width="200",height="50")

ps= StringVar()
ent1=Entry(root,borderwidth="8",font=("Ariel",20),fg="black",bg="silver",show="*",textvariable=ps)
ent1.place(x="305",y="446",width="200",height="50")

"""checkbutton"""
ja=IntVar()
py=IntVar()
cc=IntVar()
c=StringVar()

ja.set(0)
py.set(0)
cc.set(0)

def show1():
    st=" "
    if ja.get()==1:
        st+="Java, "
    if py.get()==1:
        st+="Python, "
    if cc.get()==1:
        st+="C++"
    c.set(st)
ent2=Entry(root,borderwidth="7",textvariable=c)
ent2.place(x="1010",y="385",width="200",height="50")


chk=Checkbutton(root,text="java",fg="black",bg="silver",borderwidth="7",variable=ja)
chk.place(x="1010",y="437",width="100",height="50")

chk1=Checkbutton(root,text="python",fg="black",bg="silver",borderwidth="7",variable=py)
chk1.place(x="1110",y="437",width="100",height="50")

chk2=Checkbutton(root,text="c++",fg="black",bg="silver",borderwidth="7",variable=cc)
chk2.place(x="1210",y="437",width="100",height="50")

bt= Button(root,text="click",borderwidth="7",font=("Ariel",20),activebackground="white",bg="grey",fg="black",command=show1)
bt.place(x="1010",y="490",width="100",height="50")


#radiobutton-
"""male option button"""
v0=IntVar()
rad = Radiobutton(root,text="Male",value=1,borderwidth="7",variable=v0,fg="whitesmoke",bg="grey19",command=opt)
rad.place(x="673",y="385",width="100",height="50")
"""female option button"""
rad1= Radiobutton(root,text="Female",value=2,borderwidth="7",variable=v0,fg="whitesmoke",bg="grey19",command=opt)
rad1.place(x="673",y="437",width="100",height="50")
"""connecting to excel sheet file"""
wb=openpyxl.load_workbook("C:\\Users\\Shiwansh\\OneDrive\\Desktop\\registration.xlsx")#location of your excel file.
sheet=wb.active
"""function"""
def sign():
    na=nm.get()
    pa=ps.get()
    ge=v0.get()
    l1=ja.get()
    l2=py.get()
    l3=cc.get()
    lst=[na,pa,ge,l1,l2,l3]
    sheet.append(lst)
    wb.save("C:\\Users\\Shiwansh\\OneDrive\\Desktop\\registration.xlsx")#location of your excel file.
    di=Label(root,borderwidth="7",text="SignIn Sucessful!")
    di.place(x="745",y="690")

"""signin buttons"""
but=Button(root,text="Signin",borderwidth="8",font=("Ariel",20),activebackground="white",bg="grey",fg="black",command=sign)
but.place(x="740",y="600",width=100,height=50)

"""CANVAS"""
can=Canvas(root,width="2000",height="200",bg="Dodgerblue4")
can.grid(row="0",column="0")
can.create_text("780","100",font=("bold italic",90),text="WELCOME",fill="grey19")

"""MENU"""
dmenu=Menu(root)
sub1=Menu(dmenu,tearoff="0")
sub2=Menu(dmenu,tearoff="0")

sub1.add_command(label="reload")
sub1.add_command(label="reviews")
sub1.add_command(label="help")

sub1.add_command(label="exit")
dmenu.add_cascade(label="file",menu=sub1)

sub2.add_command(label="reference")
sub2.add_command(label="FAQs")
sub2.add_command(label="contact us")
sub2.add_command(label="langauage")
dmenu.add_cascade(label="options",menu=sub2)
root.config(menu=dmenu)

"""combobox"""
lst=["Log In"]
comb=ttk.Combobox(root,value=lst)
comb.set("Already sign In?")
comb.place(x="740",y="652")

root.mainloop()
