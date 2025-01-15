#Test Passed TC#10
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
        email_field.send_keys('MarkDaniel')

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        # Wait for the input field to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inputsss")))

        # Find the input field and input text
        search_field = driver.find_element(By.CLASS_NAME, "inputsss")
        search_field.clear()  # Clear any existing text
        search_field.send_keys("Drive")

        # Wait for the button to be present and clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='buttonss']")))

        # Find the button and click it
        search_button = driver.find_element(By.XPATH, "//button[@class='buttonss']")
        search_button.click()
        print("Successfully Search")

        # # Wait for the inner "Find out more" link to be clickable
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardnew:nth-child(1) .action")))
        #
        # # Scroll into view to ensure the element is visible
        # find_out_more_link = driver.find_element(By.CSS_SELECTOR, ".cardnew:nth-child(1) .action")
        # driver.execute_script("arguments[0].scrollIntoView(true);", find_out_more_link)
        #
        # # Add an additional check to ensure the element is interactable
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardnew:nth-child(1) .action")))
        #
        # # Attempt to click the element (if this fails, use JavaScript as a fallback)
        # try:
        #     find_out_more_link.click()
        # except Exception as e:
        #     # Use JavaScript click as a fallback
        #     driver.execute_script("arguments[0].click();", find_out_more_link)

        # # Wait for the button to be clickable
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='formButton' and text()='APPLY']")))
        #
        # # Find the button and click it
        # apply_button = driver.find_element(By.XPATH, "//button[@class='formButton' and text()='APPLY']")
        # # apply_button.click()

        time.sleep(10)
        print("UT-019 - Search Errand - Success")

    finally:
        # Close the browser
        driver.quit()