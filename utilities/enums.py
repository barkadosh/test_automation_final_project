# Enums

# Enum for selecting displayed element, exist element, element text, in my wait methods
# (common_ops.py file) use this enum.
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_TEXT_PRESENT = 'text_present_in_element'


# Enum for selecting from users list in users page by username or by index, "open_user_settings" web flow use this Enum.
class By:
    USER = 'user'
    INDEX = 'index'


# Enum for tc- "test_verify_mortgage_repayment" in test_mobile, yes - for saving mortgage repayment, no - for not.
class Save:
    YES = True
    NO = False


# Enum for selecting direction in my methode- "swipe_screen", from mobile_flows.
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
