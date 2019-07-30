#TODO:
#-disable roll button when there is no dice selected
#-disable custom dice type value entry widget when custom dice radiobutton is not selected
#-if custom is selected and there is no custom value catch error (also number can not be negative or zero or string) -> make input box red and lock roll button
#-add locking radiobutton change during rolling

from tkinter import *
from tkinter import ttk
from random import *
from time import *
import threading

v = 0

diceTypeList = [
    ('K4', 4),
    ('K6', 6),
    ('K10', 10),
    ('K12', 12),
    ('K20', 20),
    ('K100', 100),
    ('K', 0)
    ]

#Determine roll result
def startThreadRoll():#start separate thread for rolling (prevents GUI freezing during roll)
   threadRoll = threading.Thread(target = roll)
   threadRoll.start()

def roll():
    for i in range (1,100): #Roll animation
        actDiceValue = randint(1, diceTypeSelected.get())
        result.configure(text = actDiceValue)
        sleep(0.01)

# Create main window
windowMain = Tk()
windowMain.title('Dices')

##### STYLES #####

styleDefault = ttk.Style()
styleDefault.configure('result.TLabel', font = ('Arial', 100))

##########

#Frame for dice selection on the left side of the window
frameDiceSelection = ttk.Frame(windowMain, padding = 10, borderwidth = 2, relief = 'sunken')
frameDiceSelection.pack(side = LEFT, fill = BOTH)

#Frame for rolling table on the right side of the window
frameRolling = ttk.Frame(windowMain, padding = 10, borderwidth = 2, relief = 'sunken')
frameRolling.pack(side = LEFT, fill = BOTH)

#Dice type selection radiobuttons
diceTypeSelected = IntVar()
diceTypeSelected.set(4)
for i, (diceTypeName, diceTypeValue) in enumerate(diceTypeList):
    ttk.Radiobutton(frameDiceSelection, text = diceTypeName, variable = diceTypeSelected, value = diceTypeValue).grid(sticky = W, row = i, column = 0)

#Input for custom dice
diceTypeCustomValue = StringVar();
entryDiceTypeCustomValue = ttk.Entry(frameDiceSelection, textvariable = diceTypeCustomValue)
entryDiceTypeCustomValue.grid(sticky = W, row = len(diceTypeList)-1, column = 1)

#show roll result
result = ttk.Label(frameRolling, text = 0, style = 'result.TLabel')
result.pack()

#Button for rolling the dice
buttonRoll = ttk.Button(frameRolling, text = 'Roll the dice!', command = startThreadRoll)
buttonRoll.pack()

#if no dice is selected disable Roll button
if v>5:
    buttonRoll.state(['disabled'])
else:
    buttonRoll.state(['!disabled']) 

windowMain.mainloop()
