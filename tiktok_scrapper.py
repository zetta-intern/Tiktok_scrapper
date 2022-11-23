"""
In this tutorial we will scrape data from https://books.toscrape.com/ with Selenium. 
"""

import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # ignoring logging
# options.add_argument('--headless') #no head
driver = Chrome(options=options)

driver.get("https://www.tiktok.com/")
time.sleep(3)
# # elements = driver.find_element(By.LINK_TEXT, "Humor")
search_bar_el = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/form/input')
search_keyword = "cat"
search_bar_el.send_keys(search_keyword)
time.sleep(3)
search_bar_el.send_keys(Keys.ENTER)
time.sleep(3)

# Menu Video --> Manual Captcha
ii = 0
while ii < 1:
    try:
        # click menu video
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]").click()
        ii = 1
    except:
        ii = 0
        time.sleep(5)
time.sleep(3)

# Load More
# i=0
# while i<2:
#     try:
#         load_more_el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button")))
#         load_more_el.click()
#         time.sleep(2)
#     except:
#         i=2

videos = driver.find_elements(
    By.CSS_SELECTOR, ".tiktok-1soki6-DivItemContainerForSearch")
print(len(videos))
data = []
for video in videos:
    caption = video.find_element(By.CSS_SELECTOR, ".tiktok-j2a19r-SpanText")
    username = video.find_element(By.CSS_SELECTOR, ".tiktok-2zn17v-PUniqueId")
    hashtag = video.find_element(By.CSS_SELECTOR, ".tiktok-f9vo34-StrongText")

    video_data = {
        "caption": caption.text,
        "username": username.text,
        "hashtag": hashtag.text
    }
    data.append(video_data)
print(len(data))
print(data)

driver.quit()
