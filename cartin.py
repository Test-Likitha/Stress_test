from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

def main():
    num_products_to_add = 10  # products_count
    driver = webdriver.Edge()  
    login(driver)
    add_products_to_cart(driver, num_products_to_add)
    click_on_image(driver)

def login(driver):
    try:
        driver.get("https://stg-admin.bjc-online.jp/mypage/login")
        login_email = driver.find_element(By.ID, "login_email")
        login_pass = driver.find_element(By.ID, "login_pass")
        login_button = driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn")

        login_email.send_keys("l-shankar@ar-system.co.jp")  
        login_pass.send_keys("test123456789") 
        login_button.click()

        time.sleep(2)  
    except Exception as e:
        print("Login failed:", e)

def click_on_image(driver):
    try:
        image = driver.find_element(By.XPATH, "//img[@alt='BJC CHARIS&Co. ONLINESTORE']")
        image.click()
    except Exception as e:
        print("Failed to click on the image:", e)

def add_products_to_cart(driver, num_products):
    try:
        driver.get("https://stg-admin.bjc-online.jp/products/list")
        
        confirm_buttons_popup = None
        try:
            confirm_buttons_popup = driver.find_element(By.ID, "confirmButtons")
        except:
            pass

        if confirm_buttons_popup:
            buttons = confirm_buttons_popup.find_elements(By.CLASS_NAME, "button.undefined")

            if len(buttons) >= 2:
                buttons[1].click()

        for _ in range(num_products):
            add_to_cart(driver)
            handle_error_message(driver)

        # Redirect to cart
        driver.get("https://stg-admin.bjc-online.jp/cart")
        scroll_up_and_down(driver)

        for _ in range(2):
            click_cart_row_buttons(driver)
            change_delivery_date(driver)
            click_action_buttons(driver)

        # Redirect to mypage
        driver.get("https://stg-admin.bjc-online.jp/mypage/")
        click_history_list_header(driver)
        handle_gateway_timeout(driver)
        scroll_down_to_ec_inline_btn(driver)
        click_ec_inline_btn(driver)

        # Go to BJC CHARIS&Co. ONLINESTORE
        driver.get("https://stg-admin.bjc-online.jp/logout")
        print("Scenario completed successfully.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

def add_to_cart(driver):
    add_cart_button = driver.find_element(By.CLASS_NAME, "ec-blockBtn--action.add-cart")
    add_cart_button.click()

def handle_error_message(driver):
    try:
        # Wait for the error message
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='カートへの追加に失敗しました。']"))
        )
        print("Error message displayed:", error_message.text)
        
        # Handle the error message as needed
        ok_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ec-inlineBtn--ok"))
        )
        ok_button.click()
    except TimeoutException:
        print("Timed out waiting for the error message.")
    except Exception as e:
        print("An error occurred while handling the error message:", e)

    try:
        # Check for the dialog
        dialog = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ec-inlineBtn--cancel"))
        )
        if "カートに追加しました。" in dialog.text:
            dialog.click()
    except TimeoutException:
        print("Timed out waiting for the dialog.")
    except Exception as e:
        print("An error occurred while handling the dialog:", e)

def scroll_up_and_down(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_UP)
    time.sleep(1)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

def click_cart_row_buttons(driver):
    for _ in range(2):
        amount_up_button = driver.find_element(By.CLASS_NAME, "ec-cartRow__amountUpButton")
        amount_up_button.click()
        time.sleep(1)

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

def click_action_buttons(driver):
    action_buttons = driver.find_elements(By.CLASS_NAME, "ec-blockBtn--action")
    for button in action_buttons:
        button.click()
        time.sleep(1)

def click_history_list_header(driver):
    history_button = driver.find_element(By.CLASS_NAME, "ec-historyListHeader__action")
    history_button.click()

def handle_gateway_timeout(driver):
    try:
        gateway_timeout_heading = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='504 Gateway Time-out']"))
        )
        print("Gateway Timeout. Refreshing the page.")
        driver.refresh()
    except:
        pass

def scroll_down_to_ec_inline_btn(driver):
    try:
        inline_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ec-inlineBtn.ec-font-bold"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", inline_btn)
    except:
        pass

def click_ec_inline_btn(driver):
    try:
        inline_btn = driver.find_element(By.CLASS_NAME, "ec-inlineBtn.ec-font-bold")
        inline_btn.click()
    except:
        pass

if __name__ == "__main__":
    main()
