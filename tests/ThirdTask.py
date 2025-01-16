import os
import requests
from BasePage import BasePage


class ThirdTaskConst:
    # класс с константами для третьего задания
    FOOTER = '.sbisru-Footer.sbisru-Footer__scheme--default'
    HELPFUL_BLOCK = '.sbisru-Footer__cell.pb-16.pb-sm-8'
    HELPFUL_LINKS_BLOCK = '.sbisru-Footer__list.sbisru-Footer__items--padding-left.sbisru-Footer__list--hidden'
    HELPFUL_LINKS_LIST = '.sbisru-Footer__list-item.pb-16'
    HELPFUL_LINK = '.sbisru-Footer__link'
    DOWNLOAD_LINKS = '.sbis_ru-DownloadNew-loadLink__link.js-link'


class ThirdTask(BasePage):
    # Класс с действиями для третьего задания

    def _get_footer(self):
        # ищем футер
        return self.find_element_by_css_selector(ThirdTaskConst.FOOTER)

    def _get_footer_helpful_blocks(self):
        # ищем блоки с полезными ссылками в футере
        footer = self._get_footer()
        return self.find_elements_by_css_selector_in_element(footer, ThirdTaskConst.HELPFUL_BLOCK)

    def get_download_page_link(self):
        # перебираем полезные ссылки из блоков в поисках нужного
        helpful_blocks = self._get_footer_helpful_blocks()
        for block in helpful_blocks:
            helpful_links_list = self.find_elements_by_css_selector_in_element(block, ThirdTaskConst.HELPFUL_LINKS_LIST)
            for link in helpful_links_list:
                if link.text == 'Скачать локальные версии':
                    return self.find_element_by_css_selector_in_element(link, ThirdTaskConst.HELPFUL_LINK)

    def _get_downloads_buttons(self):
        # ищем все кнопки скачивания файлов
        return self.find_elements_by_css_selector(ThirdTaskConst.DOWNLOAD_LINKS)

    def get_needed_download_button_href(self, link_text):
        # ищем кнопку с нужным текстом и получаем значение href из нее
        download_links = self._get_downloads_buttons()
        for link in download_links:
            if link.text == link_text:
                return link.get_attribute('href')

    def download_file(self, file_href, filename):
        # скачиваем файл в текущую директорию
        response = requests.get(file_href)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)

    def is_file_exist(self, filename):
        # проверяем, что файл скачался
        download_dir = os.getcwd()
        filepath = os.path.join(download_dir, filename)
        return os.path.isfile(filepath)

    def get_download_file_size(self, filename):
        # получаем размер файла
        download_dir = os.getcwd()
        filepath = os.path.join(download_dir, filename)
        file_byte_size = os.path.getsize(filepath)
        file_mb_size = file_byte_size / 1048576
        return round(file_mb_size, 2)

    def delete_file(self, filename):
        # удаляем файл
        download_dir = os.getcwd()
        filepath = os.path.join(download_dir, filename)
        os.remove(filepath)
