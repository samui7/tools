# python fetch_image_by_id.py imageID

from bs4 import BeautifulSoup
import urllib.request as request
import sys

def fetch(image_id):

    # construct url
    url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id='
    url += image_id
    url_response = request.urlopen(url)
    soup = BeautifulSoup(url_response, 'html.parser')
    container = soup.find('li', {'class':'work selected_works'})
    
    # use the following headers to avoid 403 eoor
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        }
    
    # download image
    for image in container:
        src = image.img['src']
        true_src = src.replace('c/128x128/', '').replace('square', 'master')
        print(true_src)
        file_name = str(image_id) + '_' + image.img['alt'] + '.jpg'
        file_name = file_name.replace('/', '_')
        
        _request = request.Request(true_src, None, headers)
        _response = request.urlopen(_request)
        
        with open(file_name, 'wb') as f:
            f.write(_response.read())

if __name__=='__main__':
    image_id = sys.argv[1]
    fetch(image_id)
