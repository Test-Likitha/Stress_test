from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import threading

def main():
    login_info = [(f"user{i}@test.com", f"password{i}!!!!") for i in range(1, 2)]
    threads = []
    for username, password in login_info:
        thread = threading.Thread(target=scenario_one, args=(username, password))
        threads.append(thread)
        thread.start()

    # Wait thread exit.
    for thread in threads:
        thread.join()

def scenario_one(email, password):
    try:
        driver = webdriver.Edge()
        driver.get("https://dev-admin.bjc-online.jp/entry")
        driver.find_element(By.CLASS_NAME, "ec-inlineBtn--action").click()
        driver.find_element(By.ID,"entry_email").send_keys(email)
        # driver.find_element(By.XPATH, "//div[@onclick='enterSameAddress()']").click()
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
        # driver.find_element(By.XPATH, "//div[@onclick='enterSameEmail()']").click()
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
        try:
            driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()
        except:
            driver.find_element(By.CLASS_NAME, 'ec-inputFormActionsBtn').click()

        # ブラウザを閉じる
        driver.close()

    except Exception as e:
        print("シナリオ①でエラーが発生しました:", e)

if __name__ == "__main__":
    main()