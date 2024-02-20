# -*- coding: utf-8 -*-

def filter_strings(arr):
    new_arr = []
    for string in arr:
        if len(string) <= 3:
            new_arr.append(string)
    return new_arr

# Пример использования
input_arr = input("Введите элементы массива через запятую: ").split(",")
result = filter_strings(input_arr)
print(result)