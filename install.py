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
from prog.imaging.imaging import *
from prog.gotoassist.install import *
from prog.mimecast.mimecast import *

def click_file_explorer():
	if not check_for_image('imgs/file_icon.png'):
		single_click_image('imgs/file_explorer_icon.png')

if check_for_image('imgs/new_pc_setup.png'):
    double_click_image('imgs/new_pc_setup.png')

start_point = str(input("Where would you like the program to start? \nBeginning (1)\nMimecast (2)\nAccess Panel (3)\nChrome (4)\nMitel (5)\nPrinter Installer (6)\nAdobe (7)\nTeams (8)\nVPN (9)\nGotoassist (10)\nCyclance (11)\nImaging (12)"))
if start_point == '1':
	##works
	install_absolute()

	if check_for_image('imgs/new_pc_setup.png'):
	    double_click_image('imgs/new_pc_setup.png')

	install_mimecast()

	click_file_explorer()

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

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '2':
	install_mimecast()

	click_file_explorer()

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

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '3':
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

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '4':
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

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '5':
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

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '6':
	# works
	install_printer_installer()

	click_file_explorer()

	# works
	install_adobe()

	click_file_explorer()

	# works
	install_teams()

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '7':

	install_adobe()

	click_file_explorer()

	# works
	install_teams()

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '8':
	install_teams()

	click_file_explorer()
	# works
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '9':
	install_vpn()

	click_file_explorer()

	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '10':
	install_g2a()

	click_file_explorer()

	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '11':
	install_cylance()

	single_click_image('imgs/new_pc_setup.png')

	click_file_explorer()

	install_imaging()

if start_point == '12':
	install_imaging()
