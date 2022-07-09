from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def SuperMax(): 
    #This variable takes the input of the item you want to search
    producto = input("Entre el nombre del producto: ")
    #Driver that makes all the magic happen (Chrome v.103)
    driver = webdriver.Chrome(executable_path="chromedriver")
    #Link of the website
    driver.get("https://www.supermaxonline.com/shopping-home.html?utm_campaign=hub_smax_pri_online_srch_traf_pros&utm_source=google&utm_medium=paid-search&utm_content=online_clientes-nuevos-1_text-2&gclid=EAIaIQobChMI2JuQmrLq-AIVdPHjBx18OgEvEAAYASAAEgLD5_D_BwE")

    #Takes the product name and uses the search bar for getting data
    driver.find_element(By.ID, 'header-search').send_keys(producto)
    search = driver.find_element(By.CLASS_NAME, 'btn.btn-default')
    search.click()
    #Ad break 
    time.sleep(10)

    #Makes the element a variable for easier approach
    boton_load_more = driver.find_element(By.ID, 'btn-load-more')
    #While loop for load more buttons 
    while True: 
        if boton_load_more.is_displayed() == True:
            load = driver.find_element(By.ID, 'btn-load-more')    
            load.click()
            #Increase if error is given, internet may be slow 
            time.sleep(1)
            boton_load_more = driver.find_element(By.ID, 'btn-load-more')
        #If no buttons are displayed, gets out of loop
        else: 
            break 
    #Checks if prodcut name is in element and creates a string contaning the items names, weights, and prices
    if producto.casefold or producto.capitalize in driver.find_element(By.CSS_SELECTOR, producto):
        resultados = driver.find_element(By.ID, "products").text
    #Writes text file with the data and names it the same as the product name you used as input
    with open(producto + ".txt", "w") as text_file:
        text_file.write(resultados)

    #close driver after 180 seconds aka closes chrome
    time.sleep(180)
    driver.close()

if __name__ == "__main__": 
    SuperMax()