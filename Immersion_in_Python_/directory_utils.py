import os
import json
import csv
import pickle


def get_directory_size(directory):
    """Возвращает размер всех файлов в директории, включая вложенные директории."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def scan_directory(directory):
    """Рекурсивно обходит директорию и сохраняет результаты в файлы JSON, CSV и Pickle."""
    results = []

    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            dir_size = get_directory_size(dir_path)
            results.append({
                "name": name,
                "path": dir_path,
                "type": "directory",
                "size": dir_size,
                "parent": root
            })

        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            results.append({
                "name": name,
                "path": file_path,
                "type": "file",
                "size": file_size,
                "parent": root
            })

    # Сохранение в JSON
    with open('directory_structure.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    # Сохранение в CSV
    with open('directory_structure.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "path", "type", "size", "parent"])
        writer.writeheader()
        writer.writerows(results)

    # Сохранение в Pickle
    with open('directory_structure.pkl', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

    print("Результаты сохранены в файлы: directory_structure.json, directory_structure.csv, directory_structure.pkl")