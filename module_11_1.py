import requests
import pandas
import numpy

from pprint import pprint

# Get запрос позволяет узнать все необходимые данные страницы

response = requests.get('https://urban-university.ru/')
pprint(response.text)
print('\n')

# Возможность просмотра ответа в виде байтов

params_dict = {'q': 'Python'}
response = requests.get('https://urban-university.ru/', params=params_dict)
pprint(response.content)
print('\n')

# Код для проверки состояния ответа
# 1XX — информация
# 2XX — успешно
# 3XX — перенаправление
# 4XX — ошибка клиента
# 5XX — ошибка сервера

response = requests.get('https://urban-university.ru/')
pprint(response.status_code)
print('\n')

# Ввод с использованием массивов NumPy и установка значения индекса для входных данных.

input = numpy.array(['Denis', 'Kostya', 'Misha', 'Dmitry'])
series_data = pandas.Series(input, index=[10, 11, 12, 13])
pprint(series_data)
print('\n')

# Ввод с помощью списков, добавление меток: «Имя» и «Город» к столбцам и установили для них значения индекса.


input = [['Denis', 'Moscow'], ['Ivan', 'Kazan'], ['Dmitry', 'Ekaterinburg']]
data_frame = pandas.DataFrame(input, columns=['Name', 'City'], index=[1, 2, 3])
pprint(data_frame)
print('\n')

# функция sum() добавляет данные каждого столбца отдельно и добавляет строковые значения везде, где они есть.

input = {'Name': pandas.Series(['John, ', 'Bran, ', 'Caret, ', 'Joha, ', 'Sam']),
         'Marks': pandas.Series([44, 48, 75, 33, 99]),
         'Roll_num': pandas.Series([1, 2, 3, 4, 5])}

data_frame = pandas.DataFrame(input)
pprint(data_frame.sum())
print('\n')

# Двумерный массив NumPy.

a = numpy.array([[1, 6, 2], [4, 3, 5]])
pprint(a)
print('\n')

# Вычисляем сумму всех элементов массива

total_sum = a.sum()
print(total_sum)
print('\n')

# Массив слуйчаных чисел.

b = numpy.random.rand(3, 2)
pprint(b)
