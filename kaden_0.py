from selenium.webdriver import Chrome, ChromeOptions
from  webdriver_manager.chrome import ChromeDriverManager
from  bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


    
def scraping_0():

      #1ページurlの取得
      #df = pd.read_csv("outputdata.csv")
      #df = df.iloc[0,2]
      #url ="https://www.biccamera.com/bc/category/001/300/"
      #url = "https://www.biccamera.com/bc/category/001/300/002/?p=2#bcs_resultTxt"
      #df = url

      #1ページ目
      #num = 1
      response = req.urlopen(df)
      #category = BeautifulSoup(response,'html.parser')
       
        
while True :
      df = pd.read_csv("outputdata.csv")
      df = df.iloc[0,2]
      #num = 1
      
      response = req.urlopen(df)
      if num >= 2 :
      #num = 2

        try :
            response = req.urlopen(df+'?p='+ str(num)+ '#bcs_resultTx')
            category = BeautifulSoup(response,'html.parser')
        except:
             
            break
      else:

      #商品名の取得
      #商品のURLの取得
             category = BeautifulSoup(response,'html.parser')
             block1 = category.find_all('a',class_= 'bcs_item')
      
             title_list = []
             url_list = []

      for i in block1:
            
               title_list.append(i.string)
               url_list.append(i.attrs['href'])
      
      #print(title_list)
      #print(url_list)

      #値段の取得
      block2 = category.find_all('span',class_= 'val')

      price_list = []

      for i in block2:
            
               price_list.append(i.string)

      #print(title_list)
      #print(url_list)
      print(price_list)
      

      df = pd.DataFrame({"商品名":title_list,"URL":url_list,"値段":price_list})
      df.to_csv("outputdata_02.csv")

      num = num + 1


              
scraping_0()
