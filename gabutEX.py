#!/usr/bin/python3

################################################
# Created By Dinar Hamid                       #
# module created by Galeh Rizky And Dinar Hamid#
# kerja bangsat                                #
################################################
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
from __future__ import print_function
from galer.module import check_cms


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
month = time.strftime("%m")
years = time.strftime("%Y")

def banner():
	print("""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |  
                                        
GabutEX v1""")

def main():
	try:
		parse = argparse.ArgumentParser(description='WordPress Killer V1')
		parse.add_argument("--list", help="List website target", required=True)
		peler = parse.parse_args()
		try:
			with ThreadPoolExecutor(max_workers=10) as Executor:
				with open(peler.list, 'r') as target:
					for s in target:
						url = s.rstrip()
						Executor.submit(check_cms,url)
		except IOError as e:
			print(colored("Unknow error.",'red'))
			sys.exit()
	except KeyboardInterrupt as e:
		print(colored("UNknow error.",'red'))
		sys.exit()		

if __name__ == '__main__':
	banner()
	main()
