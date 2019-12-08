import pyautogui
print('press control+c to quit')
try:
    while True:
        #todo : get and print screen coordinates
        (x,y) = pyautogui.position()
        positionstr = 'X: ' +str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionstr, end='')
        print('\b' *len(positionstr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
