from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


search_url ='URL'
# HTTP GET requests
page = requests.get(search_url)
# Checking if we successfully fetched the URL
if page.status_code == requests.codes.ok:
  print('Everything is cool!')
  bs = BeautifulSoup(page.text, 'lxml')
  print(bs)
  
def main(): 
    list_all_imgs = bs.findAll('img')
    print(list_all_imgs)
    for img in list_all_imgs:
        myArray = []
        myArray.append(img)
        print(myArray)
main()