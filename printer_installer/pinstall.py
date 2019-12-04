from clicks import *
import pyautogui
import time

def install_printer_installer():
    double_click_image('printer_installer/img/pinstallertooltip.png')
    wait(30)
    single_click_image('printer_installer/img/next.png')
    wait(10)
    single_click_image('printer_installer/img/finish.png')
