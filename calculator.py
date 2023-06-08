from tkinter import*
root=Tk()
root.geometry("420x270+50+80")
root.resizable(True,True)
root.title("Calculator")
root.iconbitmap("C:\\Users\Shiwansh\\Downloads\\sasuke.ico")
root.config(bg="grey20")
def show(op):
    x=a.set(a.get()+op)
def eql():
    exp=a.get()
    a.set(eval(exp))
def clr():
    a.set(" ")
a = StringVar()
ent = Entry(root,borderwidth="5" ,justify = "right",font=("Ariel",20),textvariable = a)
ent.place(x=0 , y=0, width = 420, height = 48)

b1 = Button(root,borderwidth="5" ,text = "1",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b1.place(x=5, y=156 ,width = 100, height = 50 )
b1.configure(command = lambda:show("1"))

b2 = Button(root,borderwidth="5" , text = "2",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b2.place(x=108, y=156 ,width = 100, height = 50 )
b2.configure(command = lambda:show("2"))

b3 = Button(root, borderwidth="5" ,text = "3",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b3.place(x=211, y=156 ,width = 100, height = 50 )
b3.configure(command = lambda:show("3"))

b4 = Button(root,borderwidth="5" , text = "4",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b4.place(x=5, y=103 ,width = 100, height = 50 )
b4.configure(command = lambda:show("4"))

b5 = Button(root,borderwidth="5" , text = "5",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b5.place(x=108, y=103 ,width = 100, height = 50 )
b5.configure(command = lambda:show("5"))

b6 = Button(root,borderwidth="5" , text = "6",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b6.place(x=211, y=103 ,width = 100, height = 50 )
b6.configure(command = lambda:show("6"))

b7 = Button(root,borderwidth="5" , text = "7",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b7.place(x=5, y=50 ,width = 100, height = 50 )
b7.configure(command = lambda:show("8"))

b8 = Button(root,borderwidth="5" , text = "8",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b8.place(x=108, y=50 ,width = 100, height = 50 )
b8.configure(command = lambda:show("8"))

b9 = Button(root,borderwidth="5" , text = "9",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b9.place(x=211, y=50 ,width = 100, height = 50 )
b9.configure(command = lambda:show("9"))

ba = Button(root,borderwidth="5" , text = "+",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
ba.place(x=314, y=50 ,width = 100, height = 50 )
ba.configure(command = lambda:show("+"))

bs = Button(root,borderwidth="5" ,text = "-",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
bs.place(x=314, y=103 ,width = 100, height = 50 )
bs.configure(command = lambda:show("-"))

bd = Button(root,borderwidth="5" , text = "/",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
bd.place(x=314, y=156 ,width = 100, height = 50 )
bd.configure(command = lambda:show("/"))

bc = Button(root,borderwidth="5" , text = "C",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
bc.place(x=5, y=209 ,width = 100, height = 50 )
bc.configure(command = lambda:clr())

b0 = Button(root,borderwidth="5" , text = "0",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
b0.place(x=108, y=209 ,width = 100, height = 50 )
b0.configure(command = lambda:show("0"))

beq = Button(root,borderwidth="5" , text = "=",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
beq.place(x=211, y=209 ,width = 100, height = 50 )
beq.configure(command = lambda:eql())

bm = Button(root, borderwidth="5" ,text = "x",justify = "right", font = ("Arial",20),fg ="white",bg="gray")
bm.place(x=314, y=209 ,width = 100, height = 50 )
bm.configure(command = lambda:show("*"))

root.mainloop()


