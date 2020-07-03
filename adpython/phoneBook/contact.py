class Contact:

    def __init__(self, *args, **kwargs):

        self.args = list(args)
        self.kwargs = kwargs
        self.list_keys = ['Имя', 'Фамилия', 'Телефон', 'В избранных']

    def __str__(self):
        try:
            self.dataDict = dict(zip(self.list_keys, self.args))
            data = {**self.dataDict, **self.kwargs}
            if 'В избранных' not in data:
                data['В избранных'] = 'Нет'
        except Exception as e:
            print(e)
        return str(data).replace(',', '\n').replace('{', '').replace('}', '').replace("'", "")


class PhoneBook(Contact):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        super().__init__(args, kwargs)

    def listingContacts(self, start, end, **l):
        start = start - 1
        while start < end:
            yield l
            start += 1

    def addNewContact(self):
        pass

    def deleteContactByPhoneNumber(self):
        pass

    def searchAllFavoriteNumbers(self):
        pass

    def searchForContactFirstAndLastName(self):
        pass




if __name__ == '__main__':

    jhon = Contact('Jhon', 'Smith', '+71234567809',telegram='@jhony', email='jhony@smith.com')
    print(jhon)
