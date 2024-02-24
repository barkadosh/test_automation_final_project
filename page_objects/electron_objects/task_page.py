from selenium.webdriver.common.by import By

create_field = (By.CSS_SELECTOR, "input.input_b5pqF")
tasks = (By.CSS_SELECTOR, "div.view_2Ow90")
complete_checkbox = (By.XPATH, "//*[@class='toggleIconsWrapper_2kpi8']")
task_done = (By.XPATH, "//*[@class='label_5i8SP completed_bHv-Q']")
task_not_done = (By.XPATH, "//*[@class='label_5i8SP']")
delete_buttons = (By.XPATH, "//*[@class='destroy_19w1q']")
toggle_all_completed = (By.XPATH, "//*[@class='allCompletedIconWrapper_2rCqr']")
visibility_panel = (By.XPATH, "//*[@class='toggleVisibilityPanel_hNPyc']")
close_visibility_panel = (By.CSS_SELECTOR, "div.toggleVisibilityPanel_hNPyc.isVisible_1VByM")
completed_filter = (By.XPATH, "//button[contains(text(),'Completed')]")
all_filter = (By.XPATH, "//*/div[@class='statusWrapper_fkjww']/button[contains(text(),'All')]")
color_dropdown = (By.XPATH, "//div[@class='topWrapper_2caNE']/*[name()='svg']")
color_green = (By.CSS_SELECTOR,
               "div.wrapper_3Kpfj.vertical_di1oV.tagList_2NRe0>span[style='background: rgb(114, 204, 87);']")
drag_task = (By.XPATH, "//div[@class='taskWrapper_2u8dN']/*[name()='svg']")
class TaskPage:

    def __init__(self, driver):
        self.driver = driver

    def get_create_field(self):
        return self.driver.find_element(create_field[0], create_field[1])

    def get_tasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def get_complete_checkbox(self):
        return self.driver.find_elements(complete_checkbox[0], complete_checkbox[1])

    def get_task_done(self):
        return self.driver.find_elements(task_done[0], task_done[1])

    def get_task_not_done(self):
        return self.driver.find_elements(task_not_done[0], task_not_done[1])

    def get_toggle_all_completed(self):
        return self.driver.find_element(toggle_all_completed[0], toggle_all_completed[1])

    def get_visibility_panel(self):
        return self.driver.find_element(visibility_panel[0], visibility_panel[1])
    def get_close_visibility_panel(self):
        return self.driver.find_element(close_visibility_panel[0], close_visibility_panel[1])

    def get_completed_filter(self):
        return self.driver.find_element(completed_filter[0], completed_filter[1])
    def get_all_filter(self):
        return self.driver.find_element(all_filter[0], all_filter[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_buttons[0], delete_buttons[1])

    def get_color_dropdown(self):
        return self.driver.find_element(color_dropdown[0], color_dropdown[1])

    def get_color_green(self):
        return self.driver.find_element(color_green[0], color_green[1])

    def get_drag_task(self):
        return self.driver.find_elements(drag_task[0], drag_task[1])

