# Test Passed TC#002
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#
# # Set up Edge driver options
options = Options()
options.add_argument("--start-maximized")
#
# # Define Edge driver service
service = EdgeService()

# Initialize the WebDriver
with webdriver.Edge(service=service, options=options) as driver:
    try:
        # Navigate to the login page
        driver.get('http://localhost:3000/sign-in')

        # Find the username and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys('Jynxi')
        print("Successfully Input Username")

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')
        print("Successfully Input Password")

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()
        print("Successfully Login")

        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiMenuButton-variantSoft"))
        )
        menu_button.click()
        print("Successfully clicked the profile menu button")

        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Profile"))
        )
        # Click on the link
        profile_link.click()
        print("Successfully clicked 'My Profile'")

        # Wait for the element to become clickable
        unverified_button  = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "UNVERIFIED"))
        )

        # Click the element
        unverified_button.click()
        print("Unverified button clicked successfully")

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":rp:"]'))
        )
        input_field.send_keys("Helper")

        add_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Add']")
        add_button.click()

        time.sleep(5)

        print("UT-010 Profile - Input Skills - Success")

    finally:
        # Close the browser
        driver.quit()