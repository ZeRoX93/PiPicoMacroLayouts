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
    # Wait for 1 seconds
    time.sleep(0.5)
    # Remove the macro label after 1 seconds
    splash.remove(macro_label)
    display.refresh()
    
    

def handle_keypress(key, cc, write_text, keyboard, splash, display ):
    
    # Macro names or actions
    # Change the macro names * 
    macro_names = {
        0: "1",
        1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "10",
        10: "11",
        11: "12",
        12: "13",
        13: "14",
        14: "15",
        # Add more macro names and their corresponding keys as needed
    }
    
    #Repkace keyboard.send(Keycode.G) with your macro code
    
    if key[0].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[0], display)
         
    if key[1].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[1], display)
        
    if key[2].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[2], display)
    
    if key[3].value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
        update_screen(splash, macro_names[3], display)
    
    if key[4].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[4], display)
        
    if key[5].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[5], display)

    if key[6].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[6], display)
        
    if key[7].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[7], display)
        
    if key[8].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[8], display)
        
        
    if key[9].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[9], display)
        
    if key[10].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[10], display)
        
    if key[11].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[11], display)

    if key[12].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[12], display)

    if key[13].value:
        keyboard.send(Keycode.G)
        time.sleep(0.1)
        update_screen(splash, macro_names[13], display)
         

    time.sleep(0.0001)
