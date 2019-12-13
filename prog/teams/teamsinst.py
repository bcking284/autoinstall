from clicks import *

def install_teams():
    double_click_image('prog/teams/imgs/teamstooltip.png')
    wait(30)
    if check_for_image('prog/teams/imgs/sign_in_prompt.png'):
    	right_click_image('prog/teams/imgs/teamsicon.png')
    	single_click_image('prog/teams/imgs/closewindow.png')
    else:
    	double_click_image('prog/teams/imgs/teams_close.png')
