import json
import os

def merge_json_files(input_files, output_file):
    """Объединяет данные из нескольких JSON файлов в один."""
    all_employees = []

    for file in input_files:
        with open(file, 'r', encoding='utf-8') as f:
            employees = json.load(f)
            all_employees.extend(employees)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_employees, f, ensure_ascii=False, indent=4)

    print(f"Объединённые данные сохранены в файл: {output_file}")