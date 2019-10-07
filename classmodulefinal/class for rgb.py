import pulseio
import simpleio
import time

class RGB:
    kind = "color"

    def __init__(self, r, g, b):
        self.r = pulseio.PWMOut(r, duty_cycle=0, frequency=1000)
        self.g = pulseio.PWMOut(g, duty_cycle=0, frequency=1000)
        self.b = pulseio.PWMOut(b, duty_cycle=0, frequency=1000)

    def addTrick(self, trick):
        self.tricks.append(tricks)


    def red(self, r):
        self.red(255,0,0)
        print("red")

    def green(self, g):
        self.red(255,0,0)
        print("green")

    def blue(self, b):
        self.red(255,0,0)
        print("blue")