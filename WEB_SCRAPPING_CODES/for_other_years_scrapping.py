import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
url = "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"
driver.get(url)

# Increase the wait time
wait = WebDriverWait(driver, 30)

try:
    # Select Year
    print("Selecting Year...")
    year_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlYear_chosen")))
    year_dropdown.click()
    year_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='2019']")))
    year_option.click()
    time.sleep(2)  # Wait for the page to update

    # Select Round No
    print("Selecting Round No...")
    round_no_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")))
    round_no_dropdown.click()
    round_no_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='2']")))
    round_no_option.click()
    time.sleep(2)  # Wait for the page to update

    # Select Institute Type
    print("Selecting Institute Type...")
    institute_type_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")))
    institute_type_dropdown.click()
    institute_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='ALL']")))
    institute_type_option.click()
    time.sleep(2)  # Wait for the page to update

    # Select Institute Name
    print("Selecting Institute Name...")
    institute_name_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")))
    institute_name_dropdown.click()
    institute_name_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='ALL']")))
    institute_name_option.click()
    time.sleep(2)  # Wait for the page to update

    # Select Academic Program
    print("Selecting Academic Program...")
    academic_program_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")))
    academic_program_dropdown.click()
    academic_program_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='ALL']")))
    academic_program_option.click()
    time.sleep(2)  # Wait for the page to update

    # Select Seat Type
    print("Selecting Seat Type...")
    seat_type_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlSeatType_chosen")))
    seat_type_dropdown.click()
    seat_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='ALL']")))
    seat_type_option.click()
    time.sleep(2)  # Wait for the page to update

    # Click the Submit button
    print("Clicking Submit button...")
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")))
    submit_button.click()
    
    # Wait for the results table to load
    print("Waiting for results table...")
    table = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_pnlDisplayDetails")))

    # Extract and save table data to CSV file
    print("Extracting data...")
    rows = table.find_elements(By.TAG_NAME, "tr")
    with open("output1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            data = [col.text for col in cols]
            writer.writerow(data)
    print("Data saved to 2019_R1.csv")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
