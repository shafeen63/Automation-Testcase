import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://magento.softwaretestingboard.com/")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a").click()
time.sleep(5)

# Log in to the website
username = "shafeenahmed80@gmail.com"
password = ("$Ha123456")

driver.find_element(By.ID, "email").send_keys(username)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.ID, "send2").click()
time.sleep(3)
# Wait for the login to complete and dashboard page to load
driver.find_element(By.XPATH, "//*[@id=\"ui-id-6\"]/span[2]").click()


# Add a product to the cart //*[@id="product-addtocart-button"]/span
driver.find_element(By.XPATH, "//*[@id=\"maincontent\"]/div[4]/div[1]/div[2]/div[3]/div/div/ol/li[3]/div/div/strong/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id=\"product-addtocart-button\"]/span").click()
time.sleep(2)

# Wait for the success message indicating the product has been added to the cart
driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a").click()
time.sleep(5)

# Verify if the product is successfully added to the cart
element = driver.find_element(By.ID, "top-cart-btn-checkout")
assert "Proceed to Checkout" in element.text


# Close the browser window
driver.quit()
