from tkinter import *
from tkinter.messagebox import showinfo
# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)		#red button
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)	#blue button


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
        self.label1 = Label(self.frame, text="Actual temperature: ", background="white", foreground="black", font=('Arial', 20))
        self.label1.place(x=10, y=40)
        self.entry1 = Entry(self.frame, textvariable=self.actualTemp)
        self.entry1.place(x=280, y=40)
        #Target Temperature
        self.label2 = Label(self.frame, text="Target temperature: ", background="white", foreground="black", font=('Arial', 20))
        self.label2.place(x=10, y=100)

        self.entry2 = Entry(self.frame, textvariable=self.targetTemp)
        self.entry2.place(x=280, y=100)

        self.submitButton = Button(self.frame, text="Submit", command=self.submit)
        self.submitButton.place(x=350, y=100)

    def increaseTemp(self, channel):
        print("called increaseTemp, channel=", channel)
        if(self.myWindow.focus_get() == self.entry1):
            self.actualTemp.set(self.actualTemp.get()+1)
        elif (self.myWindow.focus_get() == self.entry2):
            self.targetTemp.set(self.targetTemp.get() + 1)

    def decreaseTemp(self, channel):
        print("called decreaseemp, channel=", channel)
        if (self.myWindow.focus_get() == self.entry1):
            self.actualTemp.set(self.actualTemp.get() - 1)
        elif (self.myWindow.focus_get() == self.entry2):
            self.targetTemp.set(self.targetTemp.get() - 1)

    def submit(self):
        pass


if __name__ == "__main__":
    my_gui = MyGui()
    GPIO.add_event_detect(5, GPIO.FALLING, callback=my_gui.increaseTemp, bouncetime=200)
    GPIO.add_event_detect(12, GPIO.FALLING, callback=my_gui.decreaseTemp, bouncetime=200)
    mainloop()

