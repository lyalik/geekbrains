# word_counter.py

def count_word_occurrences(word_list):
    """Функция для подсчёта количества повторений слов в списке."""
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count