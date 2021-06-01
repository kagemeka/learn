from selenium import webdriver

from selenium.webdriver import(
  Firefox,
)

driver = Firefox()
driver.get(
  'https://twitter.com'
)
# print(driver.page_source)
driver.close()