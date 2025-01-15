# Test Passed TC#002
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pynput.keyboard import Key, Controller
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
        print("Add skills successfully")

        # Wait for the button to be visible and scroll into view
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btnn"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)  # Ensure it's in view

        # Ensure no overlays or pop-ups are in the way
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(next_button))  # Wait until it's clickable
        try:
            next_button.click()
        except Exception as e:
            # Use JavaScript click as a fallback
            driver.execute_script("arguments[0].click();", next_button)
        print("Successfully clicked the save button")
        # next_button = driver.find_element(By.CLASS_NAME, "btnn")
        # next_button.click()

        # Wait for the label with the 'for' attribute to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='fileInput1']")))

        # Find the label and click it
        choose_image_label = driver.find_element(By.XPATH, "//label[@for='fileInput1']")
        choose_image_label.click()

        keyboard = Controller()
        keyboard.type("C:\\Users\\User\\PycharmProjects\\PythonProject2\\front.jpg")

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("Image uploaded successfully")

        # Wait for the label with the 'for' attribute to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='fileInput2']")))

        # Find the label and click it
        choose_image_labels = driver.find_element(By.XPATH, "//label[@for='fileInput2']")
        choose_image_labels.click()

        keyboard1 = Controller()
        keyboard1.type("C:\\Users\\User\\PycharmProjects\\PythonProject2\\back.jpg")

        keyboard1.press(Key.enter)
        keyboard1.release(Key.enter)

        print("Image uploaded successfully")


        time.sleep(5)

        print("UT-011 Profile - Upload Identification - Success")

    finally:
        # Close the browser
        driver.quit()