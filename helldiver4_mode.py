import time
import board, busio, displayio, os, terminalio
import digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_display_text import label
import adafruit_displayio_ssd1306

def update_screen(splash, macro_name, display):
    # Update the macro label
    center_x = (118 - len(macro_name) * 6) // 2 + 5
    macro_label = label.Label(terminalio.FONT, text=macro_name, color=0xFFFF00, x=center_x, y=25)
    splash.append(macro_label)
    display.refresh()
    # Wait for 3 seconds
    time.sleep(0.5)
    # Remove the macro label after 3 seconds
    splash.remove(macro_label)
    display.refresh()
    
def handle_keypress(key, cc, write_text, keyboard, splash, display ):
    
    # Macro names or actions
    macro_names = {
        0: "Reinforce",
        1: "Resupply",
        11: "Eagle Airstrike",
        12: "Orbital Precision",
        13: "Grenade Launcher",
        14: "Guard Dog Laser",
        # Add more macro names and their corresponding keys as needed
    }
    
    #Reinforce
    if key[0].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)

        update_screen(splash, macro_names[0], display)

    #Resupply    
    if key[1].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)
        update_screen(splash, macro_names[1], display)

    #Eagle Airstrike    
    if key[11].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)
        update_screen(splash, macro_names[11], display)
    
    #Orbital Precision Strike
    if key[12].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)
        update_screen(splash, macro_names[12], display)
    
    #Granade Launcher
    if key[13].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)
        update_screen(splash, macro_names[13], display)

    #AX/LAS-5 "Guard Dog" Rover
    if key[14].value:
        keyboard.press(Keycode.CONTROL)
        time.sleep(0.05)

        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.DOWN_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.LEFT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.LEFT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.UP_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(0.05)
        keyboard.release(Keycode.RIGHT_ARROW)
        time.sleep(0.05)

        keyboard.release(Keycode.CONTROL)
        time.sleep(0.05)
        update_screen(splash, macro_names[14], display)
        
    time.sleep(0.0001)