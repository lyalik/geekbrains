import os

def find_files_by_extension(directory, extension):
    """Находит и перечисляет все файлы с заданным расширением в указанном каталоге и его подкаталогах."""
    matching_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                matching_files.append(file_path)
                print(file_path)

    return matching_files