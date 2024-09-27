import json
import csv

def convert_json_to_csv(json_file, csv_file):
    """Считывает данные из JSON файла и сохраняет их в CSV файл."""
    with open(json_file, 'r', encoding='utf-8') as f:
        products = json.load(f)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["название", "цена", "количество на складе"])
        writer.writeheader()
        writer.writerows(products)

    print(f"Данные сохранены в CSV файл: {csv_file}")