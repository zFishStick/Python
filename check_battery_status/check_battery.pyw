#A simple program that allows you to check your battery percentage

from win11toast import toast
import psutil as ps

charged_battery_icon = {
    'src' : 'C:\\Users\\gabri\\OneDrive\\Desktop\\Zona mij\\Python\\Check_Battery\\charged.ico',
    'placement': 'appLogoOverride'
}

low_battery_icon = {
    'src' : 'C:\\Users\\gabri\\OneDrive\\Desktop\\Zona mij\\Python\\Check_Battery\\low.ico',
    'placement': 'appLogoOverride'
}

mid_battery_icon = {
    'src' : 'C:\\Users\\gabri\\OneDrive\\Desktop\\Zona mij\\Python\\Check_Battery\\mid_charged.ico',
    'placement': 'appLogoOverride'
}


loopToken = True #To not receive infinite notifications :p


#This block checks when you should plug/unplug your AC adapter automatically
while True:
    battery = ps.sensors_battery()
    battery_percentage = battery.percent
    AC_power = battery.power_plugged
    #Check if the battery is below or equal to 45% and the PC is not in charge
    if (battery_percentage <= 45) and (AC_power == False) and (loopToken == True):
            toast(title='Battery about %s%%' % (battery_percentage),
            body='Battery low, please put in charge your PC',icon=low_battery_icon)
            loopToken = False #In this way it doesn't go in a infinite loop
    if (battery_percentage >= 90) and (AC_power == True) and (loopToken == False):
            toast(title='Battery about %s%%' % (battery_percentage),
            body='Battery charged, please remove the power cable', 
            icon=charged_battery_icon)
            loopToken = True
