from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def scraper():
    
    # Website url
    URL = "https://www.geeksforgeeks.org/"

    # Set an options for driver
    options = Options()

    # additional settings for chrome options.
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    ## Set a service for driver
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # Create an instance of driver
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(URL)

    # The target number that I want
    target = driver.find_elements(By.TAG_NAME, "h2")
    print(f"This is the number I want: {len(target)}")
    driver.quit()

    return len(target)

if __name__ == '__main__':
     scraper()

