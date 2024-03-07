from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to test login for a given username
def test_login(username):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Find username, password, and login button elements
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Enter credentials and click login
    username_field.send_keys(username)
    password_field.send_keys("secret_sauce")

    time.sleep(2)  # Wait

    login_button.click()

    try:
        # Wait until inventory container is visible
        inventory_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )
        print(f"Login successful for {username}")
    except:
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        print(f"Login failed for {username}. Error message: {error_message.text}")

    driver.quit()

# List of users to test
users_to_test = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
    "userexampleforme"
]

# Test login for each user
for user in users_to_test:
    test_login(user)