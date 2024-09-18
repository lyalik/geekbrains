def find_unique_elements(list1, list2):
    """Функция для нахождения элементов, уникальных для обоих списков."""
    set1 = set(list1)
    set2 = set(list2)

    # Находим элементы, которые уникальны для каждого списка
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1

    # Объединяем уникальные элементы из обоих списков
    unique_elements = list(unique_to_list1.union(unique_to_list2))

    return unique_elements