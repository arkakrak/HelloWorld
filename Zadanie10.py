from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://duckduckgo.com/")
browser.find_element_by_id("search_form_input_homepage").send_keys("Harmonogram ii up")
browser.find_element_by_id("search_button_homepage").click()
browser.find_element_by_id("r1-0").click()
assert "Harmonogramy" in browser.title
# browser.find_element_by_link_text("pdf/schedules/2019-20/niestacjonarne/II rok/zjazd7_13-15_XII_INF II N 2019-20.pdf").click()