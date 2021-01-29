# This is the main driver stub file
#
#

import lcddriver
from time import *
from datetime import datetime
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("My words -", 1)
lcd.lcd_display_string("Coming from web", 2)
lcd.lcd_display_string("Going nowhere", 3)
lcd.lcd_display_string("12345678901234567890", 4)

sleep(3)

lcd.lcd_display_string("Turning off light", 4)
sleep(2)

lcd.lcd_backlight("Off")

sleep(3)

lcd.lcd_display_string("And Magically On", 4)
sleep(.1)
lcd.lcd_backlight("On")

sleep(5)

lcd.lcd_clear()

lcd.lcd_display_string("Current Time:", 1)

while (True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = "   " + current_time
    lcd.lcd_display_string(current_time, 2)
    sleep(1)
