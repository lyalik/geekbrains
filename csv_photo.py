import pandas as pd

# Загрузка данных из CSV файла с указанием разделителя
df = pd.read_csv('Photo_botanica_1.csv', sep=';')

# Группировка по 'product_id' и обработка каждой группы
def process_group(group):
    # Если в группе больше одной строки, переносим второй URL в 'url2'
    if len(group) > 1:
        group.iloc[1:, group.columns.get_loc('url2')] = group.iloc[1:, group.columns.get_loc('url')]
        group.iloc[1:, group.columns.get_loc('url')] = None
    return group

# Применение функции к каждой группе
df = df.groupby('product_id', group_keys=False).apply(process_group)

# Сохранение результата в новый CSV файл с разделителем ';'
df.to_csv('Photo_botanica_2.csv', index=False, sep=';')