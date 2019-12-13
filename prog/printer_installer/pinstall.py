from clicks import *
import pyautogui
import time

def install_printer_installer():

    double_click_image('prog/printer_installer/img/pinstallertooltip.png')
    if not check_for_image('prog/printer_installer/img/printer_installer_title_bar.png'):
    	single_click_image('prog/printer_installer/img/focus_pinstaller.png')
    wait_and_click('prog/printer_installer/img/printer_installer_title_bar.png',1,'left')
    press_enter()
    single_click_image('prog/printer_installer/img/install.png')
    if wait_for_image('prog/printer_installer/img/finish.png'):
        press_enter()
