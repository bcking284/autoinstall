from clicks import *
def install_vpn():
    # double_click_image('prog/vpn/imgs/vpntooltip.png')
    # if wait_for_image('prog/vpn/imgs/vpnwelcome.png'):
    #     press_enter()
    #     press_enter()
    #     press_enter()
    #     press_enter()
        if check_for_image('prog/vpn/imgs/create_desktop_icon.png'):
            single_click_image('prog/vpn/imgs/create_desktop_icon.png')
        if check_for_image('prog/vpn/imgs/create_desktop_icon1.png'):
            single_click_image('prog/vpn/imgs/create_desktop_icon1.png')
        press_enter()
        press_enter()
        if wait_for_image('prog/vpn/imgs/completed.png'):
            press_enter()
