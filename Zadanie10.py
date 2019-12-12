from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://duckduckgo.com/")
try:
    browser.find_element_by_id("search_form_input_homepage").send_keys("Harmonogram ii up")
    browser.find_element_by_id("search_button_homepage").click()
    browser.find_element_by_id("r1-0").click()
    assert "Harmonogramy" in browser.title
    sleep(10)
    browser.find_element_by_link_text("Zjazd 7 13-15 XII 2019 r.").click()
except NoSuchElementException:
    print("No such element in html code")
finally:
    sleep(10)
    browser.close()
