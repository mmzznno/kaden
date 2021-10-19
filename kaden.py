from selenium.webdriver import Chrome, ChromeOptions
from  webdriver_manager.chrome import ChromeDriverManager
from  bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


    
def scraping():
       
       url ="https://www.biccamera.com/bc/category/001/300/"
       response = req.urlopen(url)
       category = BeautifulSoup(response,'html.parser')
       
      
       title_lists = category.find_all('a')
       #title_lists = category.find_all(text='アウトレット')
       
       title_lists[133:150]
       #print(title_lists[133].attrs['href'])

       #df = pd.DataFrame(title_list)

       #df.to_csv("outputdataba.csv")
   
       title_list=[]
       url_list = []

       for i in title_lists[133:151]:
            
             title_list.append(i.string)
            
             url_list.append(i.attrs['href'])

       df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})
       df_title_url.to_csv("outputdata.csv")
      
 
         
scraping()
