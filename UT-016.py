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


        # Find the password field and enter the value
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Mirac4321')

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='buttonSignin' and text()='Sign In']")
        login_button.click()

        errand_list_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-links" and @href="/dashboard/errands"]'))
        )
        errand_list_link.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Errand']")))

        # Find the button and click it
        add_errand_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add Errand']")
        add_errand_button.click()

        title_field = driver.find_element(By.NAME, 'comTitle')
        title_field.send_keys('Indoor Todays')

        start_date_field = driver.find_element(By.NAME, 'comStart')
        start_date_field.send_keys('20-12-2025')

        end_date_field = driver.find_element(By.NAME, 'comDeadline')
        end_date_field.send_keys('29-12-2025')

        # Wait for the gender select element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'comType')))
        errandtype_select = driver.find_element(By.NAME, 'comType')

        # Use the Select class to work with the dropdown
        select = Select(errandtype_select)

        # Select the option by visible text (e.g., 'Male')
        select.select_by_visible_text("Home Service - Indoor")

        location_field = driver.find_element(By.NAME, 'comLocation')
        location_field.send_keys('Consolacion')

        payment_field = driver.find_element(By.NAME, 'comPay')
        payment_field.send_keys('600')

        contact_field = driver.find_element(By.NAME, 'Contactno')
        contact_field.send_keys('09453574232')

        description_field = driver.find_element(By.NAME, 'comDescription')
        description_field.send_keys('Help my clean my house')

        r5_button = driver.find_element(By.ID, ':r5:')
        r5_button.click()

        skills_button = driver.find_element(By.XPATH, "//li[contains(.,'Plumbing')]")
        skills_button.click()

        # Wait for the button to be visible and scroll into view
        post_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'POST')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", post_button)  # Ensure it's in view

        # Ensure no overlays or pop-ups are in the way
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(post_button))  # Wait until it's clickable
        try:
            post_button.click()
        except Exception as e:
            # Use JavaScript click as a fallback
            driver.execute_script("arguments[0].click();", post_button)
        print("Successfully clicked the save button")

        time.sleep(10)

        print("Post Errand - Success")

    finally:
        # Close the browser
        driver.quit()