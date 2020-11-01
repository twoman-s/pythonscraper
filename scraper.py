import requests
from bs4 import BeautifulSoup
from os import system, name

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}  # header for smooth browsing

# to clear the screen after each input


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_details(URL, choice):
    clear()
    page = requests.get(URL, headers=headers)  # get data from website
    soup = BeautifulSoup(page.content, 'html.parser')  # get page content

    if choice == "1":
        title = soup.find(id="productTitle").get_text().strip()
        mrp = soup.findAll(
            "span", {"class": "priceBlockStrikePriceString a-text-strike"})
        deal = soup.find(id="priceblock_dealprice").get_text().strip()
        print(title, " ", mrp[0].get_text().strip(), " ", deal)
    elif choice == "2":
        title = soup.findAll("span", {"class": "_35KyD6"})
        mrp = soup.findAll(
            "div", {"class": "_3auQ3N _1POkHg"})
        deal = soup.findAll(
            "div", {"class": "_1vC4OE _3qQ9m1"})
        print(title[0].get_text().strip(), " ",
              mrp[0].get_text().strip(), " ", deal[0].get_text().strip())


def main():
    # infinite while loop for menu
    while True:
        # get user choice for website
        choice = input("Select the website\n1.Amazon\n2.Flipkart\n3.Quit")
        clear()
        if choice == "1":
            print("Amazon\n")
            # get product url
            URL = input("Enter URL of the Product :")
            get_details(URL, choice)
        elif choice == "2":
            print("Flipkart\n")
            # get product url
            URL = input("Enter URL of the Product :")
            get_details(URL, choice)
        elif choice == "3":
            break
        else:
            clear()
            print("Sorry!! try again")


if __name__ == "__main__":
    clear()
    main()
