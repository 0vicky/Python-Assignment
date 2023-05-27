from product_scraper import scrape_product_listing
from product_details_scraper import scrape_product_details
from csv_writer import write_to_csv

def main():
    base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"
    products = []

    # Scrape the first 100 URLs
    for page_number in range(1, 101):
        url = base_url + str(page_number)
        products.extend(scrape_product_listing(url))
        if len(products) >= 200:
            break

    # Scrape additional URLs if needed to reach the total of 200
    if len(products) < 200:
        additional_pages_needed = 200 - len(products)
        for page_number in range(101, 101 + additional_pages_needed):
            url = base_url + str(page_number)
            products.extend(scrape_product_listing(url))
            if len(products) >= 200:
                break

    for product in products:
        product_details = scrape_product_details(product['Product URL'])

        print("Product URL:", product['Product URL'])
        print("Product Name:", product['Product Name'])
        print("Product Price:", product['Product Price'])
        print("Rating:", product['Rating'])
        print("Number of Reviews:", product['Number of Reviews'])
        print("Description:", product['Description'])
        print("ASIN:", product_details['ASIN'])
        print("Product Description:", product_details['Product Description'])
        print("Manufacturer:", product_details['Manufacturer'])
        print("---------------------------")

    # Write the scraped data to a CSV file
    write_to_csv(products, 'product_data.csv')

if __name__ == "__main__":
    main()
