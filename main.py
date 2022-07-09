import requests
from bs4 import BeautifulSoup as bs
import re 
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
import resource

resource.setrlimit (resource.RLIMIT_DATA,
                    (resource.RLIM_INFINITY
                    ,resource.RLIM_INFINITY)) 

producto = input("Entre el nombre del producto: ")

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.supermaxonline.com/shopping-home.html?utm_campaign=hub_smax_pri_online_srch_traf_pros&utm_source=google&utm_medium=paid-search&utm_content=online_clientes-nuevos-1_text-2&gclid=EAIaIQobChMI2JuQmrLq-AIVdPHjBx18OgEvEAAYASAAEgLD5_D_BwE")

#input_box = driver.find_elements(By.CLASS_NAME, 'form-inline')
#print(len(input_box))

driver.find_element(By.ID, 'header-search').send_keys(producto)
search = driver.find_element(By.CLASS_NAME, 'btn.btn-default')
search.click()

time.sleep(10)

#i = 1

#while i < 10: 
    #if producto.casefold or producto.capitalize in driver.find_element(By.CSS_SELECTOR, producto):
      #  resultados = driver.find_element(By.CLASS_NAME, "product-space").text
      #  print(resultados)

boton_load_more = driver.find_element(By.ID, 'btn-load-more')

print(driver.find_element(By.ID, 'btn-load-more'))

while True: 
    if boton_load_more.is_displayed() == True:
        load = driver.find_element(By.ID, 'btn-load-more')    
        load.click()
        time.sleep(0.5)
        boton_load_more = driver.find_element(By.ID, 'btn-load-more')
    else: 
        break 

if producto.casefold or producto.capitalize in driver.find_element(By.CSS_SELECTOR, producto):
    resultados = driver.find_element(By.ID, "products").text
    #[x.strip().split('--------------') for x in re.findall('((?:[^\n]+\n?){1,3})', producto)]
    print(resultados)
    #precio = driver.find_element(By.CLASS_NAME, "text-center precio")
    #print(precio.get_attribute('style'))

#driver.find_element(By.CSS_SELECTOR, "[title*=" + producto + "]")
#print(driver.find_element(By.CLASS_NAME, "text-center precio")).text

time.sleep(60)
driver.close()

#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49" }

#load HTML code 
#page = requests.get("https://www.supermaxonline.com/shopping-home.html?utm_campaign=hub_smax_pri_online_srch_traf_pros&utm_source=google&utm_medium=paid-search&utm_content=online_clientes-nuevos-1_text-2&gclid=EAIaIQobChMI2JuQmrLq-AIVdPHjBx18OgEvEAAYASAAEgLD5_D_BwE", headers = headers)


#print(page.text)