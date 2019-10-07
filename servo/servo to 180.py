import time
import board
import pulseio
from adafruit_motor import servo
import touchio
from board import *
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

touch = touchio.TouchIn(touch_pad)

while True:
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        my_servo.angle = angle
        time.sleep(0.05)
     while True:
    if touch.value:
        print("Touched!")
    time.sleep(0.05)