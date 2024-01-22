# -*- coding: utf-8 -*-
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание словаря для one-hot представления
one_hot_dict = {value: [1 if val == value else 0 for val in unique_values] for value in unique_values}

# Преобразование столбца 'whoAmI' в one-hot представление
one_hot_data = pd.DataFrame([one_hot_dict[value] for value in data['whoAmI']], columns=unique_values)

# Вывод one-hot DataFrame
print(one_hot_data.head())