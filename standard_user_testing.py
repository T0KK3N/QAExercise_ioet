from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter credentials and click login || can change with different credentials here. This are for a standard user as the stories asked for.
username.send_keys("standard_user")
password.send_keys("secret_sauce")

time.sleep(3)  # Wait 
login_button.click()

try:
    # Wait until inventory container is visible
    inventory_container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    # Iterate over each inventory item to access through the image and title
    for i in range(6):
        # Click on the image link
        image_link_id = "item_" + str(i) + "_img_link"
        image_link = driver.find_element(By.ID, image_link_id)
        image_link.click()
        time.sleep(2)  # Wait 
        
        # Go back to main page
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)  # Wait 

        # Click on the title link
        title_link_id = "item_" + str(i) + "_title_link"
        title_link = driver.find_element(By.ID, title_link_id)
        title_link.click()
        time.sleep(2)  # Wait 

        # Add item to cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
        add_to_cart_button.click()
        time.sleep(2)  # Wait 
        
        # Go back to main page
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)  # Wait 

    print("Successfully added all items to cart.")

     # Click on the shopping cart link
    shopping_cart_link = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    shopping_cart_link.click()
    time.sleep(3)  # Wait 

    # Click on checkout now button
    checkout_now_button = driver.find_element(By.ID, "checkout")
    checkout_now_button.click()
    time.sleep(3)  # Wait 

    # Fill in checkout information
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Daniel")
    last_name_input.send_keys("Mora")
    postal_code_input.send_keys("001")

    time.sleep(4)  # Wait 

    # Click continue button
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    time.sleep(8)  # Wait 

    # Click finish button
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    time.sleep(3)  # Wait 

    # Click back to products button
    back_to_products_button = driver.find_element(By.ID, "back-to-products")
    back_to_products_button.click()
    time.sleep(3)  # Wait 

    print("Checkout process completed successfully.")
except:
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    print("Login failed. Error message:", error_message.text)

driver.quit()