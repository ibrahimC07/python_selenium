
from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLoginError:

    url = 'http://demostore.supersqa.com/my-account/'
    invalid_email = 'abc@supersqa.com'
    expected_msg = 'Error: The password you entered for the email address abc@supersqa.com is incorrect. Lost your ' \
                   'password?'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefge')

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_message(self):
        err_elm = self.driver.find_element(By.XPATH, "//div[@id='content']//li[1]")
        displayed_err = err_elm.text
        assert displayed_err == self.expected_msg, "The displayed error is not expected."
        print("PASS")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.driver.quit()

if __name__ == '__main__':

    obj = InvalidUserLoginError()
    obj.main()