from BasePage import BasePage


class SecondTaskConst:
    # класс с константами для второго задания
    CONTACTS_ELEMENT = '.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover'
    CONTACTS_MENU = '.sbisru-Header-ContactsMenu__items.sbisru-Header-ContactsMenu__items-visible'
    REGION_ELEMENT = '.sbis_ru-Region-Chooser__text.sbis_ru-link'
    PHONE_ELEMENT = '.sbisru-Header-ContactsMenu__text-gray'
    REGIONS_PANEL = '.sbis_ru-Region-Panel__item'
    REGION_LINK = '.sbis_ru-link'

    SABY_URL = "https://saby.ru/"


class SecondTask(BasePage):
    # Класс с действиями для второго задания

    def open_saby_url(self):
        # открытие стартовой страницы
        self.open_url(SecondTaskConst.SABY_URL)

    def contacts_button_action(self):
        # выполнение первого этапа сценария для второго задания (поиск и нажатия на блок с контактами)
        contacts_element = self.find_element_by_css_selector(SecondTaskConst.CONTACTS_ELEMENT)
        contacts_element.click()
        self.wait_browser(2)

        contacts_menu = self.find_element_by_css_selector(SecondTaskConst.CONTACTS_MENU)
        return contacts_menu

    def get_region_button(self, region_element):
        # получение кнопки региона
        return self.find_element_by_css_selector_in_element(region_element, SecondTaskConst.REGION_ELEMENT)

    def get_current_region(self, region_element):
        # получение текущего региона
        return self.find_element_by_css_selector_in_element(region_element, SecondTaskConst.REGION_ELEMENT).text

    def get_current_phone(self, region_element):
        # получение текущего номера телефона
        return self.find_element_by_css_selector_in_element(region_element, SecondTaskConst.PHONE_ELEMENT).text

    def get_regions(self):
        # получения списка ссылок с регионами
        return self.find_elements_by_css_selector(SecondTaskConst.REGIONS_PANEL)

    def find_region(self, regions, region_text):
        # поиск нужного региона
        for region in regions:
            span_link = self.find_element_by_css_selector_in_element(region, SecondTaskConst.REGION_LINK)
            if span_link.get_attribute('title') == region_text:
                return span_link
