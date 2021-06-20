"""
AntiGrab - Protecting your IP from grabbers and loggers everywhere
Copyright (C) 2021  Finlay1010

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import re
import random
import threading
import time

def check_modules():
	print("Checking if all necessary modules are installed...")
	try:
		import requests
	except:
		print("[ERROR] - Module 'requests' not installed!\nTo install, open 'Command Prompt' and type 'pip install requests' and wait.")
		time.sleep(5)
		quit()

	try:
		import ctypes
	except:
		print("[ERROR] - Module 'ctypes' not installed!\nTo install, open 'Command Prompt' and type 'pip install ctypes' and wait.")
		time.sleep(5)
		quit()
	print("Done!")

check_modules()
import requests
import ctypes

lock = threading.Lock()
proxy_list =[]
confirmed_sent = 0
maybe_sent = 0
proxy_errors = 0

referring_domains = [
'https://facebook.com',
'https://twitter.com',
'https://instagram.com',
'https://youtube.com',
'https://pinterest.com',
'https://linkedin.com',
'https://snapchat.com',
'https://twitch.com',
'https://discord.com',
'https://telegram.com',
'https://reddit.com',
'https://tiktok.com',
'http://bit.ly',
'http://cutt.ly',
'http://shorte.st',
'http://adf.ly',
'http://bc.vc',
'https://soo.gd',
'http://ouo.io',
'https://zzb.bz',
'http://adfoc.us',
'https://goo.gl',
'https://cutt.us',
''
]

os.system("cls")
input("Use of some features of this program may be illegal in your country.\n\nBy continuing you agree that the developer of this program will not be held responsible for any illegal activies that are committed by you (the user) via this program.")
os.system("cls")
input("It is RECOMMENDED that you use a good VPN while using this program however it is NOT REQUIRED.")

def logo():
	os.system("cls")
	print('''\u001b[36;1m
 █████╗ ███╗   ██╗████████╗██╗ ██████╗ ██████╗  █████╗ ██████╗ 
██╔══██╗████╗  ██║╚══██╔══╝██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
███████║██╔██╗ ██║   ██║   ██║██║  ███╗██████╔╝███████║██████╔╝
██╔══██║██║╚██╗██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔══██╗
██║  ██║██║ ╚████║   ██║   ██║╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
----------- { Dev: https://github.com/Finlay1010 } -----------
\u001b[0m''')

def get_input():
	logo()
	spam_type_input = input("Enter the type of request you would like to send: \n[1] - Grabify\n[2] - Simple request (Recommended for every IP grabber except Grabify)\n\n")

	if spam_type_input == '1':
		spam_type = 'spam_grabify'
		grabify_url = input("Enter the Grabify URL that you want to spam: ")
		return spam_type, grabify_url
	elif spam_type_input == '2':
		spam_type = 'basic_spam'
		url = input("Enter the IP grabber URL that you want to spam: ")
		return spam_type, url
	else:
		print("[ERROR] - INVALID INPUT: Enter the assigned number of the option that you want to choose.")
		time.sleep(2)
		os.system("cls")
		get_input()

spam_type, url = get_input()

with open('user-agents.txt', 'r') as file: 
	user_agent_list = file.readlines()

def scrape_proxies():
	global proxy_list

	os.system("cls")
	logo()

	ask_if_scrape = input("Do you already have a list of proxies that you want to use for this?\n[1] - Yes\n[2] - No\n\n")

	if ask_if_scrape == '1':
		input("Ok! Simply paste your proxy list into the 'proxies.txt' file that you downloaded with this program, save it, then press the enter key.")
		os.system("cls")
		logo()
	elif ask_if_scrape == '2':
		print("Ok! Scraping proxies...")
		get_proxies = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=elite&simplified=true").text
		with open("proxies.txt", "w+") as file:
			file.write(get_proxies)
		print("Done!")
		time.sleep(0.5)
		os.system("cls")
		logo()
	else:
		print("[ERROR] - INVALID INPUT: Enter the assigned number of the option that you want to choose.")
		time.sleep(2)
		os.system("cls")
		scrape_proxies()

	with open("proxies.txt", "r+") as file:
		read = file.readlines()
		for lines in read:
			try:
				replace = lines.split()[0].replace('\n', '')
				proxy_list.append(replace)
			except:
				pass

scrape_proxies()

def spam_grabify(grabify_url):
	global confirmed_sent, maybe_sent, proxy_errors, proxy_list
	r = requests.Session()
	random_proxy = random.choice(proxy_list)
	proxy = {
	'http': random_proxy, 
	'https': random_proxy
	}
	try:
		headers = {
		'referer': random.choice(referring_domains),
		'user-agent': random.choice(user_agent_list)
		}
		req = r.get(grabify_url, headers=headers, proxies=proxy, timeout=5).text
		if "You are about to be redirected" in req:
			token = re.findall(r'type="hidden" name="_token" value="(.*?)"',str(req))
			grabify_id = re.findall(r'type="hidden" id="special_id" name="special_id" value="(.*?)"',str(req))
			send = r.post(grabify_url, headers=headers, proxies=proxy, timeout=5)
			confirmed_sent += 1
		elif "Just a moment..." in req:
			maybe_sent += 1
		else:
			pass
		
	except:
		proxy_errors += 1


def basic_spam(url):
	global confirmed_sent, proxy_errors, proxy_list
	random_proxy = random.choice(proxy_list)
	proxy = {
	'http': random_proxy, 
	'https': random_proxy
	}
	try:
		headers = {
		'referer': random.choice(referring_domains),
		'user-agent': random.choice(user_agent_list)
		}
		req = requests.get(url, headers=headers, proxies=proxy, timeout=5)
		confirmed_sent += 1
	except:
		proxy_errors += 1


while True:
	if threading.active_count() <= 200:
		try:
			if spam_type == 'spam_grabify':
				threading.Thread(target = spam_grabify, args = (url,)).start()
				ctypes.windll.kernel32.SetConsoleTitleW('AntiGrab - Coded by Finlay | Sent (Confirmed): ' + str(confirmed_sent) + ' | Sent (Not Confirmed): ' + str(maybe_sent) + ' | Proxy errors: ' + str(proxy_errors))
			elif spam_type == 'basic_spam':
				threading.Thread(target = basic_spam, args = (url,)).start()
				ctypes.windll.kernel32.SetConsoleTitleW('AntiGrab - Coded by Finlay | Sent: ' + str(confirmed_sent) + ' | Proxy errors: ' + str(proxy_errors))
		except:
			pass