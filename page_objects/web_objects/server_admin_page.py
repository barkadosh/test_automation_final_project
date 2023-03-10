from selenium.webdriver.common.by import By

search = (By.CSS_SELECTOR, ".css-1mlczho-input-input")
new_user = (By.CSS_SELECTOR, "a[href='admin/users/create']")
# I changed this element to click on <a> link and not on <tr> ->
users_list = (By.CSS_SELECTOR, "table>tbody>tr>td:first-child>a")
user_by_user_name = (By.CSS_SELECTOR, "a[title='some-user']")
user_info = (By.CSS_SELECTOR, ".page-heading")
delete = (By.CSS_SELECTOR, "div>button.css-mk7eo3-button")
confirm_delete = (By.CSS_SELECTOR, "button[aria-label='Confirm Modal Danger Button']")
close_alert = (By.CSS_SELECTOR, "button[aria-label='Close alert']")


class ServerAdminPage:
    def __init__(self, driver):
        self.driver = driver

    def get_search(self):
        return self.driver.find_element(search[0], search[1])

    def get_new_user(self):
        return self.driver.find_element(new_user[0], new_user[1])

    def get_users_list(self):
        return self.driver.find_elements(users_list[0], users_list[1])

    def get_user_by_index(self, index):
        return self.get_users_list()[index]

    def get_user_by_username(self, user):
        return self.driver.find_element(user_by_user_name[0], user_by_user_name[1].replace('some-user', str(user)))

    def get_user_info(self):
        return self.driver.find_element(user_info[0], user_info[1])

    def get_delete(self):
        return self.driver.find_element(delete[0], delete[1])

    def confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])

    def close_alert(self):
        return self.driver.find_element(close_alert[0], close_alert[1])
