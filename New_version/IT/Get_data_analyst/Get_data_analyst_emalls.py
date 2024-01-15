# Import the requests library
import requests
from bs4 import BeautifulSoup

def Get_emalls_data(link):
# Define the URL of the website to scrape
    URL = link

    # Send a GET request to the specified URL and store the response in 'resp'
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, "lxml")
    elements = soup.select('div[class^="shop-row"]')
    print(len(elements))
    price_list = []

    for e in elements:
        print('########################################################################')
        #print(e)
        print("Class: ", e["data-price"])
        price_list.append(int(e["data-price"]))
        print('########################################################################')
    avarage = 0
    for x in price_list:
        avarage = avarage + x

    avarage = avarage / len(price_list)
    avarage = round(avarage,-3)
    numbers = "{:,}".format(avarage/10)
    print(numbers)
    #print(elements)
    # Print the HTTP status code of the response to check if the request was successful
    #print("Status Code:", resp.status_code)

    # Print the HTML content of the response
    #print("\nResponse Content:")
    #print(resp.text)
Get_emalls_data('https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_HP-LaserJet-Pro-MFP-M428dw-Multifunction-Printer~id~3581406/')