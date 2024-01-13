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
    'src' : 'mid_charged.ico',
    'placement': 'appLogoOverride'
}

battery = ps.sensors_battery()
battery_percentage = battery.percent
AC_power = battery.power_plugged


#This block checks when you should plug/unplug your AC adapter automatically
if (battery_percentage <= 45) and (AC_power == False):
    toast(title='Battery about %s%%' % (battery_percentage),
          body='Battery low, please put in charge your PC',icon=low_battery_icon)
elif (battery_percentage >=60) and (AC_power == True):
    toast(title='Battery about %s%%' % (battery_percentage),
          icon=mid_battery_icon)
elif (battery_percentage >= 90) and (AC_power == True):
    toast(title='Battery about %s%%' % (battery_percentage),
          body='Battery charged, please remove the power cable', 
          icon=charged_battery_icon)

#This block works only if you execute the program
if (battery_percentage > 75) and (AC_power == False):
    toast(title='Battery about %s%%' % (battery_percentage),
          body='No need to charge at the moment',
          icon=charged_battery_icon)
elif ((battery_percentage > 45) and (battery_percentage < 75)) and (AC_power == False):
    toast(title='Battery about %s%%' % (battery_percentage),
          body='No need to charge at the moment',
          icon=mid_battery_icon)
elif AC_power == True:
        toast(app_id='Battery status',title='Battery about %s%%' % (battery_percentage),
          body='Currently charging',
          icon=mid_battery_icon)
