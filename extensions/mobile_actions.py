import allure

from extensions.ui_actions import UiActions
from test_cases import conftest as conf


class MobileActions(UiActions):
    @staticmethod
    @allure.step('Tap on element')
    def tap(elem, times=1):
        conf.action.tap(elem, times).perform()

    @staticmethod
    @allure.step('Swipe screen')
    def swipe(start_x, start_y, end_x, end_y, duration):
        conf.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    @allure.step('Zoom on element')
    def zoom(elem, pixel=200):
        action1 = conf.action
        action2 = conf.action2
        m_action = conf.m_action
        x_loc = elem.rect['x']
        y_loc = elem.rect['y']
        action1.long_press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc + pixel).waite(500).release()
        action2.long_press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc - pixel).waite(500).release()
        m_action.add(action1, action2)
        m_action.perform()

    @staticmethod
    @allure.step('Pinch on element')
    def pinch(elem, pixel=200):
        action1 = conf.action
        action2 = conf.action2
        m_action = conf.m_action
        x_loc = elem.rect['x']
        y_loc = elem.rect['y']
        action1.long_press(x=x_loc, y=y_loc + pixel).move_to(x=x_loc, y=y_loc).waite(500).release()
        action2.long_press(x=x_loc, y=y_loc - pixel).move_to(x=x_loc, y=y_loc).waite(500).release()
        m_action.add(action1, action2)
        m_action.perform()
