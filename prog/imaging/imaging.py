import pyautogui
from clicks import *
import time

def install_imaging():
	double_click_image('prog/imaging/imgs/img_inst.png')
	single_click_image('prog/imaging/imgs/batch_file.png')
	right_click_image('prog/imaging/imgs/batch_file.png')
	single_click_image('prog/imaging/imgs/runasadmin.png')
	single_click_image('prog/imaging/imgs/1_continue_install.png')
	single_click_image('prog/imaging/imgs/2_kofax_next.png')
	single_click_image('prog/imaging/imgs/3_accept.png')
	single_click_image('prog/imaging/imgs/4_next.png')
	single_click_image('prog/imaging/imgs/5_next.png')
	single_click_image('prog/imaging/imgs/6_config_later.png')
	single_click_image('prog/imaging/imgs/7_next.png')
	single_click_image('prog/imaging/imgs/8_install.png')
	single_click_image('prog/imaging/imgs/9_finish.png')
