# Enums

# Enum for selecting displayed element, exist element, etc.. my wait methode (in this file) use this enum
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'


# Enum for selecting from users list in users page by username or by index, "open_user_settings" web flow use this Enum
class By:
    USER = 'user'
    INDEX = 'index'


# Enum for tc- "test_verify_mortgage_repayment" in test_mobile, yes - for saving mortgage repayment, no - for not
class Save:
    YES = True
    NO = False


# Enum for tc- "test_verify_mortgage_repayment" in test_mobile, yes - for saving mortgage repayment, no - for not
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
