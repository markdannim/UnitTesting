#Test Passed TC#001
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

        # Wait for the gender select element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'type')))
        user_select = driver.find_element(By.NAME, 'type')

        # Use the Select class to work with the dropdown
        select = Select(user_select)

        select.select_by_visible_text("Catcher")
        print("Successfully select user type")

        # Find the firstname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
        firstName = driver.find_element(By.NAME, 'firstName')
        firstName.send_keys('Noel')
        print("Successfully input Firstname")

        # Find the lastname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'lastName')))
        lastName = driver.find_element(By.NAME, 'lastName')
        lastName.send_keys('Musngi')
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

        contact_input = driver.find_element(By.NAME, "contact")
        contact_input.send_keys("09453574232")

        address_input = driver.find_element(By.NAME, "address")
        address_input.send_keys("Consolacion")

        # Find the username and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regUsername')))
        username = driver.find_element(By.NAME, 'regUsername')
        username.send_keys('Noel')
        print("Successfully input Username")

        # Find the lastname and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email = driver.find_element(By.NAME, 'email')
        email.send_keys('ratgel@gmail.com')
        print("Successfully input email")


        # Find the password and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regPassword')))
        password = driver.find_element(By.NAME, 'regPassword')
        password.send_keys('Mirac4321')
        print("Successfully input Password")

        # Find the confirm password and enter the value
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'regPassword2')))
        password2 = driver.find_element(By.NAME, 'regPassword2')
        password2.send_keys('Mirac4321')
        print("Successfully input Confirm Password")

        # Wait for the button to be visible and scroll into view
        sign_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By. CLASS_NAME, "signup-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_button)  # Ensure it's in view

        # Ensure no overlays or pop-ups are in the way
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sign_button))  # Wait until it's clickable
        try:
            sign_button.click()
        except Exception as e:
            # Use JavaScript click as a fallback
            driver.execute_script("arguments[0].click();", sign_button)

        time.sleep(5)

        print("TC-001 Register Account -  Valid Entries - Success")


    except Exception as e:
        print(f"Test Failed: {e}")

