import os #OS interactions
import requests #HTTPS Requests
from bs4 import BeautifulSoup #Transform requests in HTML
from selenium import webdriver #Interact with Browser
from selenium.webdriver.edge.options import Options #Define browser options
from time import sleep #Pause the code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    nowindow = Options()
    nowindow.add_argument('--headless')
    nowindow.add_argument('--log-level=3')

    print('Loading Browser...')
    browser = webdriver.Edge(nowindow)

    browser.get('https://store.rg-adguard.net/')

    link_software = input("Paste the APP link here: ")
    print('Please wait...')


    url_input = browser.find_element(By.ID , 'url')

    url_input.send_keys(link_software)

    submit_button = browser.find_element(By.XPATH, "//input[@type='button']")

    sleep(1)
    
    submit_button.click()

    print("Loading links...")
    sleep(20)
    
    content = browser.page_source
    html_pag = BeautifulSoup(content, 'html.parser')
    links = html_pag.find_all('a')
    sleep(3)
    
    file_namestrings = []
    download_links = []
    if len(links) == 0:
        
        retry = input("Generation Project took a way to long to respond, retrying...")
        submit_button.click()
        sleep(10)
        content = browser.page_source
        html_pag = BeautifulSoup(content, 'html.parser')
        links = html_pag.find_all('a')
        
    if len(links) == 0:
        print("Generation Project Website is offline.")
            
            
    print('Files founded')
    #splits file name and download link
    for link in links:
        if str(link.text).endswith('.appx') or str(link.text).endswith('.msixbundle'):
            download_links.append(link['href'])
            file_namestrings.append(str(link.text))
            
    print(f"{len(download_links)} links \n")

    #Create the folder
    download_folder = "C:\\Downloads\\GenerationProject"
    
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        
    # Download the files
    for download_link, file_namestring in zip(download_links, file_namestrings):
        file_name = os.path.basename(file_namestring)
        file_path = os.path.join(download_folder, file_name)

        with open(file_path , 'wb') as f:
            response = requests.get(download_link)
            f.write(response.content)

        print(f"Downloading: {file_name} \n")

    print("All files has been sucessfully downloaded to: ", download_folder)        
            

      


    

