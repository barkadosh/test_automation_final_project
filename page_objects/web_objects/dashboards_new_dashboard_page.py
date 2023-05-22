from selenium.webdriver.common.by import By

new_panel = (By.CSS_SELECTOR, "button[aria-label='Add new panel']")
# Edit dashboard
add_dashboard_title = (By.ID, "PanelFrameTitle")
add_dashboard_description = (By.ID, "description-text-area")
panel_link = (By.CSS_SELECTOR, ".css-jengqr>.css-g6c6gc-button")
add_link = (By.CSS_SELECTOR, "button.css-9ue6bh-button")
link_title = (By.XPATH, "//*[@placeholder='Show details']")
link_url = (By.CSS_SELECTOR, ".css-1x3vehx-input-input")
save_url = (By.CSS_SELECTOR, ".css-14c36pf-layoutChildrenWrapper>.css-1sara2j-button")
table_mode = (By.XPATH, "//label[text()='Table']")
placement_right = (By.XPATH, "//label[text()='Right']")
time_zone = (By.CSS_SELECTOR, ".css-15fuo2f-input-wrapper.css-1age63q")
browser_time = (By.ID, "react-select-3-option-0-1")
line_width_slider = (By.CLASS_NAME, "rc-slider-handle")
fill_opacity_slider = (By.CLASS_NAME, "rc-slider-handle")
apply_dashboard = (By.CSS_SELECTOR, ".css-ta03ya>.css-1sara2j-button")
save_dashboard = (By.XPATH, "//button[@aria-label='Save dashboard']")
add_dashboard_name = (By.NAME, "title")
save_new_dashboard = (By.XPATH, "//button[@type='submit']")
dashboard_name = (By.XPATH, "//span[@class= 'css-aqkpyi']")
dashboard_title = (By.XPATH, "//h2[@class= 'css-1m35bcr']")


class NewDashboard:
    def __init__(self, driver):
        self.driver = driver

    def get_new_panel(self):
        return self.driver.find_element(new_panel[0], new_panel[1])

    def get_add_dashboard_title(self):
        return self.driver.find_element(add_dashboard_title[0], add_dashboard_title[1])

    def get_add_dashboard_description(self):
        return self.driver.find_element(add_dashboard_description[0], add_dashboard_description[1])

    def get_panel_link(self):
        return self.driver.find_elements(panel_link[0], panel_link[1])[0]

    def get_add_link(self):
        return self.driver.find_elements(add_link[0], add_link[1])[0]

    def get_link_title(self):
        return self.driver.find_element(link_title[0], link_title[1])

    def get_link_url(self):
        return self.driver.find_element(link_url[0], link_url[1])

    def get_save_url(self):
        return self.driver.find_element(save_url[0], save_url[1])

    def get_table_mode(self):
        return self.driver.find_element(table_mode[0], table_mode[1])

    def get_placement_right(self):
        return self.driver.find_elements(placement_right[0], placement_right[1])[0]

    def get_time_zone(self):
        return self.driver.find_elements(time_zone[0], time_zone[1])[3]

    def get_browser_time(self):
        return self.driver.find_element(browser_time[0], browser_time[1])

    def get_line_width_slider(self):
        return self.driver.find_elements(line_width_slider[0], line_width_slider[1])[0]

    def get_fill_opacity_slider(self):
        return self.driver.find_elements(fill_opacity_slider[0], fill_opacity_slider[1])[1]

    def get_apply_dashboard(self):
        return self.driver.find_element(apply_dashboard[0], apply_dashboard[1])

    def get_save_dashboard(self):
        return self.driver.find_element(save_dashboard[0], save_dashboard[1])

    def get_dashboard_name(self):
        return self.driver.find_element(add_dashboard_name[0], add_dashboard_name[1])

    def get_dashboard_title(self):
        return self.driver.find_element(dashboard_title[0], dashboard_title[1])


