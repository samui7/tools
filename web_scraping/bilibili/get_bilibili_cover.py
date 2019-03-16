# python get_bilibili_cover.py av#
# get the cover image of any user-uploaded video by its av number

from bs4 import BeautifulSoup
import requests
import shutil
import sys

def get_cover(av_number):

    url = 'https://www.bilibili.com/video/av' + str(av_number)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            }

    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except Exception as e:
        print(e)

    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find('meta', {'itemprop': 'image'})
    cover_img_url = img.get('content')

    img_response = requests.get(cover_img_url, stream=True)
    try:
        img_response.raise_for_status()
    except Exception as e:
        print(e)

    out_name = 'av' + str(av_number) + '_cover.jpg'
    with open(out_name, 'wb') as out_file:
        shutil.copyfileobj(img_response.raw, out_file)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Use the command")
        print("  python get_bilibili_cover.py av_number")
        exit()
    av = sys.argv[1]
    get_cover(av)