from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import re

myArray = []
links = []
search_url ='URL'
# HTTP GET requests
page = requests.get(search_url)
# Checking if we successfully fetched the URL
if page.status_code == requests.codes.ok:
  print('Everything is cool!')
  bs = BeautifulSoup(page.text, 'lxml')
  #print(bs)
#use this function to list all imgs on view source code   
def main():
    count = 0
    list_all_imgs = bs.findAll('img')
    #print(list_all_imgs)
    for img in list_all_imgs:
        global myArray
        myArray.append(img)
        count += 1
        
#main()

#print(myArray)
#use this function to find all objects by class name
def getLinks():
    count = 0
    
    list_all_links = bs.findAll('a', attrs={"class":"chapter-name text-nowrap"})
    print(list_all_links)
    
   

getLinks()
