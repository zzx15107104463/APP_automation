from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):
        self.driver = driver

    def base_find_element(self, loc, time=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
