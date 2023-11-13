from tkinter import *
from tkinter.messagebox import showinfo


class MyGui:
    def __init__(self):
        self.myWindow = Tk()
        self.myWindow.geometry("300x300+100+100")
        self.myWindow.title("Bro fix your broke ass car!")
        self.frame = Frame(self.myWindow, width=300, height=300)
        self.frame.place(x=10, y=10)
        self.choice1 = IntVar()
        self.choice2 = IntVar()
        self.choice3 = IntVar()
        self.choice4 = IntVar()
        self.totalText = StringVar()
        self.choice1.set(0)
        self.choice2.set(0)
        self.choice3.set(0)
        self.choice4.set(0)

        self.total = 0

        self.cb1 = Checkbutton(self.frame, text="Oil Change", font=14, variable=self.choice1, command=self.do_this)
        self.cb1.place(x=20, y=40)

        self.cb2 = Checkbutton(self.frame, text="Inspection", font=14, variable=self.choice2, command=self.do_this)
        self.cb2.place(x=20, y=70)

        self.cb3 = Checkbutton(self.frame, text="Muffler replacement", font=14, variable=self.choice3,
                               command=self.do_this)
        self.cb3.place(x=20, y=110)

        self.cb4 = Checkbutton(self.frame, text="Tire Rotation", font=14, variable=self.choice4, command=self.do_this)
        self.cb4.place(x=20, y=140)

        self.totalChargeButton = Button(self.frame, text="Calculate the total", font=14, command=self.do_this)
        self.totalChargeButton.place(x=20, y=170)

        self.totalText.set("Total Charge: ")

        self.totalLabel = Label(self.frame, textvariable=self.totalText, font=14)
        self.totalLabel.place(x=20, y=200)
        mainloop()

    def do_this(self):
        self.total = 0
        print(self.choice1)
        print(dir(self.choice1))

        print(self.choice2.get())
        print(self.choice1.get())
        if self.choice1.get():
            self.total += 35
        if self.choice2.get():
            self.total += 50
        if self.choice3.get():
            self.total += 100
        if self.choice4.get():
            self.total += 20
        self.totalText.set("Total Charge: " + str(self.total))
        showinfo("Total", "Total Charge: " + str(self.total))


if __name__ == "__main__":
    my_gui = MyGui()
