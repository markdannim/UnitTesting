#Test Passed TC#002
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
        username_field.send_keys('MarkDaniel')
        print("Successfully Input Username")


        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')
        print("Successfully Input Password")

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()
        print("Successfully Login")

        errand_list_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-links" and @href="/dashboard/errands"]'))
        )
        errand_list_link.click()

        # Wait for the button with the "View" link to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//a[normalize-space()='View']")))

        # Find the button and click it
        view_button = driver.find_element(By.XPATH, "//button[@type='button']//a[normalize-space()='View']")
        view_button.click()

        print("Successfully clicked the 'View' button.")

        # Wait for the button to be visible and scroll into view
        updates_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'UPDATE')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", updates_button)  # Ensure it's in view

        # Ensure no overlays or pop-ups are in the way
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(updates_button))  # Wait until it's clickable
        try:
            updates_button.click()
        except Exception as e:
            # Use JavaScript click as a fallback
            driver.execute_script("arguments[0].click();", updates_button)
        print("Successfully clicked the update button")

        time.sleep(10)

        print("Update Errand - Success")

    finally:
        # Close the browser
        driver.quit()