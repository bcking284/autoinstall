import pyautogui
from clicks import *
import time

def install_mimecast():
	double_click_image("prog/mimecast/imgs/tooltip.jpg")
	single_click_image("prog/mimecast/imgs/2next.png")
	single_click_image("prog/mimecast/imgs/3checkbox.png")
	single_click_image("prog/mimecast/imgs/4next.png")
	single_click_image("prog/mimecast/imgs/4next.png")
	single_click_image("prog/mimecast/imgs/5install.png")
	single_click_image("prog/mimecast/imgs/6uncheck.png")
	single_click_image("prog/mimecast/imgs/7finish.png")