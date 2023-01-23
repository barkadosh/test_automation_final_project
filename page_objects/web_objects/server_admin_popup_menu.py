from selenium.webdriver.common.by import By

users_nav = (By.CSS_SELECTOR, "a[href='/admin/users']")
orgs_nav = (By.CSS_SELECTOR, "a[href='/admin/orgs']")
settings_nav = (By.CSS_SELECTOR, "a[href='/admin/settings']")
stat_nav = (By.CSS_SELECTOR, "a[href='/admin/licensing']")


class ServerAdminPopUp:
    def __init__(self, driver):
        self.driver = driver

    def get_users_nav(self):
        return self.driver.find_element(users_nav[0], users_nav[1])

    def get_orgs_nav(self):
        return self.driver.find_element(orgs_nav[0], orgs_nav[1])

    def get_settings_nav(self):
        return self.driver.find_element(settings_nav[0], settings_nav[1])

    def get_stat_nav(self):
        return self.driver.find_element(stat_nav[0], stat_nav[1])

