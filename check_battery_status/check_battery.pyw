#A simple program that allows you to check your battery percentage

from win11toast import toast
import psutil as ps
from playsound import playsound
import os
import time
import threading

#Current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

charged_battery_icon = {
    'src': os.path.join(script_dir, 'icons\\charged.ico'),
    'placement': 'appLogoOverride'
}

low_battery_icon = {
    'src': os.path.join(script_dir, 'icons\\low_battery.ico'),
    'placement': 'appLogoOverride'
}

mid_battery_icon = {
    'src': os.path.join(script_dir, 'icons\\mid_charged.ico'),
    'placement': 'appLogoOverride'
}

#Sound
low_battery_sound = os.path.join(script_dir, 'audio\\low_battery_sound.mp3')
charged_battery_sound = os.path.join(script_dir, 'audio\\charged_sound.mp3')

loopToken = True #To not receive infinite notifications :p

def show_toast(title, body, icon):
    toast(title=title, body=body, icon=icon)

def play_sound(sound_path):
      playsound(sound_path)

def thread_init(notification, sound):
    notification_thread.start()
    sound_thread.start()
    notification_thread.join()
    sound_thread.join()
      

#This block checks when you should plug/unplug your AC adapter automatically
while True:
    battery = ps.sensors_battery()
    battery_percentage = battery.percent
    AC_power = battery.power_plugged
    #Check if the battery is below or equal to 45% and the PC is not in charge
    if (battery_percentage <= 25) and (AC_power == False) and (loopToken == True):
            notification_thread = threading.Thread(target=show_toast, 
                                                   args=('Battery about %s%%' % (battery_percentage), 
                                                         'Battery low, please put in charge your PC', 
                                                         charged_battery_icon))
            sound_thread = threading.Thread(target=play_sound, args=(low_battery_sound,))
            thread_init(notification_thread, sound_thread)
            loopToken = False #In this way it doesn't go in a infinite loop

    if (battery_percentage >= 90) and (AC_power == True) and (loopToken == False):
            notification_thread = threading.Thread(target=show_toast, 
                                                   args=('Battery about %s%%' % (battery_percentage), 
                                                         'Battery charged, please remove the power cable', 
                                                         charged_battery_icon))
            sound_thread = threading.Thread(target=play_sound, args=(charged_battery_sound,))
            thread_init(notification_thread, sound_thread)
            loopToken = True
    # else:
    #     notification_thread = threading.Thread(target=show_toast, 
    #                                            args=('Battery about %s%%' % (battery_percentage), 
    #                                                  'Battery charged, please remove the power cable', 
    #                                                  charged_battery_icon))
    #     sound_thread = threading.Thread(target=play_sound, args=(charged_battery_sound,))
    #     thread_init(notification_thread, sound_thread)
    #     break
    time.sleep(60)