import pulseio
import simpleio
import time

class RGB
    kind = color

 def__init__(self, r, g, b):
        self.r = pulseio.PWMOut(r, duty_cycle=0, frequency=1000)
        self.g = pulseio.PWMOut(g, duty_cycle=0, frequency=1000)
        self.b = pulseio.PWMOut(b, duty_cycle=0, frequency=1000)


     def addTrick(self, trick):
          self.tricks.append(trick)


    def red(self, r):
        self.red(255,0,0)

    def green(self, g):
        self.green(255,0,0)

    def blue(self, b):
        self.blue(255,0,0)