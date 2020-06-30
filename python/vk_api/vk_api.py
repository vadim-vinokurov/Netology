import requests
import json
from pprint import pprint
class User:

	def get_user1(self, user1):
		URL = 'https://api.vk.com/method/users.get?'
		params = {
			'access_token':'fd0eb196d72a346219223e0b0e63b8930f343c168859051e4ea99d21283b5efc3311af531c79c5bf576eb',
			'user_ids':user1,
			'v':'5.107'
		}
		r = requests.get(URL, params).json()
		return r['response'][0]['id']

	def get_user2(self, user2):

		URL = 'https://api.vk.com/method/users.get?'
		params = {
			'access_token':'fd0eb196d72a346219223e0b0e63b8930f343c168859051e4ea99d21283b5efc3311af531c79c5bf576eb',
			'user_ids':user2,
			'v':'5.107'
		}
		r = requests.get(URL, params).json()
		return r['response'][0]['id']

	def friends_get_Mutual(self, s1, s2):
		users = {}
		uri = 'https://vk.com/id'
		URL = 'https://api.vk.com/method/friends.getMutual?'
		params = {
			'access_token':'fd0eb196d72a346219223e0b0e63b8930f343c168859051e4ea99d21283b5efc3311af531c79c5bf576eb',
			'source_uid':s1,
			'target_uid':s2,
			'v':'5.107'
		}
		try: # НА ВСЯКИЙ СЛУЧАЙ, ПРОСТО НЕ ЗНАЮ КАКОЕ ПОВЕДЕНИЕ БУДЕТ ЕСЛИ ВДРУГ СТРАНИЦА ЗАБЛОКИРОВАНА ИЛИ УДАЛЕНА
			r = requests.get(URL, params).json()
		except:
			pass
		for i, k in enumerate(r['response']):
			link = f'https://vk.com/id{k}'
			users.update({i: link})
		return users


s = User()
s1 = s.get_user1(10558439)
s2 = s.get_user2(104675964)
s3 = s.friends_get_Mutual(s1, s2)
pprint(s3)
