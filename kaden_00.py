from selenium.webdriver import Chrome, ChromeOptions
from  webdriver_manager.chrome import ChromeDriverManager
from  bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


    
def scraping_0():

      #2ページurlの取得
      #url ="https://www.biccamera.com/bc/category/001/300/"
      #ur2 = "https://www.biccamera.com/bc/category/001/300/002/?p=2#bcs_resultTxt"
      url = "https://www.biccamera.com/bc/category/001/300/002/?p={}#bcs_resultTxt"
      


      title_list = []
      url_list = []
      price_list = []

      j = 2
      for j  in range(2, 5):
         target_url =url.format(j)
      
         print(target_url)
        
          
         response = req.urlopen(target_url)

        #商品名の取得
        #商品のURLの取得
         category = BeautifulSoup(response,'html.parser')
         block1 = category.find_all('a',class_= 'bcs_item')
      
         #title_list = []
         #url_list = []

         for i in block1:
            
           title_list.append(i.string)
           url_list.append(i.attrs['href'])
      
        
      #値段の取得

         block2 = category.find_all('span',class_= 'val')

         
         for i in block2:
            
            price_list.append(i.string)
    
            #d_list3.append(price_list)
      
      df = pd.DataFrame({"商品名":title_list,"URL":url_list,"値段":price_list})
      df.to_csv("outputdata_0205.csv")
      
scraping_0()
