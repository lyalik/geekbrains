import csv
from collections import defaultdict

def aggregate_sales(input_csv, output_csv):
    """Считывает данные из CSV файла и подсчитывает общую выручку для каждого продукта."""
    sales_data = defaultdict(float)

    # Чтение данных из входного CSV файла
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_name = row['product']
            quantity = int(row['quantity'])
            unit_price = float(row['price'])
            total_revenue = quantity * unit_price
            sales_data[product_name] += total_revenue

    # Запись агрегированных данных в выходной CSV файл
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['product', 'total_revenue'])
        for product_name, total_revenue in sales_data.items():
            writer.writerow([product_name, total_revenue])

    print(f"Итоговая выручка сохранена в файл: {output_csv}")