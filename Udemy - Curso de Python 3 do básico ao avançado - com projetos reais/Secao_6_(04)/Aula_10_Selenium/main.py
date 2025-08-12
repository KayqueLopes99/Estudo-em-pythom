from pathlib import Path;
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




import time
ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser

if __name__ == '__main__':
    # options = ('--headless', '--window-size=800,600')
    options = ()
    chrome_browser = make_chrome_browser(*options)
    chrome_browser.get('https://www.google.com/?hl=pt_BR')


    # espere para encontar o input de pesquisa
    search_input = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )

    # digite "Hello World" no input de pesquisa
    search_input.send_keys('Hello World')

    # tecla ENTER
    search_input.send_keys(Keys.ENTER)

    # clique no primeiro resultado
    #results = chrome_browser.find_elements(By.ID, 'search')
    #print(f'Foram encontrados {len(results)} resultados.')

    time.sleep(100)


