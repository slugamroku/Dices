#TODO:
#-disable roll button when there is no dice selected
#-disable custom dice type value entry widget when custom dice radiobutton is not selected
#-indication is needed that new number was rolled (maybe randomly changing numbers for x seconds?)



from tkinter import *
from tkinter import ttk
from random import *

v = 0

def roll():
    global v
    v = randint(1, 4)
    result.configure(text = v)

# Create main window
windowMain = Tk()
windowMain.title('Dices')

#Frame for dice selection on the left side of the window
frameDiceSelection = ttk.Frame(windowMain, padding = 10, borderwidth = 2, relief = 'sunken')
frameDiceSelection.pack(side = LEFT, fill = BOTH)

#Frame for rolling table on the right side of the window
frameRolling = ttk.Frame(windowMain, padding = 10, borderwidth = 2, relief = 'sunken')
frameRolling.pack(side = LEFT, fill = BOTH)

#Dice type selection radiobuttons
diceType = StringVar()
radiobuttonDiceTypeK4 = ttk.Radiobutton(frameDiceSelection, text = 'K4', variable = diceType, value = 'K4')
radiobuttonDiceTypeK6 = ttk.Radiobutton(frameDiceSelection, text = 'K6', variable = diceType, value = 'K6')
radiobuttonDiceTypeK10 = ttk.Radiobutton(frameDiceSelection, text = 'K10', variable = diceType, value = 'K10')
radiobuttonDiceTypeK12 = ttk.Radiobutton(frameDiceSelection, text = 'K12', variable = diceType, value = 'K12')
radiobuttonDiceTypeK20 = ttk.Radiobutton(frameDiceSelection, text = 'K20', variable = diceType, value = 'K20')
radiobuttonDiceTypeK100 = ttk.Radiobutton(frameDiceSelection, text = 'K100', variable = diceType, value = 'K100')
radiobuttonDiceTypeK4.grid(sticky = W, row = 0, column = 0)
radiobuttonDiceTypeK6.grid(sticky = W, row = 1, column = 0)
radiobuttonDiceTypeK10.grid(sticky = W, row = 2, column = 0)
radiobuttonDiceTypeK12.grid(sticky = W, row = 3, column = 0)
radiobuttonDiceTypeK20.grid(sticky = W, row = 4, column = 0)
radiobuttonDiceTypeK100.grid(sticky = W, row = 5, column = 0)

radiobuttonDiceTypeOther = ttk.Radiobutton(frameDiceSelection, text = 'K', variable = diceType, value = 'custom')
radiobuttonDiceTypeOther.grid(sticky = W, row = 6, column = 0)

#Input for custom dice
diceTypeCustomValue = StringVar();
entryDiceTypeCustomValue = ttk.Entry(frameDiceSelection, textvariable = diceTypeCustomValue)
entryDiceTypeCustomValue.grid(sticky = W, row = 6, column = 1)

result = ttk.Label(frameRolling, text = v)
result.pack()

#Button for rolling the dice
buttonRoll = ttk.Button(frameRolling, text = 'Roll', command = roll)
buttonRoll.pack()


#radiobuttonDiceTypeK3.instate(['alternate'])


#if no dice is selected disable Roll button
if v>5:
    buttonRoll.state(['disabled'])
else:
    buttonRoll.state(['!disabled'])

windowMain.mainloop()
