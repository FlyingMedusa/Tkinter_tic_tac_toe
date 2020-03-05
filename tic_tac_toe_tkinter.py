from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

p1 = StringVar()
p2 = StringVar()

p1_name = Entry(tk, textvariable=p1, bd=5)
p1_name.grid(row=1, column=0)
p2_name = Entry(tk, textvariable=p2, bd=5)
p2_name.grid(row=1, column=2)

click = True


def checker(buttons):
    global click, p1_name, p2_name
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
    elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
    button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
    button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
    button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
    button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
    button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
    button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
    button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("It's a win!", "1st player, " + p1_name.get() + " You have just won the game")
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
    button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
    button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
    button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
    button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
    button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
    button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
    button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("It's a win!", "2nd player, " + p2_name.get() + " You have just won the game")


buttons = StringVar()

label = Label( tk, text="First player:", font='Times 17 bold', fg='black', height=1, width=10)
label.grid(row=0, column=0)


label = Label( tk, text="Second player:", font='Times 17 bold', fg='black', height=1, width=10)
label.grid(row=0, column=2)

button1 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button1))
button1.grid(row=2, column=0, sticky=S+N+E+W)

button2 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button2))
button2.grid(row=2, column=1, sticky=S+N+E+W)

button3 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button3))
button3.grid(row=2, column=2, sticky=S+N+E+W)

button4 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button4))
button4.grid(row=3, column=0, sticky=S+N+E+W)

button5 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button5))
button5.grid(row=3, column=1, sticky=S+N+E+W)

button6 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button6))
button6.grid(row=3, column=2, sticky=S+N+E+W)

button7 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button7))
button7.grid(row=4, column=0, sticky=S+N+E+W)

button8 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button8))
button8.grid(row=4, column=1, sticky=S+N+E+W)

button9 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8,
                 command=lambda: checker(button9))
button9.grid(row=4, column=2, sticky=S+N+E+W)

tk.mainloop()
