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

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tr:nth-child(1) .MuiButtonGroup-root path")))

        # Find the element and click it
        delss_element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .MuiButtonGroup-root path")
        delss_element.click()
        print("Successfully clicked the 'Delete' button.")

        delete_button = driver.find_element(By.CSS_SELECTOR, ".MuiModal-root:nth-child(5) .MuiButton-root:nth-child(1)")
        delete_button.click()

        time.sleep(10)

        print("Deleted Errand - Success")

    finally:
        # Close the browser
        driver.quit()