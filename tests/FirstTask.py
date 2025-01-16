from BasePage import BasePage


class FirstTaskConst:
    # класс с константами для первого задания
    CONTACTS_ELEMENT = '.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover'
    CONTACTS_MENU = '.sbisru-Header-ContactsMenu__items.sbisru-Header-ContactsMenu__items-visible'
    POWER_IN_PEOPLE_BLOCK = '.tensor_ru-Index__block4-content.tensor_ru-Index__card'
    POWER_IN_PEOPLE_TEXT = '.tensor_ru-Index__card-title.tensor_ru-pb-16'
    POWER_IN_PEOPLE_BUTTON = '.tensor_ru-link.tensor_ru-Index__link'
    WORK_CARD_IMAGES = '.tensor_ru-About__block3-image-filter'

    TENSOR_URL = "https://tensor.ru/"


class FirstTask(BasePage):
    # Класс с действиями для первого задания

    def get_contacts_button(self):
        # поиск кнопки с контактами
        return self.find_element_by_css_selector(FirstTaskConst.CONTACTS_ELEMENT)

    def get_contacts_menu(self):
        # поиск меню с информацией о контактах
        return self.find_element_by_css_selector(FirstTaskConst.CONTACTS_MENU)

    def open_tensor_url(self):
        # переход на URL tensor.ru
        self.open_url(FirstTaskConst.TENSOR_URL)

    def _get_power_in_people_block(self):
        return self.find_element_by_css_selector(FirstTaskConst.POWER_IN_PEOPLE_BLOCK)

    def get_power_in_people_text_element(self):
        # поиск элемента с текстом "СИЛА В ЛЮДЯХ"
        power_in_people_block = self._get_power_in_people_block()
        return self.find_element_by_css_selector_in_element(power_in_people_block, FirstTaskConst.POWER_IN_PEOPLE_TEXT)

    def get_power_in_people_more_button(self):
        # поиск кнопки "ПОДРОБНЕЕ" в блоке "СИЛА В ЛЮДЯХ"
        power_in_people_block = self._get_power_in_people_block()
        return self.find_element_by_css_selector_in_element(power_in_people_block,
                                                            FirstTaskConst.POWER_IN_PEOPLE_BUTTON)

    def _get_work_card_images(self):
        # получение карточек с фото "РАБОТАЕМ"
        return self.find_elements_by_css_selector(FirstTaskConst.WORK_CARD_IMAGES)

    def is_equals_cards_size(self):
        # сравнение размеров карточек
        work_card_images = self._get_work_card_images()

        card_width = []
        card_height = []

        for work_card_image in work_card_images:
            card_height.append(work_card_image.rect["height"])
            card_width.append(work_card_image.rect["width"])

        return all(width == card_width[0] for width in card_width), \
            all(height == card_height[0] for height in card_height)
