import pyautogui
import time
import keyboard

while True:
    im = pyautogui.screenshot()
    screen = im.getpixel((1143,161))
    
    x1 = im.getpixel((1391,410))
    x2 = im.getpixel((1427,423))
    x3 = im.getpixel((1296,405))
    x4 = im.getpixel((1282,401))
    
    y1 = im.getpixel((1311,361))
    y2 = im.getpixel((1300,366))
    y3 = im.getpixel((1432,365))
    y4 = im.getpixel((1451,363))
    
    if screen[0]==255:
        if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[0] != 255 or y4[0] != 255:
            pyautogui.press('space')
            time.sleep(0.0001)
        # else:  
        #     if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
        #         pyautogui.press('space')
        #         time.sleep(0.0001)
        
            
    if keyboard.is_pressed('q'):
        break
    else:
        pass