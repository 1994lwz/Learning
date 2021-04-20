# !usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(stroy_url):
    """get the contents"""
    r = requests.get(url=stroy_url)
    r.encoding = 'utf-8'
    html_content = r.text
    bf = BeautifulSoup(html_content, 'lxml')
    texts = bf.find('div', id='content')
    contents = texts.text.strip().split('\xa0' * 4)
    return contents


if __name__ == '__main__':
    book_name = '诡秘之主.txt'
    server = 'https://www.xsbiquge.com'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n        ')
            f.write('\n        '.join(content))
            f.write('\n')
