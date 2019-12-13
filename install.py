import pyautogui
import time
import clicks
import os
from prog.mitel.mitel import *
from prog.access_panel.access import *
from prog.absolute.absolute import *
from prog.printer_installer.pinstall import *
from prog.adobe.adobeinst import *
from prog.teams.teamsinst import *
from prog.vpn.vpn_inst import *
from prog.cylance.cyinstall import *
from prog.chrome.chrome import *

def click_file_explorer():
	if not check_for_image('imgs/file_icon.png'):
		single_click_image('imgs/file_explorer_icon.png')

while not check_for_image('imgs/new_pc_setup.png'):
	if check_for_image('imgs/new_pc_setup.png'):
	    double_click_image('imgs/new_pc_setup.png')
	    break
	    wait(3)



##works
install_absolute()

if check_for_image('imgs/new_pc_setup.png'):
    double_click_image('imgs/new_pc_setup.png')

# works
install_access_panel()

click_file_explorer()
# works
install_chrome()

click_file_explorer()

# works
install_mitel()

click_file_explorer()

# works
install_printer_installer()

click_file_explorer()

# works
install_adobe()

click_file_explorer()

# works
install_teams()

# works
install_vpn()

# install_imaging()
install_cylance()
