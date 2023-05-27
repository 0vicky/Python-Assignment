import requests
from bs4 import BeautifulSoup
from product_details_scraper import scrape_product_details

def scrape_product_listing(url):
    products = []
    for page in range(1, 21):  # Scrape at least 20 pages
        page_url = f"{url}&page={page}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        product_cards = soup.find_all('div', {'data-component-type': 's-search-result'})
        for card in product_cards:
            product = {}

            product_url = card.find('a', {'class': 'a-link-normal s-no-outline'})['href']
            product_name = card.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
            product_price_element = card.find('span', {'class': 'a-offscreen'})
            product_price = product_price_element.text.strip() if product_price_element else None
            rating_element = card.find('span', {'class': 'a-icon-alt'})
            rating = rating_element.text.strip().split()[0] if rating_element else None
            num_reviews = card.find('span', {'class': 'a-size-base'}).text.strip().replace(',', '')

            product['Product URL'] = "https://www.amazon.in" + product_url
            product['Product Name'] = product_name
            product['Product Price'] = product_price
            product['Rating'] = rating
            product['Number of Reviews'] = num_reviews

            # Scrape product details
            product_details = scrape_product_details("https://www.amazon.in" + product_url)
            product.update(product_details)

            products.append(product)

    return products
