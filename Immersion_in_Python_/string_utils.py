def remove_consecutive_duplicates(s):
    """Функция для удаления подряд идущих дублирующихся символов из строки."""
    if not s:
        return ""

    result = [s[0]]  # Начинаем с первого символа
    for char in s[1:]:
        if char != result[-1]:  # Добавляем символ, если он не равен предыдущему
            result.append(char)

    return ''.join(result)