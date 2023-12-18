from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

def main():
    test_emails = ["l-shankar@ar-system.co.jp", "l-shankar1@ar-system.co.jp", "l-shankar3@ar-system.co.jp"]
    threads = []

    for email in test_emails:
        thread = threading.Thread(target=execute_login_and_forgot_password, args=(email,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

        
def execute_login_and_forgot_password(email):
    try:
        login_scenario_wrong_credentials(email, "testtesttest")
        forgot_password_scenario(email)
        login_scenario_correct_credentials(email, "tets123456789")
    except Exception as e:
        print(f"An error occurred for user {email}: {e}")

def login_scenario_wrong_credentials(login_email, login_pass):
    try:
        driver = webdriver.Edge()
        driver.get("https://stg-admin.bjc-online.jp/mypage/login")
        driver.find_element(By.ID, "login_email").send_keys(login_email)
        driver.find_element(By.ID, "login_pass").send_keys(login_pass)
        driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn").click()
        # error_message = driver.find_element(By.CLASS_NAME, "error-message")
        # print(f"Error message for wrong credentials: {error_message.text}")
    except Exception as e:
        print(f"An error occurred during login with wrong credentials for user {login_email}:", e)
    finally:
        driver.quit()

def forgot_password_scenario(login_email):
    try:
        driver = webdriver.Edge()
        driver.get("https://stg-admin.bjc-online.jp/mypage/login")
        driver.find_element(By.CLASS_NAME, "ec-loginRole__passwordreset").click()
        if "forgot" not in driver.current_url:
            raise Exception("Not redirected to the correct URL.")
        driver.find_element(By.ID, "login_email").send_keys(login_email)
        driver.find_element(By.ID, "insert_button").click()
        driver.find_element(By.ID, "ec-loginRole__formSubmit").click()
        print(f"Forgot password scenario executed successfully for user: {login_email}")
    except Exception as e:
        print(f"An error occurred during the forgot password scenario for user {login_email}:", e)
    finally:
        driver.quit()

def login_scenario_correct_credentials(login_email, login_pass):
    try:
        driver = webdriver.Edge()
        driver.get("https://stg-admin.bjc-online.jp/mypage/login")
        driver.find_element(By.ID, "login_email").send_keys(login_email)
        driver.find_element(By.ID, "login_pass").send_keys(login_pass)
        driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn").click()
        print(f"Login successful for user: {login_email}")
    except Exception as e:
        print(f"An error occurred during login for user {login_email}:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
