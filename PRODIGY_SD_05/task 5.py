from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime 
"""
def product_information_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_name = soup.find(class_='VU-ZEz').get_text()
    product_price = soup.find(class_='Nx9bqj CxhGGd').get_text()
    product_rating = soup.find(class_='XQDdHH').get_text()
    print(product_name)
    print(product_price)
    print(product_rating)
"""


url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#file_name=str(datetime.datetime.now())
file_name="c"
sn_ls=[]
name_ls=[]
price_ls=[]
rating_ls=[]
link_ls=[]
i=0
for link in soup.find_all('a', class_='CGtC98'):
    full_link='https://www.flipkart.com'+link['href']
    response_1 = requests.get(full_link)
    soup_1 = BeautifulSoup(response_1.content, 'html.parser')
    product_name = soup_1.find(class_='VU-ZEz').get_text()
    product_price = soup_1.find(class_='Nx9bqj CxhGGd').get_text()[1:]
    product_rating = soup_1.find(class_='XQDdHH').get_text()
    sn_ls.append(i)
    name_ls.append(product_name)
    price_ls.append(product_price)
    rating_ls.append(product_rating)
    link_ls.append(full_link)
    i=i+1
#.get_text()
#.get_text()[1:]
dict={"S No":sn_ls,"Product Name":name_ls,"Product Price":price_ls,"Product Rating":rating_ls,"Product Link":link_ls}

df = pd.DataFrame(dict)
 
df.to_csv(file_name+'.csv',index=False)


