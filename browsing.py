from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import random

def main(num_users):
    threads = []

    for _ in range(num_users):
        thread = threading.Thread(target=browsing_scenario)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def browsing_scenario():
    try:
        driver = webdriver.Edge()  
        login(driver, "l-shankar@ar-system.co.jp", "test123456789")
        close_image_popup(driver)
        navigate_to_all_products(driver)
        
        for _ in range(3):
            select_and_interact_with_product(driver)
            
        navigate_to_bjc_charis(driver)
        # navigate_to_seminar_page(driver)
        # close_image_popup(driver)
        # read_more(driver)
        navigate_to_qa(driver)
        scroll_down(driver)
        scroll_up(driver)
        navigate_to_bjc_charis(driver)
        logout(driver)

    except Exception as e:
        print("Browsing scenario failed:", e)

    finally:
        driver.quit()

def login(driver, email, password):
    try:
        driver.get("https://stg.bjc-online.jp/mypage/login")

        login_email = driver.find_element(By.ID, "login_email")
        login_pass = driver.find_element(By.ID, "login_pass")
        login_button = driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn")

        login_email.send_keys(email)
        login_pass.send_keys(password)
        login_button.click()

        time.sleep(3) 

    except Exception as e:
        print("Login failed:", e)
        raise e


def close_image_popup(driver):
    try:
        close_image = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='閉じる']"))
        )
        close_image.click()
        print("Closed image popup successfully.")
    except Exception as e:
        print("Failed to close image popup:", e)

def navigate_to_all_products(driver):
    try:
        driver.get("https://stg.bjc-online.jp/products/list")
    except Exception as e:
        print("Failed to navigate to all products:", e)

def select_and_interact_with_product(driver):
    try:
        product_link = driver.find_element(By.CLASS_NAME, "ec-shelfBlock__item-image")
        product_link.click()

        scroll_down(driver)
        scroll_up(driver)

        driver.back()
    except Exception as e:
        print("Failed to interact with product:", e)

def navigate_to_bjc_charis(driver):
    try:
        bjc_charis_link = driver.find_element(By.XPATH, "//img[@alt='BJC CHARIS&Co. ONLINESTORE']")
        bjc_charis_link.click()
    except Exception as e:
        print("Failed to navigate to BJC CHARIS:", e)

def navigate_to_seminar_page(driver):
    try:
        seminar_link = driver.find_element(By.XPATH, "//img[@alt='講習会セミナー']")
        seminar_link.click()
    except Exception as e:
        print("Failed to navigate to seminar page:", e)

def read_more(driver):
    try:
        read_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Read more')]")
        read_more_button.click()
    except Exception as e:
        print("Failed to click on 'Read more':", e)

def navigate_to_qa(driver):
    try:
        driver.get("https://stg.bjc-online.jp/faq_list")
    except Exception as e:
        print("Failed to navigate to Q&A:", e)

def scroll_down(driver):
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)  

def scroll_up(driver):
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_UP).perform()
    time.sleep(1) 

def logout(driver):
    try:
        driver.get("https://stg.bjc-online.jp/logout")
        # logout_link = driver.find_element(By.CLASS_NAME, "ec-headerMenu__item logout")
        # logout_link.click()
    except Exception as e:
        print("Failed to logout:", e)

if __name__ == "__main__":
    num_users_to_run = 1  #  users: 1 to 20
    main(num_users_to_run)
