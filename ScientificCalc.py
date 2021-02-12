#Building Scientific Calculator Application
import math
from tkinter import *
root = Tk()
root.title("Scientific Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def btn_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def clr():
    e.delete(0, END)
    f_num = int(0)
    sign = None

def compute(s):
    first_num = e.get()
    global f_num
    global sign
    sign = s
    f_num = float(first_num)
    e.delete(0, END)
    
def sci_compute(sc):
    a = e.get()
    global s_num
    global sci_sign
    sci_sign = sc
    s_num = int(a)
    e.delete(0, END)
    
def facto(inp):
    if inp==0 or inp==1:
        f = int(1)
    elif inp < 0:
        f = "Nan"
    else:
        f = int(1)
        for i in range(1, inp+1):
            f = f*inp
            inp = inp - 1
    return f

def sin_x(t):
    x = float((t * math.pi)/180)
    nt = float(0)
    i = 1
    num = float(x)
    counter = 1
    sum = float(0)
    while True:
        f = facto(i)
        nt = float(num/f)
        
        if nt < pow(10,-5):
            break
        
        if counter % 2 == 0:
            nt = nt * (-1)
        
        sum = sum + nt
        i = i + 2
        counter = counter + 1
        num = num * pow(x, 2)    
    return sum

def cos_x(t):
    x = float((t * math.pi)/180)
    nt = float(0)
    i = 0
    num = float(1)
    counter = 1
    sum = float(0)
    while True:
        f = facto(i)
        nt = float(num/f)
        if nt < pow(10,-5):
            break
        if counter % 2 == 0:
            nt = nt * (-1)
        sum = sum + nt
        i = i + 2
        counter = counter + 1
        num = num * pow(x, 2)
    return sum

def tan_x(t):
    s = sin_x(t)
    c = cos_x(t)
    if t != 90:
        res = float(s / c)
    else:
        res = "Not defined"
    return res

def btn_equal():
    second_num = e.get()
    e.delete(0, END)
    if sign == "+" and second_num != "":
        e.insert(0, f_num + float(second_num))
    elif sign == "-" and second_num != "":
        e.insert(0, f_num - float(second_num))
    elif sign == "*" and second_num != "":
        e.insert(0, f_num * float(second_num))
    elif sign == "/" and second_num != "":
        if int(second_num) == int(0):
            e.insert(0, "Division by 0 not possible!")
        else:
            e.insert(0, float(f_num / float(second_num)))
    elif sign == "%" and second_num != "":
        try:
            e.insert(0, int(f_num) % int(second_num))
        except:
            e.insert(0, "Only Integer parameters are allowed for modulo operator")
    elif sign == "x^" and second_num != "":
        e.insert(0, pow(f_num, float(second_num)))
    elif sci_sign == "P" and second_num != "":
        if s_num >= int(second_num):
            a1 = facto(s_num)
            t = s_num - int(second_num)
            a2 = facto(t)
            e.insert(0, a1/a2)
        else:
            e.insert(0, "First number should be greater")
    elif sci_sign == "C" and second_num != "":
        if s_num >= int(second_num):
            a1 = facto(s_num)
            a2 = facto(int(second_num))
            t = s_num - int(second_num)
            a3 = facto(t)
            e.insert(0, a1/(a2 * a3))
        else:
            e.insert(0, "First number should be greater")
    elif sign == "sin" and second_num == "":
        e.insert(0, sin_x(f_num))
    elif sign == "cos" and second_num == "":
        e.insert(0, cos_x(f_num))
    elif sign == "tan" and second_num == "":
        e.insert(0, tan_x(f_num))
    else:
        if sign == "sqrt" and second_num == "":
            e.insert(0, pow(f_num, float(1/2)))
        elif sign == "cubrt" and second_num == "":
            e.insert(0, pow(f_num, float(1/3)))
        elif sign == "ln" and second_num == "":
            try:
                e.insert(0, math.log(f_num))
            except:
                e.insert(0, "Math error: Natural Log of 0")
        elif sci_sign == "!" and second_num == "":
            try:
                e.insert(0, facto(s_num))
            except:
                e.insert(0, "Only Integer parameters are allowed for factorial, no negative values")
        else:
            pass


#Define Buttons
b1 = Button(root, text="1", padx=40, pady=20, command= lambda :btn_click(1))
b2 = Button(root, text="2", padx=40, pady=20, command= lambda :btn_click(2))
b3 = Button(root, text="3", padx=40, pady=20, command= lambda :btn_click(3))
b4 = Button(root, text="4", padx=40, pady=20, command= lambda :btn_click(4))
b5 = Button(root, text="5", padx=40, pady=20, command= lambda :btn_click(5))
b6 = Button(root, text="6", padx=40, pady=20, command= lambda :btn_click(6))
b7 = Button(root, text="7", padx=40, pady=20, command= lambda :btn_click(7))
b8 = Button(root, text="8", padx=40, pady=20, command= lambda :btn_click(8))
b9 = Button(root, text="9", padx=40, pady=20, command= lambda :btn_click(9))
b0 = Button(root, text="0", padx=40, pady=20, command= lambda :btn_click(0))
add = Button(root, text="+", padx=39, pady=20, command= lambda :compute("+"))
equal = Button(root, text="=", padx=89, pady=20, command= btn_equal)
clear = Button(root, text="Clear", padx=78, pady=20, command=clr)
sub = Button(root, text="-", padx=42, pady=20, command= lambda :compute("-"))
mul = Button(root, text="*", padx=40, pady=20, command= lambda :compute("*"))
div = Button(root, text="/", padx=43, pady=20, command= lambda :compute("/"))
mod = Button(root, text="%", padx=40, pady=20, command= lambda :compute("%"))
pt = Button(root, text=".", padx=40, pady=20, command= lambda :btn_click("."))
power = Button(root, text="x^", padx=40, pady=20, command= lambda :compute("x^"))
sqrt = Button(root, text="sqrt", padx=49, pady=20, command= lambda :compute("sqrt"))
cubrt = Button(root, text="cube rt", padx=40, pady=20, command= lambda :compute("cubrt"))
natlog = Button(root, text="ln", padx=57, pady=20, command= lambda :compute("ln"))
fact = Button(root, text="!", padx=57, pady=20, command= lambda :sci_compute("!"))
permutation = Button(root, text="nPr", padx=40, pady=20, command= lambda :sci_compute("P"))
combination = Button(root, text="nCr", padx=40, pady=20, command= lambda :sci_compute("C"))
sinx = Button(root, text="Sin", padx=40, pady=20, command= lambda :compute("sin"))
cosx = Button(root, text="Cos", padx=40, pady=20, command= lambda :compute("cos"))
tanx = Button(root, text="Tan", padx=40, pady=20, command= lambda :compute("tan"))

#Put the buttons on the screen
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
tanx.grid(row=3,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
cosx.grid(row=2,column=3)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
sinx.grid(row=1,column=3)

b0.grid(row=4,column=0)
clear.grid(row=4,column=1,columnspan=2)
fact.grid(row=4,column=3)

add.grid(row=5,column=0)
equal.grid(row=5,column=1,columnspan=2)
natlog.grid(row=5,column=3)

sub.grid(row=6,column=0)
mul.grid(row=6,column=1)
div.grid(row=6,column=2)
sqrt.grid(row=6,column=3)

mod.grid(row=7,column=0)
pt.grid(row=7,column=1)
power.grid(row=7,column=2)
cubrt.grid(row=7,column=3)

permutation.grid(row=8,column=0)
combination.grid(row=8,column=1)

root.mainloop()
