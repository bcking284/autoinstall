import pyautogui
from clicks import *
import time

def install_absolute():
	double_click_image('prog/absolute/imgs/absolute_folder.png')
	double_click_image('prog/absolute/imgs/computracepic.png')

	if wait_for_image('prog/absolute/imgs/select_lang_prompt.png'):
		press_enter()
	if wait_for_image('prog/absolute/imgs/welcome_message.png'):
		press_enter()
	if wait_for_image('prog/absolute/imgs/start_install_prompt.png'):
		press_enter()
	if wait_for_image('prog/absolute/imgs/installer_complete.png'):
		if check_for_image('prog/absolute/imgs/dont_restart_prompt.png'):
			single_click_image('prog/absolute/imgs/dont_restart_prompt.png')
			press_enter()
		else:
			press_enter()

	while not check_for_image('prog/absolute/imgs/textbox.png'):
		right_click_image('prog/absolute/imgs/ctmweb.png')
		single_click_image('prog/absolute/imgs/runasadmin.png')
		time.sleep(10)


	if check_for_image('prog/absolute/imgs/allowaccess.png'):
		single_click_image('prog/absolute/imgs/allowaccess.png')

	single_click_image('prog/absolute/imgs/textbox.png')
	type_string('password')
	single_click_image('prog/absolute/imgs/next.png')
	single_click_image('prog/absolute/imgs/testcall.png')
	if check_for_image('prog/absolute/imgs/ctm_start.png'):
		single_click_image('prog/absolute/imgs/ctm_start.png')

	single_click_image('prog/absolute/imgs/ctmtooltip.png')
	single_click_image('imgs/new_pc_setup.png')
	# wait(0.5)
	# single_click_image('prog/absolute/imgs/close_window.png')
	# wait(1)
	# single_click_image('prog/absolute/imgs/goback.png')
