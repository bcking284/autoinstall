import pyautogui
import time
from clicks import *

def install_mitel():
	double_click_image('prog/mitel/imgs/15.png')
	single_click_image('prog/mitel/imgs/install_button.png')
	if wait_for_image('prog/mitel/imgs/ready_for_next.png'):
		single_click_image('prog/mitel/imgs/17.png')

	single_click_image('prog/mitel/imgs/16.png')

	single_click_image('prog/mitel/imgs/17.png')

	single_click_image('prog/mitel/imgs/17.png')
	if check_for_image('prog/mitel/imgs/remove.png'):
		single_click_image('prog/mitel/imgs/cancel.png')
		single_click_image('prog/mitel/imgs/accept_cancel.png')

	single_click_image('prog/mitel/imgs/install_button2.png')

	single_click_image('prog/mitel/imgs/finish_button.png')
