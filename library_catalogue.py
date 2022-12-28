from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

title = "title"
chr_options = Options()
chr_options.add_experimental_option("detach", True)
path = 'C:/Users/atiya/PycharmProjects/library_catalogue/chromedriver_win32/chromedriver.exe'
service = Service (executable_path=path)
website = 'https://miss.ent.sirsidynix.net/client/en_CA/mlsathome/'
driver = webdriver.Chrome(service=service, chrome_options=chr_options)

driver.get(website)

def get_book ():
    title = sys.argv.remove("library_catalogue.py")
    print ("title")

def search_book():
    book_search = driver.find_element(By.ID,'q')
    book_search.send_keys(title)
    search_btn = driver.find_element(By.ID,'searchButton')
    search_btn.click()

def apply_filter ():
    filter =driver.find_element(By.XPATH,"//input[@title='Regular print']")
    filter.click()
    get_format = driver.find_element(By.ID,"facetFormFORMAT")
    include_filter = get_format.find_element(By.XPATH,"""//button[contains(@onclick,"doFacets('FORMAT',  'Format', 'Inclusion', 'Graph', 'true')")]""").click()



search_book()
apply_filter()