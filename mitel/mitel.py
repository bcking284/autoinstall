import pyautogui
import time
from clicks import *

def install_mitel():
	double_click_image('mitel/imgs/15.png')
	time.sleep(15)
	single_click_image('mitel/imgs/17.png')
	time.sleep(1)
	single_click_image('mitel/imgs/16.png')
	time.sleep(1)
	single_click_image('mitel/imgs/17.png')
	time.sleep(1)
	single_click_image('mitel/imgs/17.png')
	time.sleep(1)
	single_click_image('mitel/imgs/18.png')
	time.sleep(20)
	single_click_image('mitel/imgs/20.png')
	time.sleep(3)


