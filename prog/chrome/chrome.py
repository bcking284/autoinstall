from clicks import *

def install_chrome():
    double_click_image('prog/chrome/img/chrome_thumbnail.png')
    wait(10)
    while True:
	    right_click_image('prog/chrome/img/chrome_taskbar.png')
	    if check_for_image('prog/chrome/img/close.png'):
	    	single_click_image('prog/chrome/img/close.png')
	    	break
