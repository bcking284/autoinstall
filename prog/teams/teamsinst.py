from clicks import *

def install_teams():
    double_click_image('prog/teams/imgs/teamstooltip.png')

    if wait_for_image('prog/teams/imgs/act_chat.png'):
        right_click_image('prog/teams/imgs/teamsicon.png')
        single_click_image('prog/teams/imgs/closewindow.png')
