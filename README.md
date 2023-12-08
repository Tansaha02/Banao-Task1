This Python script scrapes product details from Amazon India and saves the information in a CSV file.

Description
This script fetches product details such as Product Name, Price, Rating, and Seller Name (if available) from the specified Amazon India URL.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/amazon-product-scraper.git
cd amazon-product-scraper
Install the required Python packages:

bash
Copy code
pip install requests beautifulsoup4
Usage
Modify the url variable in the main() function to change the target Amazon India URL.

Run the script:

bash
Copy code
python amazon_scraper.py
The script will scrape the product details and save them in a file named products.csv.

Error Handling
If the server returns a 503 Service Unavailable Error, the script will display an appropriate message and terminate.
If no products are found on the Amazon page, the script will display "No products found!" and create an empty CSV file.
Contributing
Contributions are welcome! If you encounter any issues or want to enhance the script, feel free to open an issue or submit a pull request.
