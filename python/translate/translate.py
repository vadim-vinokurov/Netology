import requests
import json
import os, glob

dirpath = '/Users/Vadim/Documents/netology/python/translate/'

es = []
de = []
fr = []

def from_file():
    os.chdir(dirpath)
    for files in glob.glob('*.txt'):
        if files == 'DE.txt':
            with open(files) as file:
                file_name = file.read()
                de.append(file_name.strip())
        elif files == 'ES.txt':
            with open(files) as file:
                file_name = file.read()
                es.append(file_name.strip())
        elif files == 'FR.txt':
            with open(files) as file:
                file_name = file.read()
                fr.append(file_name.strip())

from_file_path = from_file()

def translate_it(from_file_path):
    key = 'trnsl.1.1.20181203T070124Z.bcae76e379350fb1.3de331c4f47b5f6beb0e6b668d71a122e87bfcc0'
    data = {'lang': 'ru',
            'key': key,
            'text': from_file_path,
            'format': 'plain'
            }
    result = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data=data).json()
    return result['text']



if __name__ == '__main__':
    with open(dirpath + 'translate.txt', 'a') as file:
        file.writelines(translate_it(de))
        file.writelines(translate_it(es))
        file.writelines(translate_it(fr))