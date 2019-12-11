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



# if check_for_image('imgs/new_pc_setup.png'):
#     double_click_image('imgs/new_pc_setup.png')
#
#
##works
# install_absolute()
#
# if check_for_image('imgs/new_pc_setup.png'):
#     double_click_image('imgs/new_pc_setup.png')

##need to come back for access panel on new computer. Network resource not available
# install_access_panel()

#works
# install_chrome()

##need to come back for Mitel on fresh computer
# install_mitel()

#works
# install_printer_installer()

# come back to adobe on new computer so don't have to uninst chrome
# install_adobe()
#

#works
install_teams()
# install_vpn()
# install_Ch_Ad()
# install_cylance()
