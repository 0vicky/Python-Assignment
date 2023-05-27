import requests
from bs4 import BeautifulSoup

def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the necessary information from the product page
    description_element = soup.find('div', {'id': 'productDescription'})
    description = description_element.text.strip() if description_element else None

    asin_element = soup.find('th', text='ASIN')
    asin = asin_element.find_next('td').text.strip() if asin_element else None

    product_description_element = soup.find('div', {'id': 'productDescription_feature_div'})
    product_description = product_description_element.text.strip() if product_description_element else None

    manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
    manufacturer = manufacturer_element.text.strip() if manufacturer_element else None

    # If the above extraction fails, try alternative selectors or patterns specific to the page structure
    if not description:
        description_element = soup.find('div', {'id': 'feature-bullets'})
        description = description_element.text.strip() if description_element else None

    if not asin:
        asin_element = soup.find('th', {'class': 'prodDetSectionEntry'}, text='ASIN:')
        asin = asin_element.find_next('td').text.strip() if asin_element else None

    if not product_description:
        product_description_element = soup.find('div', {'id': 'prodDetails'})
        product_description = product_description_element.text.strip() if product_description_element else None

    if not manufacturer:
        manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
        manufacturer = manufacturer_element.text.strip() if manufacturer_element else None

    return {
        'Description': description,
        'ASIN': asin,
        'Product Description': product_description,
        'Manufacturer': manufacturer
    }
