import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import usb_hid
import digitalio
import time
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from windows_mode import handle_keypress as windows_mode_handle_keypress
from template_mode import handle_keypress as template_mode_handle_keypress
from helldiver1_mode import handle_keypress as helldiver1_mode_handle_keypress
from helldiver2_mode import handle_keypress as helldiver2_mode_handle_keypress
from helldiver3_mode import handle_keypress as helldiver3_mode_handle_keypress
from helldiver4_mode import handle_keypress as helldiver4_mode_handle_keypress


#____________________________________________________________________________________


# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)

displayio.release_displays()

sda, scl = board.GP26, board.GP27
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
print(display_bus)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # Black

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a label
text = "Steam Deck"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=35, y=10)
splash.append(text_area)

# Draw a label
text2 = "MacroKeyboard"
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFF00, x=28, y=20)
splash.append(text_area2)

# These are the corresponding GPIOs on the Pi Pico that is used for the Keys on the PCB

buttons = [board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP18,board.GP19]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(0,len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN

modeChangeButton = digitalio.DigitalInOut(board.GP20)
modeChangeButton.direction = digitalio.Direction.INPUT
modeChangeButton.pull = digitalio.Pull.DOWN

#__________________________________________________________________________________________
#_________________List of defind mode names, change the modes as you need_________________

mode_names = {1 : "Windows", 2 : "My Custom Mode", 3 : "Helldiver 1", 4 : "Helldiver 2", 5 : "Helldiver 3", 6: "Helldiver 4"}

# Set Default Mode To 1
mode = 0
print(mode_names[1])

# Function to update the macro label on the OLED screen
def update_macro_label(macro_name):
    macro_label = label.Label(terminalio.FONT, text=macro_name, color=0xFFFF00, x=0, y=25)
    splash.append(macro_label)
    display.refresh()
    time.sleep(0.01)
    splash.remove(macro_label)
    display.refresh()

while True:

    if modeChangeButton.value:
        mode = mode + 1
        if mode > 6:
            mode = 1
        time.sleep(1)

        # Make the display context
        splash = displayio.Group()
        display.show(splash)

        color_bitmap = displayio.Bitmap(128, 32, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0x000000  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a label
        text = mode_names[mode]
        center_x = (118 - len(text) * 6) // 2 + 5
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=center_x, y=15)
        splash.append(text_area)


#----------------------------------------MODE 1--------------------------------------------------------------------------

    if mode == 0:

        time.sleep(0.001)

    if mode == 1:
        windows_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)

    elif mode == 2:
        template_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)

    elif mode == 3:
        helldiver1_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)

    elif mode == 4:
        helldiver2_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)

    elif mode == 5:
        helldiver3_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)

    elif mode == 6:
        helldiver4_mode_handle_keypress(key, cc, write_text, keyboard, splash, display)


    time.sleep(0.001)




