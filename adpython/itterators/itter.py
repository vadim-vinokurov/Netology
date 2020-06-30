import json
from pprint import pprint
import hashlib
path = '/Users/Vadim/Documents/netology/adpython/itterators/'


class My_itter:

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def read_file(self):
        """ЧИТАЕМ ФАЙЛ countries.json"""
        with open(path+"countries.json", "r") as file:
            countries = json.load(file)
            return countries

    def __itter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start

    def get_countries(self):
        """ФОРИРУЕМ СПИСОК СТРАН ИЗ ФАЙЛА countries.json И ССЫЛКИ ИЗ WIKIPEDIA"""
        list_countries = []
        [list_countries.append(i['name']['official']+' - '+'https://en.wikipedia.org/wiki/' +
                               i['name']['official'].replace(' ', '_')) for i in self.read_file()]
        return list_countries[self.start:self.end]

# ЗАДАНИЕ №2


def counter_itter(start, end):
    file = input('Введите путь к файлу: ')
    with open(file, 'r', encoding='utf-8') as file:
        start = start - 1
        while start < end:
            yield hashlib.md5(file.readline().encode())
            start += 1


if __name__ == '__main__':
    s = My_itter(1, 30)
    with open('result.txt', 'w') as file:
        file.write(json.dumps(s.get_countries(), sort_keys=False, indent=4, ensure_ascii=True, separators=(',', ':')))

    [print(i.hexdigest()) for i in counter_itter(1, 20)]


# /Users/Vadim/Documents/netology/adpython/itterators/result.txt
