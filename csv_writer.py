import csv

def write_to_csv(products, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Product Name', 'Product Price', 'Product URL', 'Description', 'ASIN', 'Product Description', 'Manufacturer']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            writer.writerow({
                'Product Name': product['Product Name'],
                'Product Price': product['Product Price'],
                'Product URL': product['Product URL'],
                'Description': product['Description'],
                'ASIN': product['ASIN'],
                'Product Description': product['Product Description'],
                'Manufacturer': product['Manufacturer']
            })
