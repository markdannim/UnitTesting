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
        email_field.send_keys('MarkDaniel')

        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        # Wait for the link to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/dashboard/c-map']")))

        # Find the link using the href attribute and click it
        errands_link = driver.find_element(By.XPATH, "//a[@href='/dashboard/c-map']")
        errands_link.click()
        print("Successfully clicked map")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "maplibregl-ctrl-geolocate")))
        map_pointer = driver.find_element(By.CLASS_NAME, "maplibregl-ctrl-geolocate")
        map_pointer.click()
        print("Successfully clicked map pointer")

        # Wait for the gender select element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'type')))
        errand_select = driver.find_element(By.NAME, 'type')

        ## Use the Select class to work with the dropdown
        #select = Select(errand_select)

        # Select the option by visible text (e.g., 'Home Service')
        # select.select_by_visible_text("Home Service")
        # print("Successfully selected Home Service")
        #
        # select.select_by_visible_text("Delivery")
        # print("Successfully selected Delivery")
        #
        # select.select_by_visible_text("Transportations")
        # print("Successfully selected Transportations")

        # Wait for the slider element to be present
        #slider = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'proximity')))

        # Change the slider value using JavaScript
        # new_value = 1  # Set the desired value (must be within min & max)
        # driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
        #                       slider,
        #                       new_value)

        # new_value = 1
        # for _ in range(3):  # Retry setting the value
        #     driver.execute_script("""
        #         arguments[0].value = arguments[1];
        #         arguments[0].dispatchEvent(new Event('input'));
        #         arguments[0].dispatchEvent(new Event('change'));
        #     """, slider, new_value)
        #     sleep(0.5)  # Wait for the application to stabilize

        # Optionally, verify the value has been updated successfully
        # updated_value = slider.get_attribute('value')
        # assert updated_value == str(
        #     new_value), f"Slider value not updated. Expected {new_value}, but got {updated_value}"
        #
        # print(f"Slider updated successfully to {updated_value}")

        time.sleep(10)
        print("UT-022 - View Map - Success")


    except Exception as e:
        print(f"Test Failed: {e}")