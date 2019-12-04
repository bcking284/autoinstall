import pyautogui
import time
from clicks import *

def install_access_panel():
	double_click_image('access_panel/imgs/1.png')
	time.sleep(1)
	single_click_image('access_panel/imgs/next.png')
	time.sleep(1)
	single_click_image('access_panel/imgs/install.png')
	time.sleep(3)
	single_click_image('access_panel/imgs/finish.png')
	time.sleep(5)
	right_click_image('access_panel/imgs/ieicon.png')
	time.sleep(0.5)
	single_click_image('access_panel/imgs/close.png')