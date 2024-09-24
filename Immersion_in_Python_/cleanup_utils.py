import os
import time

def delete_old_files(directory, days):
    """Удаляет файлы в указанном каталоге, которые не изменялись более заданного количества дней."""
    # Вычисляем время в секундах, которое соответствует заданному количеству дней
    cutoff_time = time.time() - (days * 86400) # 86400 секунд в одном дне

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Получаем время последнего изменения файла
            file_mod_time = os.path.getmtime(file_path)
            # Если файл старше заданного времени, удаляем его
            if file_mod_time < cutoff_time:
                os.remove(file_path)
                print(f"Удалён файл: {file_path}")