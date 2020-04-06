import keyboard
import pyautogui
import time
## note for the future make a selection box for the user and have
## the user select if they want to had in those extra fields and
##  in order to include those filds turn them into functions and
##  just call those functions based on the selection

print("Inicitating SOAHOLD for desktop on DELL")
def deleteHold():
  ##  delete the hold
    pyautogui.keyDown('shift')
    pyautogui.press('f6')
    pyautogui.keyUp('shift')
    time.sleep(.25)
def go_to_reasons():
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.1)
    pyautogui.write('some reaon')
    time.sleep(.25)
def go_to_amount():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.25)
def go_to_date_from():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('06302020', interval=0.1)
def go_to_holdtype():
    pyautogui.press('f7')
    time.sleep(1)
    pyautogui.write('pc', interval=0.1)
    time.sleep(.25)
  
with open('id.txt') as f:

    lines = [line.rstrip() for line in f]

    my_list_len = len(lines)
pyautogui.click(x=1425, y=637)
for i in range(0, my_list_len):
    
    keyboard.wait('pause')
    
    pyautogui.press('f5')
    time.sleep(.25)
    pyautogui.write(lines[i], interval=0.1)
    time.sleep(.25)
    pyautogui.press('enter')
    time.sleep(.1)
    go_to_holdtype()
##    go_to_reasons()
##    go_to_amount()
##    go_to_date_from()

    
##  search
    pyautogui.press('enter')

##    deleteHold()
##  save all changes    
##  pyautogui.press('f10')


    print('student ID#',lines[i], i)
