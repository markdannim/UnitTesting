#Test Passed TC#004
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

        # Find the email or nationality field and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        email_field = driver.find_element(By.NAME, 'username')
        email_field.send_keys('Admin')

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        # Wait for the link to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/dashboard/admin/request']")))

        # Find the link using the href attribute and click it
        errands_link = driver.find_element(By.XPATH, "//a[@href='/dashboard/admin/request']")
        errands_link.click()

        # Wait for the button to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Action']")))

        # Find the button using XPath and click it
        action_button = driver.find_element(By.XPATH, "//button[text()='Action']")
        action_button.click()

        # Wait for the button to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Verify']")))

        # Find the button using XPath and click it
        verify_button = driver.find_element(By.XPATH, "//button[text()='Verify']")
        verify_button.click()

        # Wait for the button to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Yes']")))

        # Find the button using XPath and click it
        yes_button = driver.find_element(By.XPATH, "//button[text()='Yes']")
        yes_button.click()

        time.sleep(5)
        print("UT-013 - Verify Account - Success")

    finally:
        # Close the browser
        driver.quit()