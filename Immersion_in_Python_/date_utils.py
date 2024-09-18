def _is_leap_year(year):
    """Проверяет, является ли год високосным."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_valid_date(date_str):
    """Проверяет, может ли дата существовать в формате DD.MM.YYYY."""
    try:
        day, month, year = map(int, date_str.split('.'))

        if not (1 <= year <= 9999):
            return False

        if not (1 <= month <= 12):
            return False

        # Количество дней в каждом месяце
        days_in_month = [31, 29 if _is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (1 <= day <= days_in_month[month - 1]):
            return False

        return True
    except ValueError:
        return False