#Test Passed TC#006
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
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
        email_field.send_keys('Employer')

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        # Wait for the anchor element to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-links[href='/dashboard/applicants']")))

        # Find the anchor element and click it
        applicant_link = driver.find_element(By.CSS_SELECTOR, "a.nav-links[href='/dashboard/applicants']")
        applicant_link.click()

        # Wait for the button with text "Accept" to be clickable
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept"]'))
        )

        # Click the "Accept" button
        accept_button.click()
        print("Accept button clicked successfully")

        time.sleep(10)
        print("Accept Applicant - Success")


    except Exception as e:
        print(f"Test Failed: {e}")