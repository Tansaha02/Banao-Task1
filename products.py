import csv
import requests
from bs4 import BeautifulSoup


# Fetch HTML content
def fetch_content(url):
    response = requests.get(url)
    
    if response.status_code == 503:
        print('503 Service Unavailable Error: Server is temporarily unable to handle the request.')
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Extract product details
def extract_product_details(soup):
    if soup is None:
        return []

    product_list = []
    product_cards = soup.select('.s-result-item')
    #extract the required field information
    for product in product_cards:
        try:
            product_name = product.select_one('.a-text-normal').text.strip()
            product_price = product.select_one('.a-price-whole').text.strip()
            product_rating = product.select_one('.a-icon-alt').text.strip()
            product_seller = product.select_one('.a-size-mini').text.strip()
           

            product_list.append({
                'Product Name': product_name,
                'Price': product_price,
                'Rating': product_rating,
                'Seller Name': product_seller
            })
        except:
            continue

    return product_list

# Write to CSV file
def write_to_csv(file_name, product_list):
    if not product_list:
        print("No products found!")
        return
    
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        # Check if product_list is empty before accessing its elements
        fieldnames = product_list[0].keys() if product_list else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write header and rows only if product_list is not empty
        if product_list:
            writer.writeheader()
            writer.writerows(product_list)



def main():
    # Starting URL
    url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'
    
    # Get HTML content
    soup = fetch_content(url)
    
    # Extract product details
    product_list = extract_product_details(soup)
    
    # Write to CSV file
    write_to_csv('products.csv', product_list)

    print(f'{len(product_list)} products scraped and saved to products.csv')

if __name__ == '__main__':
    main()