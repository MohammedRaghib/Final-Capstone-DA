import requests
import pandas as pd
from bs4 import BeautifulSoup

session = requests.Session()

def get_html(url):
    r = session.get(url)
    return r.text

def get_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='itm col')
    return items

def get_product_info(items, url):
    products = []
    for item in items:
        name_tag = item.find('div', class_='name')
        name = name_tag.text.strip() if name_tag else None
        prod_link = item.find('a', class_='core')
        rating = None

        if prod_link:
            prod_link = url + prod_link.get('href', None)
            req = session.get(prod_link)
            soup = BeautifulSoup(req.text, 'html.parser')

            rating_tag = soup.find('div', class_='stars _m _al')

            if rating_tag:
                rating_text = rating_tag.text.strip()
                rating_number = rating_text.split()[0]
                rating = float(rating_number)
            
        curr_price_tag = item.find('div', class_='prc')
        curr_price_text = curr_price_tag.text.strip() if curr_price_tag else None
        curr_price = None
        if curr_price_text:
            curr_price = int(''.join(filter(str.isdigit, curr_price_text))) 

        old_price = curr_price_tag.get('data-oprc', None) if curr_price_tag else None
        if old_price:
            old_price = int(''.join(filter(str.isdigit, old_price)))

        discount_tag = item.find('div', class_='bdg _dsct')
        discount = discount_tag.text.strip() if discount_tag else None

        if name and curr_price:
            products.append({
                'name': name,
                'curr_price': curr_price,
                'old_price': old_price,
                'prod_link': prod_link,
                'discount': discount,
                'rating': rating
            })
            
    for product in products:
        brand = product['name'].split()[0]
        product['brand'] = brand.lower()

    return products

def find_cheapest_seller(products):
    if not products:
        return None
    cheapest = min(products, key=lambda x: x['curr_price'])

    return cheapest


url = 'https://www.jumia.co.ke/home-office-appliances/'
html = get_html(url)
items = get_products(html)
products = get_product_info(items, url)

products_df = pd.DataFrame(products)

# for brand in brand_names:
#     products_df[brand] = products_df['brand'] == brand

print(products_df)

# products_df.to_csv('products_jumia.csv', index=False)