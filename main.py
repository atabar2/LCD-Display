# This is the main driver stub file

# First edit from the web side to test sync

# First edit from RaspPi 3

import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("My words -", 1)
lcd.lcd_display_string("Coming from web", 2)
# lcd.lcd_display_string("", 3)
# lcd.lcd_display_string("HD44780 I2C Tutorial", 4)
