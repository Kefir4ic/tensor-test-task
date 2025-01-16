from selenium.webdriver.common.by import By


class BasePage:
    # класс для взаимодействия с webdriver

    def __init__(self, driver):
        self.base_url = 'https://saby.ru/'
        self.driver = driver

    def open_saby_url(self):
        # открываем стартовый URL
        self.driver.get(self.base_url)
        self.wait_browser(2)

    def open_url(self, url):
        # открываем необходимый URL
        self.driver.get(url)
        self.wait_browser(2)

    def wait_browser(self, time):
        # задержка перед выполнением следующего действия
        self.driver.implicitly_wait(time)

    def find_element_by_css_selector(self, css_selector):
        # поиск первого элемента по css-селектору
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_elements_by_css_selector(self, css_selector):
        # поиск списка элементов по css-селектору
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    def get_current_url(self):
        # получение текущего URL
        return self.driver.current_url

    def find_element_by_css_selector_in_element(self, element, css_selector):
        # поиск первого элемента по css-селектору
        return element.find_element(By.CSS_SELECTOR, css_selector)

    def find_elements_by_css_selector_in_element(self, element, css_selector):
        # поиск списка элементов по css-селектору
        return element.find_elements(By.CSS_SELECTOR, css_selector)
