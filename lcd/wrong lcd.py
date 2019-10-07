from digitalio import DigitalInOut, Direction, Pull
import board
import time
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

presses = 0
fread = True
lread = True

begin(16,2)
print("hello, world")

while True:


    if switch.value:
        lread = True

    else:
        if fread == lread:
            switch2.value:
                presses +=1
                print(presses)



                lread = not lread