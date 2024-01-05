from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time
import random 
import logging 
import os

log_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "addCart_log.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(message)s")

login_credentials = [
    {"email": "user1000@test.com", "password": "test123456789"},
    {"email": "user1001@test.com", "password": "test123456789"},
    {"email": "user1002@test.com", "password": "test123456789"},
    {"email": "user1003@test.com", "password": "test123456789"},
    {"email": "user1004@test.com", "password": "test123456789"},
    {"email": "user1005@test.com", "password": "test123456789"},
    {"email": "userkizon1@test.com", "password": "test123456789"},
    {"email": "userkizon2@test.com", "password": "test123456789"},
    {"email": "userkizon3@test.com", "password": "test123456789"},
    {"email": "userkizon4@test.com", "password": "test123456789"},
    {"email": "userkizon5@test.com", "password": "test123456789"},
    {"email": "userkizon6@test.com", "password": "test123456789"},
    {"email": "userkizon7@test.com", "password": "test123456789"},
    {"email": "userkizon8@test.com", "password": "test123456789"},
    {"email": "userkizon9@test.com", "password": "test123456789"},
]


def main(num_users):
    threads = []

    for i in range(num_users):
        thread = threading.Thread(target=browsing_scenario, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def browsing_scenario(user_index):
    try:
        temp = login_credentials[user_index % len(login_credentials)]
        logging.info(f"User ID {temp["email"]} browsing scenario started")
        driver = webdriver.Edge()  
        login(driver, user_index)
        add_products_to_cart(driver, 50)
        logout(driver)
        
        # click_on_image(driver)
        logging.info(f"User ID {temp["email"]} browsing scenario successful")
    except Exception as e:
        print(f"Scenario for user {temp["email"]} failed:", e)
        logging.error(f"User ID {temp["email"]} browsing scenario failed: {e}")
    finally:
        if driver:
            driver.quit()

def login(driver, user_index):
    try:
        driver.get("https://stg.bjc-online.jp/mypage/login")
        credentials = login_credentials[user_index % len(login_credentials)]
        login_email = driver.find_element(By.ID, "login_email")
        login_pass = driver.find_element(By.ID, "login_pass")
        login_button = driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn")

        login_email.send_keys(credentials["email"])
        login_pass.send_keys(credentials["password"])
        login_button.click()

        time.sleep(2)
    except Exception as e:
        print(f"Login for user {user_index + 1} failed:", e)

def click_on_image(driver):
    try:
        image = driver.find_element(By.XPATH, "//img[@alt='BJC CHARIS&Co. ONLINESTORE']")
        image.click()
    except Exception as e:
        print("Failed to click on the image:", e)

def add_products_to_cart(driver, num_products):
    try:
        driver.get("https://stg.bjc-online.jp/products/list")

        try:
            for _ in range(num_products):
                add_to_cart(driver)
                handle_error_message(driver)
        except:
            pass        

        driver.get("https://stg.bjc-online.jp/cart")

        for _ in range(1):
            click_cart_row_buttons(driver)
            # change_delivery_date(driver)

        driver.get("https://stg.bjc-online.jp/mypage/")
        click_history_list_header(driver)
        time.sleep(2)
        driver.refresh()
        driver.get("https://stg.bjc-online.jp/mypage/")
        time.sleep(2)

        driver.get("https://stg.bjc-online.jp/logout")
        print(f"Scenario for user completed successfully.")

    except Exception as e:
        print(f"An error occurred for user ", e)

def add_to_cart(driver):
    try:
        add_cart_button = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action.add-cart")
        add_cart_button.click()
        time.sleep(2)
        chkbox = driver.find_element(By.ID, "lash-agreement-checkbox")
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
        driver.find_element(By.CLASS_NAME, "button undefined").click()
    except:
        driver.refresh()

def handle_error_message(driver):
    driver.refresh()

def click_cart_row_buttons(driver):
    try:
        confirm_box_overlay = driver.find_element(By.ID, "confirmBox")
        driver.execute_script("arguments[0].scrollIntoView();", confirm_box_overlay)

        undefined_button = confirm_box_overlay.find_element(By.CLASS_NAME, "button.undefined")
        undefined_button.click()
        print("Clicked on undefined button in confirmBox overlay.")
    except:
        pass

    try:
       cart_button = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action")
       cart_button.click()
    except:
        driver.get("https://stg.bjc-online.jp/shopping")

        cart_button = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action")
        cart_button.click()

def change_delivery_date(driver):
    change_button = driver.find_element(By.CLASS_NAME, "ec-orderDelivery__change")
    change_button.click()
    time.sleep(1)

    cancel_button = driver.find_element(By.CLASS_NAME, "ec-blockBtn--cancel")
    cancel_button.click()

    try:
        dropdown = driver.find_element(By.ID, "shopping_order_Shippings_0_shipping_delivery_date")
        options = dropdown.find_elements(By.TAG_NAME, "option")
        random_option = random.choice(options)
        random_option.click()
    except:
        pass

    try:
        action_buttons = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action")
        action_buttons.click()
        time.sleep(1)
    except:
        pass

    try:
        # action_buttons = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action")
        # action_buttons.click()
        time.sleep(1)
    except:
        pass

def click_history_list_header(driver):
    history_button = driver.find_element(By.CLASS_NAME, "ec-inlineBtn")
    history_button.click()

def logout(driver):
    try:
        driver.get("https://stg.bjc-online.jp/logout")
    except Exception as e:
        print("Failed to logout:", e)

if __name__ == "__main__":
    num_users_to_run = 1  # number of users
    main(num_users_to_run)
