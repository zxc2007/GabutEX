#!/usr/bin/python3
################################################
# Created By Dinar Hamid                       #
# module created by Galeh Rizky And Dinar Hamid#
# kerja bangsat                                #
################################################

import time,json
import requests as req
from bs4 import BeautifulSoup as peler
from galer.wpbrute import go_brute
from galer.pretashop import go_exploit
from galer.wpexploit import wpexploit

def check_array(arr):
    if len(arr) == 0:
        return 0
    else: 
        return 1

def local_time():
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	return current_time

def save(format):
	s = open("../result/result.txt", "a+")
	s.write(format+"\n")

def formparse(url):
	ux = req.get(url,headers=headers)
	get = peler(html_str,ux.text)
	getform = peler.find_all("input",{"class":"forminput"})
	for item in getform:
		name = item.next_sibling.strip()
		return name

def check_cms(url):
	try:
#		uuri = url.split("//")[-1].split("/")[0].split('?')[0]
		http = req.get(url+"/xmlrpc.php",headers=headers)
		if 'XML-RPC' in http.text:
			print(colored("{} WORDPRESS".format(url),'yellow'))
			exploit_wp(url)
		else:
			print(colored("{} NOT WORDPRESS".format(url),'yellow'))
			exploit_other(url)
	except:
		print(colored("Unknow error check cms.",'red'))

def exploit(url):
	try:
		go_brute(url)
		wpexploit(url)
	except:
		print(colored("Seems we got error in function exploit",'red'))

def exploit_other(url):
	try:
		go_exploit(url)
	except:
		print(colored("Seems we got error in function exploit",'red'))