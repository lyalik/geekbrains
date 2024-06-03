def filter_short_strings(array):
    result = []
    for string in array:
        if len(string) <= 3:
            result.append(string)
    return result

# Ввод массива строк с клавиатуры
n = int(input("Введите количество строк в массиве: "))
input_array = []
print("Введите строки:")
for _ in range(n):
    input_array.append(input())

# Формирование нового массива
result_array = filter_short_strings(input_array)

# Вывод результата
print("Новый массив строк, длина которых <= 3 символам:")
for string in result_array:
    print(string)
```

### Примеры использования

1. Для массива `["Hello", "2", "world", ":-)"]`:
    - Ввод: `["Hello", "2", "world", ":-)"]`
    - Вывод: `["2", ":-)"]`

2. Для массива `["1234", "1567", "-2", "computer science"]`:
    - Ввод: `["1234", "1567", "-2", "computer science"]`
    - Вывод: `["-2"]`

3. Для массива `["Russia", "Denmark", "Kazan"]`:
    - Ввод: `["Russia", "Denmark", "Kazan"]`
    - Вывод: `[]`
