import requests
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

def search_meny(query):
    # Define the API endpoint URL
    api_url = "https://api.ngdata.no/sylinder/search/productsearch/v1/search/7080001150488/products"

    # Specify query parameters
    params = {
        "search": query,
        "chainId": 1300,
        "pageSize": 6,
        "page": 1,
        "showNotForSale": True,
        "popularity": True
    }

    # Send a GET request to the API
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if there are any results
        if data['total'] == 0:
            print(f"{Fore.RED}No results found.{Style.RESET_ALL}")
            return

        # Iterate through the hits and extract relevant information
        for hit in data['hits']:
            product_name = hit['title']
            product_price = hit['pricePerUnit']
            product_url = f"https://meny.no{hit['slugifiedUrl']}"

            # Format and print the product information with colors.
            print(f"{Fore.LIGHTYELLOW_EX}Product Name: {Fore.WHITE}{product_name}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Product Price: {Fore.WHITE}{product_price} kr{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Product URL: {Fore.BLUE}{product_url}{Style.RESET_ALL}")
            print()

    else:
        print(f"{Fore.RED}Failed to retrieve product data. Status code: {response.status_code}{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        user_input = input("Enter a search query, 'clear' to clear the screen, or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'clear':
            clear_screen()
        else:
            search_meny(user_input)
