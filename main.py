# This is the main driver stub file
#
#

import lcddriver
from time import *
from datetime import datetime
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Demo of LCD Display", 1)
lcd.lcd_display_string(" ", 2)
lcd.lcd_display_string("Display size: 20", 3)
lcd.lcd_display_string("12345678901234567890", 4)

sleep(5)

lcd.lcd_clear()

lcd.lcd_display_string("Current Time:", 1)

while (True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = "   " + current_time
    lcd.lcd_display_string(current_time, 2)
    sleep(1)
