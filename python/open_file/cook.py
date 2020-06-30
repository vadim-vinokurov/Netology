from pprint import pprint

def get_cook_book():
	qw = [] # промежуточные списки
	wq = []  # промежуточные списки
	dishes = [] # список блюд
	ingridients = [] # список игридиентов
	count_ingridients = [] # колличество ингридиентов в блюде
	count_ingridients_person = [] # количество ингридентов на количество человек
	dish = [] # наименованиe ингридиентов
	measure = [] # весовая мера
	with open('cookbook.txt', 'r', encoding='UTF-8') as cookbook:
		for i in cookbook.readlines():
			if '\n' in i:
				qw.append(i.strip())
	for i in qw:
		if '|' in i:
			ingridients.append(i.strip())
		else:
			wq.append(i.strip())
	for i in wq:
		if i.isdigit():
			count_ingridients.append(i)
		else:
			dishes.append(i)

	for i in ingridients:
		r = i.split('|')
		dish.append(r[0])
		count_ingridients_person.append(r[1])
		measure.append(r[2])


	cook_book = {
		dishes[0]:[
			{'ingredient_name':dish[0], 'quantity':count_ingridients_person[0], 'measure':measure[0]},
			{'ingredient_name':dish[1], 'quantity': count_ingridients_person[1], 'measure': measure[1]},
			{'ingredient_name': dish[2], 'quantity': count_ingridients_person[2], 'measure': measure[2]}
			],
		dishes[2]:[
			{'ingredient_name': dish[3], 'quantity': count_ingridients_person[3], 'measure': measure[3]},
			{'ingredient_name': dish[4], 'quantity': count_ingridients_person[4], 'measure': measure[4]},
			{'ingredient_name': dish[5], 'quantity': count_ingridients_person[5], 'measure': measure[5]},
			{'ingredient_name': dish[6], 'quantity': count_ingridients_person[6], 'measure': measure[6]}
			],
		dishes[4]:[
			{'ingredient_name': dish[7], 'quantity': count_ingridients_person[7], 'measure': measure[7]},
			{'ingredient_name': dish[8], 'quantity': count_ingridients_person[8], 'measure': measure[8]},
			{'ingredient_name': dish[9], 'quantity': count_ingridients_person[9], 'measure': measure[9]}

		]
	}

	return cook_book

def get_shop_list_by_dishes(dishes, person_count):
	cook_book = get_cook_book()
	count_person = cook_book.values()

	if 'Запеченный картофель' in dishes:
		for i in cook_book:
			pprint({
				cook_book.get(i, None)[2]['ingredient_name']:{'measure':cook_book.get(i, None)[0]['measure'],
				                                              'quantity':cook_book.get(i, None)[0]['quantity']}
			})

get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 2)



