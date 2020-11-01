import requests
from bs4 import BeautifulSoup
from os import system, name
import pickle
import os.path

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

# product price details


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
# products list


def products_details(products):
    clear()
    if products.get("flipkart"):
        links = products["flipkart"]
        c = 1
        print("FLIPKART")
        for url in links:
            page = requests.get(url, headers=headers)  # get data from website
            # get page content
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.findAll("span", {"class": "_35KyD6"})
            mrp = soup.findAll(
                "div", {"class": "_3auQ3N _1POkHg"})
            deal = soup.findAll(
                "div", {"class": "_1vC4OE _3qQ9m1"})
            print(c, ". ", title[0].get_text().strip(), " ",
                  mrp[0].get_text().strip(), " ", deal[0].get_text().strip())
            c += 1
    if products.get("amazon"):
        links = products["amazon"]
        c = 1
        print("AMAZON")
        for url in links:
            page = requests.get(url, headers=headers)  # get data from website
            # get page content
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id="productTitle").get_text().strip()
            mrp = soup.findAll(
                "span", {"class": "priceBlockStrikePriceString a-text-strike"})
            deal = soup.find(id="priceblock_dealprice").get_text().strip()
            print(c, ". ", title, " ", mrp[0].get_text().strip(), " ", deal)
            c += 1


def main():
    clear()
    # infinite while loop for menu
    while True:
        # get user choice for website
        choice = input(
            "\n\n\nSelect the website\n1.Amazon\n2.Flipkart\n3.Add data to file\n4.Current products\n5.Quit  : ")
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
            # check if file is present or not
            if os.path.isfile("products.pickle"):
                clear()
                try:
                    URL = input("Enter URL of the Product :")
                    pickle_in = open("products.pickle", "rb")
                    # gets current filedata
                    products = pickle.load(pickle_in)
                    print(products)
                    pickle_in.close()
                    pickle_out = open("products.pickle", "wb")
                    # checking if url is from flipkart or amazon
                    if "flipkart" in URL.lower():
                        # works if product dictionary already have flipkart key
                        if products.get("flipkart"):
                            products["flipkart"].append(URL)
                        else:
                            products["flipkart"] = [URL]
                    elif "amazon" in URL.lower():
                        # works if product dictionary already have amazon key
                        if products.get("amazon"):
                            products["amazon"].append(URL)
                        else:
                            products["amazon"] = [URL]
                    # updates file with new products data
                    pickle.dump(products, pickle_out)
                    pickle_out.close()
                except:
                    pickle_in.close()
                    pickle_out.close()
            # if the file is not present
            else:
                clear()
                URL = input("Enter URL of the Product :")
                products = {}
                pickle_out = open("products.pickle", "wb")
                # checking if url is from flipkart or amazon
                if "flipkart" in URL.lower():
                    products["flipkart"] = [URL]
                elif "amazon" in URL.lower():
                    products["amazon"] = [URL]
                pickle.dump(products, pickle_out)
                pickle_out.close()
                print("New file created")
        elif choice == "4":
            pickle_in = open("products.pickle", "rb")
            products = pickle.load(pickle_in)
            products_details(products)
            pickle_in.close()
        elif choice == "5":
            clear()
            break
        else:
            clear()
            print("Sorry!! try again")


if __name__ == "__main__":
    main()
