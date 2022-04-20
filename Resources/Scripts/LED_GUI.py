from tkinter import *
from tkinter import font
import tkinter as tk
import lgpio as GPIO

chip = GPIO.gpiochip_open(0)
LED = 21

GPIO.gpio_claim_output(chip, LED)

win = tk.Tk()

myFont = font.Font(family = 'Helvetica', size = 36, weight = 'bold')

def ledON():
    print("LED button pressed")
    if GPIO.gpio_read(chip,LED) == 0 :
        GPIO.gpio_write(chip,LED,1)
        ledButton["text"] = "LED ON"
    else:
        GPIO.gpio_write(chip,LED,0)
        ledButton["text"] = "LED OFF"

def exitProgram():
    print("Exit Button pressed")
    GPIO.gpio_write(chip, LED, 0)
    GPIO.gpiochip_close(chip)
    win.quit()


win.title("First GUI")
win.geometry('800x480')

exitButton  = tk.Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6)
exitButton.pack(side = tk.BOTTOM)

ledButton = tk.Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack()

mainloop()
