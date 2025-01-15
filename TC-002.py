# Test Passed TC#001
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/sign-up']")))
        sign_up = driver.find_element(By.XPATH, "//a[@href='/sign-up']")
        sign_up.click()
        print("Successfully click sign up")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='wrapper-Catcher']")))
        sign_up = driver.find_element(By.XPATH, "//div[@id='wrapper-Catcher']")
        sign_up.click()

        join_button = driver.find_element(By.XPATH, "//button[text()='Join as Catcher']")
        join_button.click()
        print("Successfully click Join as Catcher")

        # Find the firstname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
        firstName = driver.find_element(By.NAME, 'firstName')
        firstName.send_keys('Tanner')
        print("Successfully input Firstname")

        # Find the lastname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'lastName')))
        lastName = driver.find_element(By.NAME, 'lastName')
        lastName.send_keys('Newland')
        print("Successfully input Lastname")

        # Find the birthday and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'bday')))
        bday = driver.find_element(By.NAME, 'bday')
        bday.send_keys('01-01-2000')
        print("Successfully input Birthday")

        # Wait for the gender select element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'gender')))
        gender_select = driver.find_element(By.NAME, 'gender')

        # Use the Select class to work with the dropdown
        select = Select(gender_select)

        # Select the option by visible text (e.g., 'Male')
        select.select_by_visible_text("Male")
        print("Successfully select Gender")

        # # Optionally, verify the selected value
        # assert select.first_selected_option.get_attribute('value') == 'Male', "Gender was not selected correctly"

        # Find the username and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regUsername')))
        username = driver.find_element(By.NAME, 'regUsername')
        username.send_keys('Caseoh')
        print("Successfully input Username")

        # Find the lastname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email = driver.find_element(By.NAME, 'email')
        email.send_keys('iamskinny@gmail.com')
        print("Successfully input email")

        # Find the password and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regPassword')))
        password = driver.find_element(By.NAME, 'regPassword')
        password.send_keys('Mirac4321')
        print("Successfully input Password")

        # Find the confirm password and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regPassword2')))
        password2 = driver.find_element(By.NAME, 'regPassword2')
        password2.send_keys('Mirac432')
        print("Succesfully input Confirm Password")

        # # Wait for the "Sign in" link to be present
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/sign-in']")))
        # sign_in_link = driver.find_element(By.XPATH, "//a[@href='/sign-in']")
        # sign_in_link.click()

        # Locate and click the "Sign Up" button
        sign_up_button = driver.find_element(By.CLASS_NAME, 'signup-button')
        sign_up_button.click()

        time.sleep(2)

        print("UT-002 Register Account - Invalid Entries - Success")

    except Exception as e:
        print(f"Test Failed: {e}")

