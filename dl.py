#/usr/bin/python
# -*- coding: utf-8 -*-

# https://github.com/UtkarshGpta/nasa-apod-image-crawler

import requests
import urllib.request
import os
from bs4 import BeautifulSoup


def spider():
    directory = r'C:/Users/apod/Pictures/'
    try:
        os.chdir(directory)
    except:
        print("ERR!: Unable to use the directory provided")
        os._exit(1)
    # アーカイブ から トップページ にアクセスするよう変更
    index_url = r'http://apod.nasa.gov/apod/astropix.html'
    url = 'http://apod.nasa.gov/apod'
    source_code = requests.get(index_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for link in soup.findAll('img'):
        src = link.get('src')
        url2 = url + '/' + src
        name = src[11:]
        local = directory + '/' + name
        if (os.path.exists(local)) :
            continue
        print(name)
        urllib.request.urlretrieve(url2,name)


spider()
