import os


def batch_rename_files(directory, desired_name, num_digits, src_extension, dest_extension, name_range):
    """Функция для группового переименования файлов в указанной директории."""
    files = [f for f in os.listdir(directory) if f.endswith(src_extension)]

    for index, filename in enumerate(files, start=1):
        # Извлекаем часть оригинального имени в соответствии с диапазоном
        original_name_part = filename[name_range[0] - 1:name_range[1]]

        # Формируем новый порядковый номер с ведущими нулями
        index_str = str(index).zfill(num_digits)

        # Формируем новое имя файла
        new_name = f"{original_name_part}{desired_name}{index_str}.{dest_extension}"

        # Получаем полные пути к старому и новому файлам
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(old_file, new_file)
        print(f"Переименован: {old_file} -> {new_file}")