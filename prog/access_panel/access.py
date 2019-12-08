import pyautogui
import time
from clicks import *

def install_access_panel():
	double_click_image('prog/access_panel/imgs/1.png')

	if wait_for_image('prog/access_panel/imgs/welcome_message.png'):
		press_enter()

	if wait_for_image('prog/access_panel/imgs/install.png'):
		press_enter()

	if wait_for_image('prog/access_panel/imgs/finish.png'):
		press_enter()

	right_click_image('prog/access_panel/imgs/ieicon.png')
	single_click_image('prog/access_panel/imgs/close.png')
