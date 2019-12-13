import pyautogui
import time
from clicks import *

def install_adobe():
	double_click_image('prog/adobe/imgs/installertooltip.png')
	single_click_image('prog/adobe/imgs/launch_checkbox.png')
	double_click_image('prog/adobe/imgs/finish_button.png')
	wait(7)
	if not check_for_image('prog/adobe/imgs/chrome_taskbar.png'):
		right_click_image('prog/adobe/imgs/edgeicon.png')
		single_click_image('prog/adobe/imgs/close_button.png')
		wait(3)
		if check_for_image('prog/adobe/imgs/close_all.png'):
			single_click_image('prog/adobe/imgs/close_all.png')
	else:
		right_click_image('prog/adobe/imgs/chrome_taskbar.png')
		single_click_image('prog/adobe/imgs/close_button.png')