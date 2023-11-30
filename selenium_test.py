#import selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

ADMIN_NAME = "123@gmail.com"
ADMIN_PW = "123"
WAIT_DURATION = 3

# Path encoding, 'extend' variable
# 0: Login only
# 1: Admin credentials
# 2: Business credentials
# 3: Contractor credentials

def wait():
    # universal wait function to observe steps being taken throughout scripts
    time.sleep(WAIT_DURATION)

def login(email, password, extend):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    title = driver.title
    actions = ActionChains(driver)

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "btnLogin")
    actions.move_to_element(login_button).perform()

    ## conditional statements chcecking for 'extend == 0' only to execute if showing login functionality 
    ## meant to skip if navigating to other pages
    if (extend == 0):
        wait()  
    login_button.click()
    if (extend == 0):
        wait()
    if (extend == 1 and email == ADMIN_NAME and password == ADMIN_PW):
        adminAssignJob(driver, actions)

def register(fname, lname, email, password, phone, company, website, contractorChoice):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/register")
    title = driver.title
    actions = ActionChains(driver)

    fname_input = driver.find_element(By.NAME, 'FirstName')
    fname_input.send_keys(fname)

    lname_input = driver.find_element(By.NAME, 'LastName')
    lname_input.send_keys(lname)

    email_input = driver.find_element(By.NAME, 'Email')
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, 'Password')
    password_input.send_keys(password)

    phone_input = driver.find_element(By.NAME, 'Phone')
    phone_input.send_keys(phone)

    company_input = driver.find_element(By.NAME, 'Company')
    company_input.send_keys(company)

    website_input = driver.find_element(By.NAME, 'Website')
    website_input.send_keys(website)

    dropdown_element = driver.find_element(By.ID, "Registration_Type__c")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(contractorChoice)
    # index 1 = "Interested in contracting Titan Construction Partners"
    # index 2 = "Interested in becomoing a Titan Construction Partner"

    time.sleep(5)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

def adminAssignJob(driver, actions):
    assign_button = driver.find_element(By.CLASS_NAME, "assignButton")
    assign_button.click()
    wait()
    
    dropdown_element = driver.find_element(By.CLASS_NAME, "contractorsDropdown")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(2)
    wait()

    confirm_button = driver.find_element(By.CLASS_NAME, "confirmButton")
    confirm_button.click()

    wait(); wait()

## BEGIN TESTING ##

# admin job assignment
# login(ADMIN_NAME, ADMIN_PW, 1)

# admin login attempt
# login("123@gmail.com","123", 0)

# registration attempt for new contractor
# register("registerTestFname", "registerTestLname", "registerTestEmail@gmail.com", "registerTestPassword",
            #9165550147, "registerTestCompany", "registerTestWebsite.com", 1)

# registration attempt for a new company
# register("testCompany", "One", "testCompany@gmail.com", "pw123", "9165550147", "testCompany", "testCompany.com", 2)

# login attempt for above company
# login("testCompany@gmail.com", "pw123", 0)

# login attempt with valid credentials
# login("test@gmail.com", "test123", 0)

# login attempt with incorrect password
# login("test@gmail.com", "nicetry", 0)

# login attempt with invalid credentials
# login("hacker@gmail.com", "givemeyourinfo", 0)
