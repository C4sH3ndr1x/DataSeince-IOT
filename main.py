
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep

#setting up sensor pins
sensor = 16

#setup GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

#pushbullet access token and devices
pb = Pushbullet("token")
print(pb.devices)

#checking for inputs
while True:
    i = GPIO.input(sensor)
    if i == 0:
        print("Nothing to report.")
        sleep(1)
    elif i == 1:
        print("Mail")

        #sending push notification to your device when input = 1
        dev = pb.get_device('Google Pixel 3a')
        push = dev.push_note("You have just received mail!")
        sleep(1)

