import requests
import json
import time
import os
path=os.getcwd()

def logger(log):
    def wrapper():
        try:
            if not os.path.isdir('logs'):
                os.mkdir('logs')
        except Exception:
            pass
        params = {
            'Дата': time.strftime('%d.%m.%Y'),
            'Время': time.strftime('%H.%M'),
            'Имя функции': log.__name__,
            'Аргументы':user,
            'Результат':log(user)
        }
        with open(path+'/logs/log.txt', 'a') as file:
            file.write(json.dumps(params, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':')))
    return wrapper

@logger
def get_user(user):
    """ПОЛУЧАЕМ ID ПОЛЬЗОВАТЕЛЯ ВКОНТАКТЕ"""
    URL = 'https://api.vk.com/method/'
    params = {
        'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
        'v': '5.107'
    }
    method = 'users.get?'
    params['user_ids'] = user
    r = requests.get(URL+method, params).json()
    return r['response'][0]['id']  # ID 171691064

user = input('Введите имя пользователя: ')
try:
    get_user()
except Exception as e:
    print(e)

