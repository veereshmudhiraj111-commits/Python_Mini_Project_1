from playsound import playsound
import time
from datetime import datetime

def get_alarm_time():
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    return alarm_time 
def play_alarm_sound(alarm_time):
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("Wake Up! ")
                playsound('alarm.mp3')
                break
            time.sleep(1)

alarm_time = get_alarm_time()
play_alarm_sound(alarm_time)
