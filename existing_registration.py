import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def main():
    start_time = time.time()
    csv_file_path = r'C:\Users\Likitha Shankar\Desktop\bjc_ec_stress_test\csv\existing_member_list.csv'

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header

        for row in csv_reader:
            login_id = row[0]
            login_pass = row[1]

            driver = webdriver.Edge()  
            try:
                driver.get("https://stg.bjc-online.jp/mypage/login")

                driver.find_element(By.CLASS_NAME, "ec-loginRole__currentMember").click()
                driver.find_element(By.ID, "login_id").send_keys(login_id)
                driver.find_element(By.ID, "login_pass").send_keys(login_pass)
                driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn").click()
                try:
                    error_message = driver.find_elements(By.CLASS_NAME, "ec-loginRole__formMsg")
                    if error_message:
                        print(f"Login failed for {login_id}, trying next credentials.")
                        continue
                except:
                    pass    

                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                except:
                    pass
                
                driver.find_element(By.CLASS_NAME, "ec-inlineBtn--action").click()

                driver.find_element(By.ID, "entry_plain_password_first").send_keys("test123456789")
                driver.find_element(By.ID, "entry_plain_password_second").send_keys("test123456789")
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

            except Exception as e:
                print(f"An error occurred for {login_id}: {e}")

            finally:
                driver.quit()

def execute_code_block(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()
    except:
        driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()                   

if __name__ == "__main__":
    main()
