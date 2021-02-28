from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("320x324")
root.resizable(0,0)

expression=""

def btn_click(num):
    global expression
    expression=expression+num
    input_text.set(expression)

def vl_clear():
    global expression
    expression=" "
    input_text.set(" ")

def vl_equal():
    global expression
    result=str(eval(expression)) #result is string type
    input_text.set(result)
    expression=""


#input_frame
#takes input data
input_frame=Frame(root,width=312,height=60,bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_text=StringVar()

input_field=Entry(input_frame, textvariable=input_text, width=50, font=("arial",16, "bold"),bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=Frame(root,width=312,height=272.5,bg="white")
btn_frame.pack()

#first_row
#buttons
clear=Button(btn_frame,text="Clear",fg="black",width=34,height=3,bd=0,bg="#eee",command=lambda:vl_clear())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide=Button(btn_frame,text="/",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:btn_click("/"))
divide.grid(row=0,column=3,padx=1,pady=1)

#second row
seven=Button(btn_frame,text="7",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("7"))
seven.grid(row=1,column=0,padx=1,pady=1)

eight=Button(btn_frame,text="8",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("8"))
eight.grid(row=1,column=1,padx=1,pady=1)

nine=Button(btn_frame,text="9",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("9"))
nine.grid(row=1,column=2,padx=1,pady=1)

multiply=Button(btn_frame,text="x",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:btn_click("*"))
multiply.grid(row=1,column=3,padx=1,pady=1)

#third row

four=Button(btn_frame,text="4",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("4"))
four.grid(row=2,column=0,padx=1,pady=1)

five=Button(btn_frame,text="5",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("5"))
five.grid(row=2,column=1,padx=1,pady=1)

six=Button(btn_frame,text="6",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("6"))
six.grid(row=2,column=2,padx=1,pady=1)

minus=Button(btn_frame,text="-",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:btn_click("-"))
minus.grid(row=2,column=3,padx=1,pady=1)

#fourth row

one=Button(btn_frame,text="1",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("1"))
one.grid(row=3,column=0,padx=1,pady=1)

two=Button(btn_frame,text="2",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("2"))
two.grid(row=3,column=1,padx=1,pady=1)

three=Button(btn_frame,text="3",fg="black",width=10,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("3"))
three.grid(row=3,column=2,padx=1,pady=1)

plus=Button(btn_frame,text="+",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:btn_click("+"))
plus.grid(row=3,column=3,padx=1,pady=1)

#fifth row

zero=Button(btn_frame,text="0",fg="black",width=22,height=3, bd = 0, bg = "#fff",command=lambda:btn_click("0"))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)

point=Button(btn_frame,text=".",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:btn_click("."))
point.grid(row=4,column=2,padx=1,pady=1)

equal=Button(btn_frame,text="=",fg="black",width=10,height=3, bd = 0, bg = "#eee",command=lambda:vl_equal())
equal.grid(row=4,column=3,padx=1,pady=1)


mainloop()

