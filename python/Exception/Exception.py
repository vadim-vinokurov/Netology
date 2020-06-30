documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "1002345"}
      ]

                     # Задание № 1, 2

def polskaya_nataciya(a):
    operator = a[0]
    operand_1 = int(a[1])
    operand_2 = int(a[2])
    assert operand_1 > 0, 'Число должно быть положительным'
    assert operand_2 > 0, 'Число должно быть положительным'
    assert operator in ['+', '-', '*', '/'], 'Оператор должен быть [’+’, ‘-’, '*', ‘/’]'
    if operator == '+':
        result = operand_1 + operand_2
        print(f'{operator} {operand_1} {operand_2} = {result}')
    elif operator == '-':
        result = operand_1 - operand_2
        print(f'{operator} {operand_1} {operand_2} = {result}')
    elif operator == '*':
        result = operand_1 * operand_2
        print(f'{operator} {operand_1} {operand_2} = {result}')
    elif operator == '/':
        try:
            result = operand_1 / operand_2
            print(f'{operator} {operand_1} {operand_2} = {result}')
        except ZeroDivisionError:
            print('Делить на 0 нельзя')
        except TypeError:
            print('Делить на строки нельзя')

if __name__ == '__main__':
    a=input().split()
    polskaya_nataciya(a)
 

                       # Задание № 3

def get_list_documens(number_user):
  a = False
  for number_doc in documents:
    try:
      if number_user == number_doc['number']:
        print (number_doc['number'], number_doc['name'])
    except KeyError:
      print('Номер есть, а имени нет')
      a = True
  if a == False:
    print('Такого документы нет')


get_list_documens('1002345')
