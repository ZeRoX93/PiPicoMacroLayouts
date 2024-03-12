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

def handle_keypress(key, cc, write_text, keyboard, splash, display):
    
    # Macro names or actions
    macro_names = {
        0: "Play / Pause",
        1: "Play/Pause",
        2: "Open Chrome",
        3: "Volume Up",
        4: "Grab",
        # Add more macro names and their corresponding keys as needed
    }

    if key[0].value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.2)
        
        
    if key[1].value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.2)
        
    if key[2].value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('chrome\n')
        time.sleep(0.2)
        write_text.write('\n')
        time.sleep(1)
        write_text.write('https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1\n')
    
    if key[3].value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.2)
    
    if key[4].value:
        print("test")
        keyboard.send(Keycode.N)
        time.sleep(0.2)
        

    time.sleep(0.0001)
