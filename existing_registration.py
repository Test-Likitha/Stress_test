import time
import threading
import psutil
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
log_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "existing_registration_log.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    start_time = time.time()

    # Example login information (replace with your actual data)
    login_info_list = [
        {"login_id": "userkizon30@test.com", "login_pass": "test123"},
        # {"login_id": "userkizon2@test.com", "login_pass": "test123456789"},
        # Add more user data as needed
    ]

    threads = []
    for login_info in login_info_list:
        thread = threading.Thread(target=scenario_one, args=(login_info,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def scenario_one(login_info):
    login_id = login_info["login_id"]
    login_pass = login_info["login_pass"]

    try:
        logging.info(f"User ID {login_id} registration started")
        driver = webdriver.Edge()
        driver.get("https://stg.bjc-online.jp/mypage/login")

        driver.find_element(By.CLASS_NAME, "ec-loginRole__currentMember").click()
        driver.find_element(By.ID, "login_id").send_keys(login_id)
        driver.find_element(By.ID, "login_pass").send_keys(login_pass)
        driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn").click()
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass
        
        driver.find_element(By.CLASS_NAME, "ec-inlineBtn--action").click()

        driver.find_element(By.ID, "entry_plain_password_first").send_keys("test123456789")
        driver.find_element(By.ID, "entry_plain_password_second").send_keys("test123456789")
        driver.find_element(By.ID, "entry_transfer_name").send_keys("test")
        chkbox = driver.find_element(By.ID, "entry_user_policy_check")
        try:
            ac = ActionChains(driver)
            mvelmt= ac.move_to_element(chkbox)

            mvelmt.perform()
        except:
            pass
        while(not chkbox.is_selected()):
            try:
                chkbox.click()
            except:
                pass

        execute_code_block(driver)
        time.sleep(1)
        execute_code_block(driver)

        logging.info(f"User ID {login_id} registration successful")
    except Exception as e:
        logging.error(f"User ID {login_id} registration failed: {e}")
        print(f"An error occurred for {login_id}: {e}")
    finally:
        if driver:
            driver.quit()

def execute_code_block(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()
    except:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()                   

if __name__ == "__main__":
    main()
