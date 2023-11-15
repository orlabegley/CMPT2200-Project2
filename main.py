from tkinter import *
from tkinter.messagebox import showinfo
# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

seg2A = 4
seg2B = 2
seg2C = 14
seg2D = 15
seg2E = 23
seg2F = 27
seg2G = 22
seg1A = 9
seg1B = 10
seg1C = 24
seg1D = 25
seg1E = 8
seg1F = 11
seg1G = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(seg1A, GPIO.OUT)
GPIO.setup(seg1B, GPIO.OUT)
GPIO.setup(seg1C, GPIO.OUT)
GPIO.setup(seg1D, GPIO.OUT)
GPIO.setup(seg1E, GPIO.OUT)
GPIO.setup(seg1F, GPIO.OUT)
GPIO.setup(seg1G, GPIO.OUT)
GPIO.setup(seg2A, GPIO.OUT)
GPIO.setup(seg2B, GPIO.OUT)
GPIO.setup(seg2C, GPIO.OUT)
GPIO.setup(seg2D, GPIO.OUT)
GPIO.setup(seg2E, GPIO.OUT)
GPIO.setup(seg2F, GPIO.OUT)
GPIO.setup(seg2G, GPIO.OUT)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # red button
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # blue button

LEDblue=19
LEDred=26
LEDgreen=16
GPIO.setup(LEDblue,GPIO.OUT)
GPIO.setup(LEDred,GPIO.OUT)
GPIO.setup(LEDgreen,GPIO.OUT)

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
        self.label1 = Label(self.frame, text="Actual temperature: ", background="white", foreground="black",
                            font=('Arial', 20))
        self.label1.place(x=10, y=40)
        self.entry1 = Entry(self.frame, textvariable=self.actualTemp)
        self.entry1.place(x=280, y=40)

        # Target Temperature
        self.label2 = Label(self.frame, text="Target temperature: ", background="white", foreground="black",
                            font=('Arial', 20))
        self.label2.place(x=10, y=100)
        self.entry2 = Entry(self.frame, textvariable=self.targetTemp)
        self.entry2.place(x=280, y=100)

        self.submitButton = Button(self.frame, text="Submit", command=self.submit)
        self.submitButton.place(x=50, y=200)

        self.quitButton = Button(self.frame, text="Quit", command=self.myWindow.destroy)
        self.quitButton.place(x=150, y=200)

    def writeTens(self, number):
        if number == 0:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, True)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, False)  # G

        elif number == 1:
            GPIO.output(seg1A, False)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, False)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, False)  # F
            GPIO.output(seg1G, False)  # G

        elif number == 2:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, False)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, True)  # E
            GPIO.output(seg1F, False)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 3:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, False)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 4:
            GPIO.output(seg1A, False)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, False)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 5:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, False)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 6:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, False)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, True)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 7:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, False)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, False)  # F
            GPIO.output(seg1G, False)  # G

        elif number == 8:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, True)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, True)  # G

        elif number == 9:
            GPIO.output(seg1A, True)  # A
            GPIO.output(seg1B, True)  # B
            GPIO.output(seg1C, True)  # C
            GPIO.output(seg1D, True)  # D
            GPIO.output(seg1E, False)  # E
            GPIO.output(seg1F, True)  # F
            GPIO.output(seg1G, True)  # G

    def writeOnes(self, number):
        if number == 0:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, True)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, False)  # G

        elif number == 1:
            GPIO.output(seg2A, False)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, False)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, False)  # F
            GPIO.output(seg2G, False)  # G

        elif number == 2:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, False)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, True)  # E
            GPIO.output(seg2F, False)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 3:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, False)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 4:
            GPIO.output(seg2A, False)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, False)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 5:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, False)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 6:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, False)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, True)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 7:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, False)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, False)  # F
            GPIO.output(seg2G, False)  # G

        elif number == 8:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, True)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, True)  # G

        elif number == 9:
            GPIO.output(seg2A, True)  # A
            GPIO.output(seg2B, True)  # B
            GPIO.output(seg2C, True)  # C
            GPIO.output(seg2D, True)  # D
            GPIO.output(seg2E, False)  # E
            GPIO.output(seg2F, True)  # F
            GPIO.output(seg2G, True)  # G

    def writeToSevenSegmentDisplay(self, num):
        print("Writing " + str(num))
        print("Writing " + str(num % 10) + " to ones")
        self.writeOnes(num % 10)
        print("Writing " + str(num // 10) + " to tens")
        self.writeTens(num // 10)

    def increaseTemp(self, channel):
        print("called increaseTemp, channel=", channel)
        if (self.myWindow.focus_get() == self.entry1):
            self.actualTemp.set(self.actualTemp.get() + 1)
            self.writeToSevenSegmentDisplay(self.actualTemp.get())
            self.turnActualLED()

        elif (self.myWindow.focus_get() == self.entry2):
            self.targetTemp.set(self.targetTemp.get() + 1)
            self.writeToSevenSegmentDisplay(self.targetTemp.get())
            self.turnTargetLED()

    def decreaseTemp(self, channel):
        print("called decreaseemp, channel=", channel)
        if (self.myWindow.focus_get() == self.entry1):
            self.actualTemp.set(self.actualTemp.get() - 1)
            self.writeToSevenSegmentDisplay(self.actualTemp.get())
            self.turnActualLED()
        elif (self.myWindow.focus_get() == self.entry2):
            self.targetTemp.set(self.targetTemp.get() - 1)
            self.writeToSevenSegmentDisplay(self.targetTemp.get())
            self.turnTargetLED()
    def turnActualLED(self):

        GPIO.output(LEDred,False)	#RED
        GPIO.output(LEDgreen,False)	#GREEN
        GPIO.output(LEDblue,True)	#BLUE

    def turnTargetLED(self):
        GPIO.output(LEDred,False)	#RED
        GPIO.output(LEDgreen,True)	#GREEN
        GPIO.output(LEDblue,False)	#BLUE

    def submit(self):
        showinfo("Temperature reading", "Actual temperature is: " + str(self.actualTemp.get()) + '\n' + "Target temperature is: " + str(self.targetTemp.get()) )


if __name__ == "__main__":
    my_gui = MyGui()
    GPIO.add_event_detect(5, GPIO.FALLING, callback=my_gui.increaseTemp, bouncetime=200)
    GPIO.add_event_detect(12, GPIO.FALLING, callback=my_gui.decreaseTemp, bouncetime=200)
    mainloop()



