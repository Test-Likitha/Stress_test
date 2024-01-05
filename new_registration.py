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
log_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "new_registration_log.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(message)s")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
report_file_path = os.path.join(desktop_path, "load_report.txt")

def main():
    start_time = time.time()
    num_users = 1091
    login_info = [(f"user{i}@test.com", f"password{i}!!!!") for i in range(1091, num_users + 1)]
    threads = []
    for i, (username, password) in enumerate(login_info, start=1):
        thread = threading.Thread(target=scenario_one, args=(i, username, password))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    cpu_consumption = psutil.cpu_percent()

    with open(report_file_path, "w") as report_file:
        report_file.write(f"Time to complete all executions: {elapsed_time:.2f} seconds\n")
        report_file.write(f"CPU consumption: {cpu_consumption}%\n")

def scenario_one(user_id, email, password):
    try:
        logging.info(f"User mail {email} registration started")
        driver = webdriver.Edge()
        # driver.get("https://dev-admin.bjc-online.jp/entry")
        driver.get("https://stg.bjc-online.jp/entry")

        driver.find_element(By.CLASS_NAME, "ec-inlineBtn--action").click()
        driver.find_element(By.ID,"entry_email").send_keys(email)
        driver.find_element(By.ID,"entry_order_complete_email").send_keys(email)
        driver.find_element(By.ID,"entry_shipping_email").send_keys(email)
        driver.find_element(By.ID,"entry_invoice_send_email").send_keys(email)
        driver.find_element(By.ID,"entry_product_inventory_notification_email").send_keys(email)
        driver.find_element(By.ID,"entry_contract_send_email").send_keys(email)
        driver.find_element(By.ID, "entry_plain_password_first").send_keys(password)
        driver.find_element(By.ID, "entry_plain_password_second").send_keys(password)
        driver.find_element(By.ID, "entry_salon_name").send_keys("salonName")
        driver.find_element(By.ID, "entry_salon_kana").send_keys("ア")
        driver.find_element(By.ID, "entry_salon_phone_number").send_keys("123")
        textarea = driver.find_element(By.ID, "entry_salon_postal_code")
        textarea.send_keys("1000005")
        textarea.send_keys(Keys.ENTER)
        driver.find_element(By.ID, "entry_salon_address_salon_addr02").send_keys("1-2")
        textarea = driver.find_element(By.ID, "entry_postal_code")
        textarea.send_keys("1000005")
        textarea.send_keys(Keys.ENTER)
        driver.find_element(By.ID, "entry_address_addr02").send_keys("1-2")
        textarea = driver.find_element(By.ID, "entry_CustomerAddresses_0_postal_code")
        textarea.send_keys("1000005")
        textarea.send_keys(Keys.ENTER)
        driver.find_element(By.ID, "entry_CustomerAddresses_0_address_addr02").send_keys("1-2")
        driver.find_element(By.ID, "entry_name_name01").send_keys("salonName")
        driver.find_element(By.ID, "entry_name_name02").send_keys("salonName")
        driver.find_element(By.ID, "entry_kana_kana01").send_keys("ア")
        driver.find_element(By.ID, "entry_kana_kana02").send_keys("ア")
        driver.find_element(By.ID, "entry_phone_number").send_keys("123")
        driver.find_element(By.ID, "entry_CustomerAddresses_0_company_name").send_keys("salonName")
        driver.find_element(By.ID, "entry_CustomerAddresses_0_phone_number").send_keys("123")
        driver.find_element(By.ID, "entry_salon_regular_holiday").send_keys("salonName")
        driver.find_element(By.ID, "entry_location_confirmation_content").send_keys("salonName")
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

        logging.info(f"User mail {email} registration successful")
        driver.close()
        time.sleep(2)

    except Exception as e:
        logging.error(f"User mail {email} registration failed: {e}")
        with open(report_file_path, "a") as report_file:
            report_file.write(f"シナリオでエラーが発生しました: {e}\n")

def execute_code_block(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()
    except:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()

if __name__ == "__main__":
    main()
