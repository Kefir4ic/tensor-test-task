from BasePage import BasePage
from selenium.webdriver.common.by import By


class FirstTaskConst:
    # класс с константами для первого задания
    CONTACTS_ELEMENT = '.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover'
    CONTACTS_MENU = '.sbisru-Header-ContactsMenu__items.sbisru-Header-ContactsMenu__items-visible'
    POWER_IN_PEOPLE_BLOCK = '.tensor_ru-Index__block4-content.tensor_ru-Index__card'
    POWER_IN_PEOPLE_TEXT = '.tensor_ru-Index__card-title.tensor_ru-pb-16'
    POWER_IN_PEOPLE_BUTTON = '.tensor_ru-link.tensor_ru-Index__link'
    WORK_CARD_IMAGES = '.tensor_ru-About__block3-image-filter'

    SABY_URL = "https://saby.ru/"
    TENSOR_URL = "https://tensor.ru/"


class FirstTask(BasePage):
    # Класс с действиями для первого задания

    def open_saby_url(self):
        self.open_url(FirstTaskConst.SABY_URL)

    def contacts_button_action(self):
        # выполнение первого этапа сценария для первого задания (поиск и нажатия на блок с контактами)
        contacts_element = self.find_element_by_css_selector(FirstTaskConst.CONTACTS_ELEMENT)
        contacts_element.click()
        self.wait_browser(2)

        contacts_menu = self.find_element_by_css_selector(FirstTaskConst.CONTACTS_MENU)
        return contacts_menu
        # return contacts_menu.is_displayed()

    def open_tensor_url(self):
        # выполнение второго этапа сценария для первого задания (переход на URL tensor.ru и проверка перехода)
        self.open_url(FirstTaskConst.TENSOR_URL)
        # return self.get_current_url()

    def power_in_people_text(self):
        # выполнение третьего этапа сценария для первого задания (поиск текста "СИЛА В ЛЮДЯХ")
        power_in_people_block = self.find_element_by_css_selector(FirstTaskConst.POWER_IN_PEOPLE_BLOCK)

        # МНЕ НЕ НРАВИТСЯ ЭТОТ ЭЛЕМЕНТ С ТОЧКИ ЗРЕНИЯ АРХИТЕКТУРЫ
        power_in_people_text = power_in_people_block.find_element(By.CSS_SELECTOR, FirstTaskConst.POWER_IN_PEOPLE_TEXT)
        return power_in_people_text
        # return power_in_people_text.is_displayed()

    def power_in_people_action(self):
        # выполнение четвертого этапа сценария для первого задания (нажатие на кнопку)
        power_in_people_block = self.find_element_by_css_selector(FirstTaskConst.POWER_IN_PEOPLE_BLOCK)

        # МНЕ НЕ НРАВИТСЯ ЭТОТ ЭЛЕМЕНТ С ТОЧКИ ЗРЕНИЯ АРХИТЕКТУРЫ
        power_in_people_more_button = power_in_people_block.find_element(By.CSS_SELECTOR, FirstTaskConst.POWER_IN_PEOPLE_BUTTON)
        power_in_people_more_button.click()
        self.wait_browser(5)

        # return self.get_current_url()

    def check_cards_size(self):
        # выполнение пятого этапа сценария для первого задания (сравнение размеров карточек)
        work_card_images = self.find_elements_by_css_selector(FirstTaskConst.WORK_CARD_IMAGES)

        card_width = []
        card_height = []

        for work_card_image in work_card_images:
            card_height.append(work_card_image.rect["height"])
            card_width.append(work_card_image.rect["width"])

        return all(width == card_width[0] for width in card_width),\
            all(height == card_height[0] for height in card_height)
