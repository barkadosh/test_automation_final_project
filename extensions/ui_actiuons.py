import test_cases.conftest as conf


class UiActions:
    @staticmethod
    def click(elem):
        #explistly wait...
        elem.click()

    @staticmethod
    def update_text(elem, value):
        elem.send_keys(value)

    @staticmethod
    def mouse_hover(elem1, elem2):
        conf.action.move_to_element(elem1).move_to_element(elem2).perform()

    @staticmethod
    def right_click(elem):
        conf.action.context_click(elem).perform()

    @staticmethod
    def drag_and_drop(elem1, elem2):
        conf.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    def clear(elem):
        elem.clear()

