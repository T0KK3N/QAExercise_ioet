from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to check for XSS vulnerability
def check_xss_vulnerability(driver):
    # Open the webpage
    driver.get("https://www.saucedemo.com/")

    # Inject XSS payload with JavaScript
    script = "<script>alert('XSS Vulnerability Found');</script>"
    driver.execute_script(f'document.getElementById("password").value = "{script}"')
    driver.find_element(By.ID, "login-button").click()

    # Check if the alert popup appears
    try:
        alert = driver.switch_to.alert
        print("XSS Vulnerability Detected!")
        alert.accept()
    except:
        print("No XSS Vulnerability Detected.")

# Initialize the WebDriver
driver = webdriver.Chrome()

# Perform XSS vulnerability check
check_xss_vulnerability(driver)

# Close the WebDriver
driver.quit()