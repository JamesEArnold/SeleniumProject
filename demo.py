from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

# We define a variable URL for our target website
url = "https://brainyquote.com/"

# We define another variable to locate the headless web browser exe
chrome_driver_path = "../chromedriver"

# Creating an instance of our Options class
chrome_options = Options()

# This is where we make our browser headless
chrome_options.add_argument('--headless')

# This is our default search query -- any if we pass any keyword
# from the terminal, this will be replaced
search_query = "life"

# If the length of our arguments passed in from the terminal is
# atleast 2, we'll know we passed in a keyword
if (len(sys.argv) >= 2):
    search_query = sys.argv[1]
    print(search_query)

# This instance of webdriver will be working as a browser
with webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) as driver:
    # Setting the timeout time
    wait = WebDriverWait(driver, 10)

    # Retrieve the URL from the headless browser
    driver.get(url)

    # Finding the search box in the DOM
    searchBox = driver.find_element_by_id("hmSearch")
    searchBox.send_keys(search_query + Keys.RETURN)

    # Waiting until our DOM is updating with our quotesList element
    wait.until(presence_of_element_located((By.ID, "quotesList")))

    # Search through our DOM results for specific class elements
    results = driver.find_elements_by_class_name('m-brick')
    print(results)

    # Iterating through our quotes
    for quote in results:
        quoteArr = quote.text.split('\n')
        print(quoteArr)
        print()

    # Closing the browser when the task is finished
    driver.close()

