#!/usr/bin/python3
################################################
# Created By Dinar Hamid                       #
# module created by Galeh Rizky And Dinar Hamid#
# kerja bangsat                                #
################################################

import time,json
import requests as req
from bs4 import BeautifulSoup as peler
from urllib3.util import parse_url

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

def get_domain(url):
                p = parse_url(url)
                x = p.host
                return x

def get_user_and_replace(url,user,x):
        try:
                if x is None:
                        return 0
                if '[DOMAIN]' or '[UPPERUSER]' or '[DEFUSER]' in x:
                        if check_array(x):
                                new = []
                                for pwd in x:
                                        new.append(pwd)
                        for px in new:
                                px.replace('[DOMAIN]',get_domain(url))
                                px.replace('[UPPERUSER]',user.upper())
                                px.replace('[DEFUSER]',user)
                        return px
        except:
                print(colored("seems we got error in function replace for wpbrute"))
