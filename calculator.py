import tkinter
from tkinter import *

""" Header    """
#Table Heading For the Simple CalCulator

root=Tk()
root.title("CALCULATOR")
root.geometry("600x600+100+200")
root.resizable(False,False)
root.configure(bg="white")

""" Function for the calculation """
equation = ""
#Display values in the terminal box
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
#Clear the valuesfrom the boxx
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)  
      
#Calcuatiom for the Values
def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result ="error"
            equation = ""
    label_result.config(text=result)
        
""" Top Body  """
label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

""" Body 1st ROW """

Button(root,text="C",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#00EEEE", command=lambda: clear()).place(x=10,y=110)
Button(root,text="/",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("/")).place(x=160,y=110)
Button(root,text="%",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("%")).place(x=310,y=110)
Button(root,text="*",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("*")).place(x=460,y=110)

""" Body 2nd ROW """

Button(root,text="7",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("7")).place(x=10,y=210)
Button(root,text="8",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("8")).place(x=160,y=210)
Button(root,text="9",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("9")).place(x=310,y=210)
Button(root,text="-",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("-")).place(x=460,y=210)

""" Body 3nd ROW """

Button(root,text="4",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("4")).place(x=10,y=310)
Button(root,text="5",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("5")).place(x=160,y=310)
Button(root,text="6",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("6")).place(x=310,y=310)
Button(root,text="+",width=5, height=1, font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("+")).place(x=460,y=310)

""" Body 4nd ROW """

Button(root,text="1",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("1")).place(x=10,y=410)
Button(root,text="2",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("2")).place(x=160,y=410)
Button(root,text="3",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("3")).place(x=310,y=410)
Button(root,text="=",width=5, height=3,font=("arial",30,"bold"),bd=1, fg="#fff", bg="red", command=lambda: calculate()).place(x=460,y=410)

""" Body 4nd ROW """

Button(root,text="0",width=11, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show("0")).place(x=10,y=510)
Button(root,text=".",width=5, height=1,font=("arial",30,"bold"),bd=1, fg="#fff", bg="#5B5B5B", command=lambda: show(".")).place(x=310,y=510)


root.mainloop()