from tkinter import *
from tkinter.messagebox import showinfo


class MyGui:
    def __init__(self):
        self.myWindow = Tk()
        self.myWindow.geometry("500x300+100+100")
        self.myWindow.title("Temperature Checker")
        self.frame = Frame(self.myWindow, width=500, height=300, background="white")
        self.frame.place(x=10, y=10)

        self.actualTemp = IntVar()
        self.actualTemp.set(20)
        self.targetTemp = IntVar()
        self.targetTemp.set(20)

        # Actual Temperature
        self.label = Label(self.frame, text="Actual temperature: ", background="white", foreground="black", font=('Arial', 20))
        self.label.place(x=10, y=40)
        self.entry = Entry(self.frame, textvariable=self.actualTemp)
        self.entry.place(x=280, y=40)
        #Target Temperature
        self.label = Label(self.frame, text="Target temperature: ", background="white", foreground="black", font=('Arial', 20))
        self.label.place(x=10, y=100)

        self.entry = Entry(self.frame, textvariable=self.targetTemp)
        self.entry.place(x=280, y=100)

        self.submitButton = Button(self.frame, text="Submit", command=self.submit)

        mainloop()

    def submit(self):




if __name__ == "__main__":
    my_gui = MyGui()
