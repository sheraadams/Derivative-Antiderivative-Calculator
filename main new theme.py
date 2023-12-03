from tkinter import*
import math
import random
import math
import tkinter as tk
from PIL import Image, ImageTk
import time

def calculus():
    if __name__ == '__main__':
        command = "menu"

        def derivative():
            x = int(input("If value is x^n, Enter value for coefficient of x:"))
            n = int(input("If value is x^n, Enter value for n:"))
            coefficient = n * x
            power = n - 1
            print("Derivative of", x, "x^", n, ":")
            print(coefficient, "x^", power, "\n")

        def antiderivative():
            x = int(input("If value is x^n, Enter value for x:"))
            n = int(input("If value is x^n, Enter value for n:"))
            power = n + 1
            print("Antiderivative of", x, "x^", n, ":")
            print(x, "/", (n + 1), "x^", power, "+ C")
            q = input("simplify fraction?")
            if q == "yes":
                print(x, "/", n + 1, "=", x / (n + 1), "\n")

# GUI window defined
#colors
bg_color = "#1c1b1f"   # dark slate
text_color = "#000000"   # black or  "#6200EE"   purple
box_color = "#03DAC5"   # teal
purple = "#BB86FC"  # lavender
button_color = "#BB86FC"

window = Tk(className= "Derivative and Antiderivative Calculator")
window.configure(bg= bg_color, padx=180, pady=60)
window.geometry("880x508")

def calc():
    # Derivative calculation
    coefficient = float(c1_value.get()) * float(p1_value.get())
    x = 'x'
    power = float(p1_value.get()) - 1

    # Antiderivative calculation
    power2 = float(p2_value.get()) + 1
    coefficient2 = float(c2_value.get()) / power2

    # display calculated values to ui
    t1.delete("1.0", END)
    t1.insert(END, coefficient)
    t2.delete("1.0", END)
    t2.insert(END, x)
    t3.delete("1.0", END)
    t3.insert(END, power)
    t4.delete("1.0", END)
    t4.insert(END, coefficient2)
    t5.delete("1.0", END)
    t5.insert(END, x)
    t6.delete("1.0", END)
    t6.insert(END, power2)

# Derivative Calculator and Labels
l1= Label(window, bg= bg_color,  fg=purple, text='Derivative Calculator',font='Helvetica 11 bold')
l2= Label(window, bg= bg_color,  fg=box_color, text='Coefficient of X')
l3= Label(window, bg= bg_color,  fg=box_color,text='Power')
l4 = Label(window, bg= bg_color,  fg=box_color, text="Enter coefficient of x, power:",font='Helvetica 9 bold')

# Derivative Calculator Entry
c1_value = StringVar(window, value='0')
c1 = Entry(window, bg= box_color, fg= text_color, textvariable=c1_value)
p1_value = StringVar(window, value='0')
p1 = Entry(window, bg= box_color,  fg=text_color, textvariable=p1_value)

# Label Coefficient, x, power
r1 = Label(window, bg= bg_color,  fg=box_color, text='Coefficient')
r2 = Label(window, bg= bg_color,  fg=box_color, text='x^')
r3 = Label(window, bg= bg_color,  fg=box_color, text='Power')

# Widget to display Calculated derivative values
t1 = Text(window, bg= box_color,  fg=text_color, height=1, width=20)
t2 = Text(window, bg= box_color,  fg=text_color, height=1, width=20)
t3 = Text(window, bg= box_color,  fg=text_color, height=1, width=20)

# Space between Calcs
s0 = Label(window, bg= bg_color,  fg=box_color, text='')
s1 = Label(window, bg= bg_color,  fg=box_color, text='')
s2 = Label(window, bg= bg_color,  fg=box_color, text='')
s3 = Label(window, bg= bg_color,  fg=box_color, text='')

# Antiderivative Calculator and labels
l5= Label(window, bg= bg_color,  fg=purple, text='Antiderivative Calculator',font='Helvetica 11 bold')
l6= Label(window, bg= bg_color,  fg=box_color, text='Coefficient of X')
l7= Label(window, bg= bg_color,  fg=box_color, text='Power')
l8 = Label(window, bg= bg_color,  fg=box_color, text="Enter coefficient of x, power:",font='Helvetica 9 bold')

# Antidervative Calc Entry
c2_value = StringVar(window, value='0')
c2 = Entry(window, bg= box_color,  fg=text_color, textvariable=c2_value)
p2_value = StringVar(window, value='0')
p2 = Entry(window, bg= box_color,  fg=text_color, textvariable=p2_value)

# Label Coefficient, x, power
r4 = Label(window,bg= bg_color,  fg=box_color, text='Coefficient')
r5 = Label(window,bg= bg_color,  fg=box_color, text='x^')
r6 = Label(window, bg= bg_color,  fg=box_color, text='Power')

# Widget to display Calculated antiderivative values
t4 = Text(window, bg= box_color,  fg=bg_color, height=1, width=20)
t5 = Text(window, bg= box_color,  fg=bg_color, height=1, width=20)
t6 = Text(window, bg= box_color,  fg=bg_color, height=1, width=20)

# Button Widgets Calculate
b1 = Button(window,bg= button_color,  fg=bg_color, text="Calculate", command=calc)
b2 = Button(window, bg= button_color,  fg=bg_color, text="Calculate", command=calc)
b3 = Button(window, bg= button_color,  fg=bg_color, text="Launch")

# Grid
# Row 0: Label Derivative
l1.grid(row=0, column=1)

# Row 1: Label Coefficient x, power
l2.grid(row=1, column=1)
l3.grid(row=1, column=2)
l4.grid(row=2, column=0)

# Row 2: Text entry for coefficient and power
c1.grid(row=2, column=1)
p1.grid(row=2, column=2)

# Row 3: Label Coefficient, x, power
r1.grid(row=3, column=0)
r2.grid(row=3, column=1)
r3.grid(row=3, column=2)

# Row 4: Widget to display Calculated derivative values
t1.grid(row=4, column=0)
t2.grid(row=4, column=1)
t3.grid(row=4, column=2)
# Add Spacing
s0.grid(row=5, column= 1)

# Calculate Derivative button
b1.grid(row=6, column=1)
s1.grid(row=7, column=1)

# Row 6: Label Antierivative
l5.grid(row=8, column=1)

# Row 7: Label Coefficient x, power
l6.grid(row=9, column=1)
l7.grid(row=9, column=2)
l8.grid(row=10, column=0)

# Row 8: Text entry for coefficient and power
c2.grid(row=10, column=1)
p2.grid(row=10, column=2)

# Row 9: Label Coefficient, x, power
r4.grid(row=11, column=0)
r5.grid(row=11, column=1)
r6.grid(row=11, column=2)

# Row 10: Widget to display Calculated antiderivative values
t4.grid(row=12, column=0)
t5.grid(row=12, column=1)
t6.grid(row=12, column=2)

# Add Spacing
s2.grid(row=13, column=1)

# Calculate Antierivative button
b2.grid(row=14, column=1)
# Add Spacing
s3.grid(row=15, column=1)

# Launch Button
b3.grid(row=16, column=1)

# Start the GUI
window.mainloop()

# TODO: Create launch new window
