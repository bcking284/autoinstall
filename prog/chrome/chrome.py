from clicks import *

def install_chrome():
    double_click_image('prog/chrome/img/chrome_thumbnail.png')
    wait(10)
    right_click_image('prog/chrome/img/chrome_taskbar.png')
    single_click_image('prog/chrome/img/close.png')
