from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

def login_scenario(login_email, login_pass):
    try:
        driver = webdriver.Edge()
        # driver.get("https://stg-admin.bjc-online.jp/mypage/login")
        driver.get("https://stg.bjc-online.jp/mypage/login")

        while True:
            driver.find_element(By.ID, "login_email").send_keys(login_email)
            driver.find_element(By.ID, "login_pass").send_keys(login_pass)

            driver.find_element(By.CLASS_NAME, "ec-loginRole__formSubmitBtn").click()

            # error_message = driver.find_element(By.CLASS_NAME, "error-message")
            
            # if "ログインIDまたはパスワードが違います" in error_message.text:
            #     driver.find_element(By.ID, "login_email").clear()
            #     driver.find_element(By.ID, "login_pass").clear()
            # else:
            #     print(f"Login successful for user: {login_email}")
            #     break

    except Exception as e:
        print(f"An error occurred during login for user {login_email}:", e)

    finally:
        driver.quit()

def execute_login_scenario(test_case):
    user_id, password = test_case
    login_scenario(user_id, password)

def main():
    test_cases = [
        ("l-shankar@ar-system.co.jp", "test123456789"),
        # ("user2@example.com", "password2"),
        # add more cases here
    ]

    threads = []

    for test_case in test_cases:
        thread = threading.Thread(target=execute_login_scenario, args=(test_case,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
