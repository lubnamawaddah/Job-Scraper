import pandas as pd
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Function to scrape Site 1 (Jobstreet)
def scrape_site_1(result_list, keyword, driver_path):
    # Create dynamic URL based on keyword
    base_url = "https://id.jobstreet.com/id/"
    search_url = f"{base_url}{keyword.replace(' ', '-').lower()}-jobs"
    
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(search_url)

    job_name = []
    job_company = []
    job_location = []
    job_salary = []
    job_uploaded = []
    job_url = []
    
    # Extract data based on site structure
    jobs = driver.find_elements(by=By.XPATH, value='//article[@data-automation="normalJob"]')
    
    for job in jobs:
        try:
            job_name.append(job.find_element(by=By.XPATH, value='.//a[@data-automation="jobTitle"]').text)
        except NoSuchElementException:
            job_name.append("Position not displayed")
        
        try:
            job_company.append(job.find_element(by=By.XPATH, value='.//a[@data-automation="jobCompany"]').text)
        except NoSuchElementException:
            job_company.append("Company not displayed")
        
        try:
            job_location.append(job.find_element(by=By.XPATH, value='.//a[@data-automation="jobLocation"]').text)
        except NoSuchElementException:
            job_location.append("Location not displayed")
        
        try:
            job_salary.append(job.find_element(by=By.XPATH, value='.//span[@data-automation="jobSalary"]').text)
        except NoSuchElementException:
            job_salary.append("Salary not displayed")

        try:
            job_uploaded.append(job.find_element(by=By.XPATH, value='.//span[@data-automation="jobListingDate"]').text)
        except NoSuchElementException:
            job_uploaded.append("Upload time not displayed")

        try:
            job_url.append(job.find_element(by=By.XPATH, value='.//a[@data-automation="jobTitle"]').get_attribute('href'))
        except NoSuchElementException:
            job_url.append("Link not displayed")

    driver.quit()
    
    result_list.append(pd.DataFrame({
        'Position': job_name, 
        'Company': job_company, 
        'Location': job_location, 
        'Salary': job_salary, 
        'Upload Time': job_uploaded, 
        'Link': job_url,
        'Site': 'Jobstreet'
    }))

# Function to scrape Site 2 (Loker.id)
def scrape_site_2(result_list, keyword, driver_path):
    # Create dynamic URL based on keyword
    base_url = "https://www.loker.id/cari-lowongan-kerja"
    search_url = f"{base_url}?q={keyword.replace(' ', '+')}"
    
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(search_url)

    job_name = []
    job_company = []
    job_location = []
    job_salary = []
    job_uploaded = []
    job_url = []
    
    # Extract data based on site structure
    jobs = driver.find_elements(by=By.XPATH, value='//div[contains(@class, "job-box")]')
    
    for job in jobs:
        try:
            job_name.append(job.find_element(by=By.XPATH, value='.//a[@title="Lihat detail lowongan"]').text)
        except NoSuchElementException:
            job_name.append("Position not displayed")
        
        try:
            job_company.append(job.find_element(By.CLASS_NAME, 'media-body').text.split('\n')[-1].strip())
        except NoSuchElementException:
            job_company.append("Company not displayed")

        try:
            job_location.append(job.find_element(by=By.XPATH, value='.//td[@class="padding-0" and not(contains(text(), "Rp")) and not(contains(text(), "Negosiasi"))]').text)
        except NoSuchElementException:
            job_location.append("Location not displayed")

        try:
            job_salary.append(job.find_element(by=By.XPATH, value='.//td[@class="padding-0" and contains(text(), "Rp")]').text)
        except NoSuchElementException:
            job_salary.append("Salary not displayed")

        job_uploaded.append("Upload time not displayed")

        try:
            job_url.append(job.find_element(by=By.XPATH, value='.//a[@title="Lihat detail lowongan"]').get_attribute('href'))
        except NoSuchElementException:
            job_url.append("Link not displayed")

    driver.quit()
    
    result_list.append(pd.DataFrame({
        'Position': job_name, 
        'Company': job_company, 
        'Location': job_location, 
        'Salary': job_salary, 
        'Upload Time': job_uploaded, 
        'Link': job_url,
        'Site': 'Loker.id'
    }))

# Function to scrape Site 3 (Kalibrr)
def scrape_site_3(result_list, keyword, driver_path):
    # Create dynamic URL based on keyword
    base_url = "https://www.kalibrr.id/home/te"
    search_url = f"{base_url}/{keyword.replace(' ', '-')}"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(search_url)

    job_name = []
    job_company = []
    job_location = []
    job_salary = []
    job_uploaded = []
    job_url = []
    
    # Extract data based on site structure
    jobs = driver.find_elements(by=By.XPATH, value='//div[contains(@class, "k-font-dm-sans k-rounded-lg k-bg-white k-border-solid k-border hover:k-border-2 hover:k-border-primary-color k-border k-group k-flex k-flex-col k-justify-between css-1otdiuc")]')
    
    for job in jobs:
        try:
            job_name.append(job.find_element(by=By.XPATH, value='.//a[contains(@class, "k-text-black")]').text)
        except NoSuchElementException:
            job_name.append("Position not displayed")
        
        try:
            job_company.append(job.find_element(by=By.XPATH, value='.//a[contains(@class, "k-text-subdued k-font-bold")]').text)
        except NoSuchElementException:
            job_company.append("Company not displayed")
        
        try:
            job_location.append(job.find_element(by=By.XPATH, value='.//span[contains(@class, "k-text-gray-500 k-block k-pointer-events-none")]').text)
        except NoSuchElementException:
            job_location.append("Location not displayed")
        
        try:
            job_salary.append(job.find_element(by=By.XPATH, value='.//span[contains(@class, "k-text-subdued")]').text)
        except NoSuchElementException:
            job_salary.append("Salary not displayed")

        try:
            job_uploaded.append(job.find_element(by=By.XPATH, value='.//span[contains(@class, "k-text-gray-500") and contains(text(), "Recruiter was hiring")]').text)
        except NoSuchElementException:
            job_uploaded.append("Upload time not displayed")

        try:
            job_url.append(job.find_element(by=By.XPATH, value='.//a[contains(@class, "k-text-black")]').get_attribute('href'))
        except NoSuchElementException:
            job_url.append("Link not displayed")

    driver.quit()
    
    result_list.append(pd.DataFrame({
        'Position': job_name, 
        'Company': job_company, 
        'Location': job_location, 
        'Salary': job_salary, 
        'Upload Time': job_uploaded, 
        'Link': job_url,
        'Site': 'Kalibrr'
    }))

# Function to run scraping with threading (parallel)
def scrape_with_threading(selected_sites, keyword, driver_path):
    result_list = []
    threads = []
    
    # Start time of scraping
    start_time = time.time()
    
    # Mapping sites to scraping functions
    site_functions = {
        "Jobstreet": scrape_site_1,
        "Loker.id": scrape_site_2,
        "Kalibrr": scrape_site_3
    }

    # Create and start threads based on selected sites
    for site in selected_sites:
        if site in site_functions:
            thread = threading.Thread(target=site_functions[site], args=(result_list, keyword, driver_path))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # End time of scraping
    end_time = time.time()
    
    # Calculate scraping duration in seconds
    scraping_duration = end_time - start_time
    
    # Combine all scraping results
    final_result = pd.concat(result_list, ignore_index=True)
    
    # Check if result is empty
    if final_result.empty:
        return None, scraping_duration
    
    return final_result, scraping_duration