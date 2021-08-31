from playsound import playsound
from datetime import datetime
from time import sleep

aler_time = input("enter time :")

while 1:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == aler_time :
        playsound("sound.mp3")
        break
    else :
        sleep(10)