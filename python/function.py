import random
from faker import Faker
from datetime import datetime
import csv

fake = Faker()

def generate_sample_products(num_products=1000):
    products = []
    for _ in range(num_products):
        products.append({
            'name': fake.word() + ' ' + fake.name(),  # Corrected method name
            'sku': ''.join(random.choice('ABCDEFGHIJKLM1234567890') for _ in range(8)),
            'description': fake.paragraph(nb_sentences=3),
            'price': random.uniform(10.00, 1000.00),
            'stock_quantity': random.randint(0, 500),
            'date_added': datetime.now(),
            'is_active': random.choice([True, False]),
        })
    return products

sample_data = generate_sample_products()
# Specify the CSV file path
csv_file_path = 'sample_products.csv'

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['name', 'sku', 'description', 'price', 'stock_quantity', 'date_added', 'is_active']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product in sample_data:
        writer.writerow(product)

print(f"Sample data has been written to {csv_file_path}")
