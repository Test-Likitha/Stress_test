from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import random

def main(user_credentials):
    threads = []

    for credentials in user_credentials:
        thread = threading.Thread(target=browsing_scenario, args=(credentials,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def browsing_scenario(credentials):
    try:
        driver = webdriver.Edge()
        login(driver, credentials[0], credentials[1])
        close_image_popup(driver)
        navigate_to_all_products(driver)

        for _ in range(3):
            select_and_interact_with_product(driver)

        navigate_to_bjc_charis(driver)
        navigate_to_qa(driver)
        scroll_down(driver)
        scroll_up(driver)
        navigate_to_bjc_charis(driver)
        navigate_to_all_products(driver)
        for _ in range(5):
            select_and_interact_with_product(driver)
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
    except Exception as e:
        print("Failed to logout:", e)

if __name__ == "__main__":
    user_credentials = [
        ("user502@test.com", "test123456789"),
        ("user503@test.com", "test123456789"),
        ("user504@test.com", "test123456789"),
        ("user505@test.com", "test123456789"),
        ("user506@test.com", "test123456789"),
        ("user507@test.com", "test123456789"),
        ("user508@test.com", "test123456789"),
        ("user509@test.com", "test123456789"),
        ("user5010@test.com", "test123456789"),
        ("user511@test.com", "test123456789"),
        ("user512@test.com", "test123456789"),
        ("user513@test.com", "test123456789"),
        ("user514@test.com", "test123456789"),
        ("user515@test.com", "test123456789"),
        ("user516@test.com", "test123456789"),
        ("user1000@test.com", "test123456789"),
        ("user1001@test.com", "test123456789"),
        ("user1002@test.com", "test123456789"),
        ("user1003@test.com", "test123456789"),
        ("user1004@test.com", "test123456789"),
        ("user1005@test.com", "test123456789"),
        ("user1006@test.com", "test123456789"),
        ("user1007@test.com", "test123456789"),
        ("user1008@test.com", "test123456789"),
        ("user1009@test.com", "test123456789"),
        ("user1011@test.com", "test123456789"),
        ("user1012@test.com", "test123456789"),
        ("user1013@test.com", "test123456789"),
        ("user1014@test.com", "test123456789"),
        ("user1015@test.com", "test123456789"),
        ("user1016@test.com", "test123456789"),
        ("user1017@test.com", "test123456789"),
        ("user1018@test.com", "test123456789"),
        ("user1023@test.com", "test123456789"),
        ("user1024@test.com", "test123456789"),
        ("user1025@test.com", "test123456789"),
        ("user1026@test.com", "test123456789"),
        ("user1027@test.com", "test123456789"),
        ("user1028@test.com", "test123456789"),
        ("user1029@test.com", "test123456789"),
        ("user1030@test.com", "test123456789"),
        ("user1031@test.com", "test123456789"),
        ("user1032@test.com", "test123456789"),
        ("user1034@test.com", "test123456789"),
        ("user1035@test.com", "test123456789"),
        ("user1036@test.com", "test123456789"),
        ("user1037@test.com", "test123456789"),
        ("user1038@test.com", "test123456789"),
        ("user1039@test.com", "test123456789"),
        ("user1040@test.com", "test123456789"),
        ("user1219@test.com", "test123456789"),
        ("userkizon1@test.com", "test123456789"),
        ("userkizon2@test.com", "test123456789"),
        ("userkizon3@test.com", "test123456789"),
        ("userkizon4@test.com", "test123456789"),
        ("userkizon5@test.com", "test123456789"),
        ("userkizon6@test.com", "test123456789"),
        ("userkizon7@test.com", "test123456789"),
        ("userkizon8@test.com", "test123456789"),
        ("userkizon9@test.com", "test123456789"),
        ("userkizon10@test.com", "test123456789"),
        ("userkizon11@test.com", "test123456789"),
        ("userkizon12@test.com", "test123456789"),
        ("userkizon13@test.com", "test123456789"),
        ("userkizon14@test.com", "test123456789"),
        ("userkizon15@test.com", "test123456789"),
        ("userkizon16@test.com", "test123456789"),
        ("userkizon17@test.com", "test123456789"),
        ("userkizon18@test.com", "test123456789"),
        ("userkizon19@test.com", "test123456789"),
        ("userkizon20@test.com", "test123456789"),
        ("userkizon21@test.com", "test123456789"),
        ("userkizon22@test.com", "test123456789"),
        ("userkizon23@test.com", "test123456789"),
        ("userkizon24@test.com", "test123456789"),
        ("userkizon25@test.com", "test123456789"),
        ("userkizon26@test.com", "test123456789"),
        ("userkizon27@test.com", "test123456789"),
        ("userkizon28@test.com", "test123456789"),
        ("userkizon29@test.com", "test123456789"),
        ("l-shankar@ar-system.co.jp", "test123456789"),
        ("l-shankar1@ar-system.co.jp", "test123456789"),
        ("l-shankar2@ar-system.co.jp", "test123456789"),
    ]
    main(user_credentials)
