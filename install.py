import pyautogui
import time
import clicks
from mitel.mitel import *
from access_panel.access import *
from absolute.absolute import *

install_absolute()
time.sleep(5)
install_access_panel()
time.sleep(5)
install_mitel()
# install_printer_installer()
# install_teams()
# install_vpn()