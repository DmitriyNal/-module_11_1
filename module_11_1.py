import numpy as np
import requests

array = np.arange(1, 10, 2)  # создание массива из чисел от 1 до 10 с шагом 2
print(array)

arr = np.array([3, 5, 7, 2, 4, 8, 9, ])
print(np.sort(arr))  # сортировка массива

a = np.array([1, 2, 3, 4, 5, 6])  # создание массива из чисел от 1 до 6
print(a)

b = np.array([7, 8, 9, 10, 11, 12])
print(np.shape(b))  # получение размерности массива

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))  # объединение массивов

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.vstack((a, b)))  # вертикальное объединение массивов

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.hstack((a, b)))  # горизонтальное объединение массивов

"""Requests — это элегантная и простая HTTP-библиотека для Python, созданная для людей."""


def get_request(url):
    response = requests.get(url)
    print(response.headers)#получение заголовков ответа
    print(response.status_code)
    print(response.encoding)#получение кодировки ответа
    return response.text# получение текста ответа


print(get_request('https://urban-university.ru/profile/course?alias=course999421818026'))
