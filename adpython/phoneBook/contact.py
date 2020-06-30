from pprint import pprint

class Contact:

    list_rows = ['Имя', 'Фамилия', 'Телефон', 'В избранных']
    list_args = []
    dict_args = {}

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        [Contact.list_args.append(x) for x in self.args]
        try:
            [Contact.dict_args.update({k[0::]: self.args[i]}) for i, k in enumerate(Contact.list_rows)]
        except Exception:
            if 'В избранных' not in Contact.dict_args:
                Contact.dict_args.update({'В избранных':'Нет'})


        return f"""
{Contact.dict_args}
Дополнительная информация:
        {self.kwargs}
"""


class PhoneBook(Contact):

    def __init__(self, *args, **kwargs):
        # self.name = name
        super().__init__(args, kwargs)

    def get_contact(self):
        book = Contact.dict_args
        return book

    def add_contact(self):
        pass

    def del_contact(self):
        pass

    def search_favorite_contact(self):
        pass

    def search_contact(self):
        pass



if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809',telegram='@jhony', email='jhony@smith.com')
    print(next(jhon).replace(',','\n').replace("'","").replace('{','').replace('}',''))
    c = PhoneBook.get_contact()
    print(c)