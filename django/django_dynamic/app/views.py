from django.shortcuts import render

import csv



def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста

    with open('inflation_russia.csv', newline='') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=';', quotechar=' '))

    context = {
        'file':spamreader

    }




    return render(request, template_name,
                  context)