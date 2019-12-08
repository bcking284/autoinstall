import pyautogui
import time
from imagesearch import *


def wait_and_click(image, clicks,button):
    pos = imagesearch_loop(image, 1)
    click_image(image,pos,action = button,timestamp=1,clicks=clicks)

def double_click_image(imagefile):
	wait_and_click(imagefile,clicks=2, button='left')

def right_click_image(imagefile):
	wait_and_click(imagefile,clicks=1, button='right')

def single_click_image(imagefile):
	wait_and_click(imagefile,clicks=1, button='left')

def type_string(text):
	pyautogui.typewrite(text,interval=0.125)

def press_enter():
	pyautogui.typewrite(['enter'],interval=0.125)

def arrow_key(direction):
	#left or right
	pyautogui.hotkey(direction)

def wait(leng):
	time.sleep(leng)

def wait_for_image(image):
	pos = imagesearch_loop(image, 1)
	if pos:
		return True

def check_for_image(image):
	return imagesearch(image) != [-1,-1]
