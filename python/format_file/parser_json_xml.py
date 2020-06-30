import xml.etree.ElementTree as ET
import json
from collections import Counter

path_json = '/Users/Vadim/Documents/netology/python/format_file/newsafr.json'
path_xml = '/Users/Vadim/Documents/netology/python/format_file/newsafr.xml'
news_xml = []
news_json = []

def pars_json():
    z = []
    with open(path_json, encoding='utf-8') as file:
        text_json = json.load(file)
        s = text_json['rss']['channel']
        for x in s['items']:
            titles = x['description']
            for x in titles.split():
                if len(x) >=6:
                    news_json.append(x.upper())
        for i in Counter(news_json).most_common():
            z.append(list(i))
        print(f'json:\n{z[0:10]}')
pars_json()

def pars_xml():
    s = []
    tree = ET.parse(path_xml)
    root = tree.getroot()
    for i in root.iter('description'):
        for x in i.text.split():
            if len(x) >= 6:
                news_xml.append(x.upper())
    for i in Counter(news_xml).most_common():
        s.append(list(i))
    print(f'\nxml:\n{s[0:10]}')
    
pars_xml()
