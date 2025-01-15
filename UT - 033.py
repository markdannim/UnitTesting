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
        email_field.send_keys('Employer')

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        # Wait for the element matching the CSS Selector to become clickable
        target_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-1d159sf-MuiSvgIcon-root > path'))
        )

        # Perform a click action
        target_element.click()
        print("Notification Button Clicked")

        # Wait for the button defined by the CSS selector to be clickable
        target_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-16c77hi > .MuiButton-root'))
        )

        # Click the button
        target_button.click()
        print("Button clicked successfully")

        # Wait for the third notification SVG icon to be clickable
        svg_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.notification-item:nth-child(3) .MuiSvgIcon-root'))
        )

        # Click the SVG icon
        svg_icon.click()
        print("SVG icon in the third notification clicked successfully!")

        time.sleep(5)

        print("UT-033 - Mark as Read - Success")

    finally:
        # Close the browser
        driver.quit()