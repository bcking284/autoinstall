import pyautogui
import time
def double_click_image(imagefile):
	pyautogui.click(pyautogui.locateOnScreen(imagefile),button='left', clicks=2)

def right_click_image(imagefile):
	pyautogui.click(pyautogui.locateOnScreen(imagefile),button='right', clicks=1)

def single_click_image(imagefile):
	pyautogui.click(pyautogui.locateOnScreen(imagefile),button='left', clicks=1)

def type_string(text):
	pyautogui.typewrite(text,interval=0.5)

def press_enter():
	pyautogui.typewrite(['enter'],interval=0.5)

def arrow_key(direction):
	#left or right
	pyautogui.hotkey(direction)

def wait(leng):
	time.sleep(leng)

