'''
1. pip install bs4 (beautiful soup - 4) 


#Beautiful Soup
Python library for pulling data out of HTML and XML files.
It provides Pythonic idioms for iterating, searching, and modifying the parse tree.
Beautiful Soup automatically converts incoming documents to Unicode and outgoing
documents to UTF-8. It sits on top of an HTML or XML parser and provides Pythonic
dioms for iterating, searching, and modifying the parse tree.
In simpler terms, Beautiful Soup helps parse HTML or XML documents, making it
easier to extract and manipulate data from web pages. It provides methods and
attributes to navigate and search the HTML/XML structure, making web scraping tasks
more convenient and efficient.

#product_price_value = int(''.join(filter(str.isdigit, product_price.split('.')[0])))
product_price.split('.')[0]: This part splits the product_price string using the dot (.) as a separator and takes the first part before the dot. It's effectively isolating the part of the price before the decimal point.
filter(str.isdigit, ...): The filter function is used to filter out characters that are digits from the result obtained in step 1. str.isdigit is a function that returns True for each character that is a digit and False otherwise.
''.join(...): This part joins the filtered characters back into a single string. The '' between the quotes specifies that there should be no separator between the joined characters.
int(...): Finally, the entire result is converted to an integer using the int function.

'''

# Import the 'requests' module for making HTTP requests
import requests
# Import the 'BeautifulSoup' class from the 'bs4' (Beautiful Soup 4) library
from bs4 import BeautifulSoup

# URL of the webpage to scrape
URL = 'https://www.ebay.com/itm/235032714355?hash=item36b90a9c73%3Ag%3APbYAAOSwzvFkhfXK&_trkparms=%2526rpp_cid%253D64ba3dd356318a9866be5c44'

# Headers to simulate a user agent for the HTTP request
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Send an HTTP GET request to the specified URL with the provided headers
page = requests.get(URL, headers=headers)

# Create a BeautifulSoup object to parse the content of the webpage using the 'html.parser'
soup = BeautifulSoup(page.content, 'html.parser')

# Print the prettified HTML content of the webpage
# print(soup.prettify())

product_title = soup.find(class_='vim x-item-title').get_text()
product_price = soup.find(class_='x-price-primary').get_text()

# Extract numerical part of the price and convert it to an integer
product_price_value = int(''.join(filter(str.isdigit, product_price.split('.')[0])))

# print(product_title)
# print(product_price_value)

# Define a function named 'check_price'
def check_price():
    # Check if the product price is less than $500
    if product_price_value < 500:
        # Print a congratulatory message if the price has fallen below $500
        print('Congrats! The price has fallen to: $', product_price_value)
    else:
        # Print a message indicating that the price is still $500 or more
        print('Sorry! The price is still $500')

# Check if the script is run as the main module
if __name__ == "__main__":
    # Call the 'check_price' function if the script is run as the main module
    check_price()
