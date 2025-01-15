import os
import requests
from FirstTask import FirstTask
from SecondTask import SecondTask

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_dir = os.getcwd()


# проверка файла после скачивания
def check_file(dirname, filename):
    filepath = os.path.join(dirname, filename)
    file_byte_size = os.path.getsize(filepath)
    file_mb_size = file_byte_size / 1048576
    print(round(file_mb_size, 2))


# скачивание файла по ссылке
def download_file(download_url):
    response = requests.get(download_url)
    response.raise_for_status()

    with open('plagin.exe', 'wb') as file:
        file.write(response.content)


def test_first_task(browser):
    first_task = FirstTask(browser)

    first_task.open_saby_url()
    contacts_menu = first_task.contacts_button_action()
    assert contacts_menu.is_displayed()

    first_task.open_tensor_url()
    assert first_task.get_current_url() == "https://tensor.ru/"

    power_in_people_text = first_task.power_in_people_text()
    assert power_in_people_text.is_displayed()

    first_task.power_in_people_action()
    assert first_task.get_current_url() == "https://tensor.ru/about"

    is_width, is_height = first_task.check_cards_size()
    assert is_width, is_height


def test_second_task(browser):
    second_task = SecondTask(browser)

    second_task.open_saby_url()
    contacts_menu = second_task.contacts_button_action()

    current_region = second_task.get_current_region(contacts_menu)
    current_phone = second_task.get_current_phone(contacts_menu)

    assert current_region == 'г. Москва'
    assert current_phone == '+7 495 532-02-27'

    region_button = second_task.get_region_button(contacts_menu)

    region_button.click()
    second_task.wait_browser(2)

    regions_panel = second_task.get_regions()
    needed_region_button = second_task.find_region(regions_panel, 'Камчатский край')

    needed_region_button.click()
    time.sleep(1)

    new_region = second_task.get_current_region(contacts_menu)
    new_phone = second_task.get_current_phone(contacts_menu)

    assert new_phone != current_phone
    assert new_region != current_region

# ТРЕТИЙ СЦЕНАРИЙ ПЕРЕРАБОТАТЬ
# print("-------------")
# print("НАЧАЛО ТРЕТЬЕГО СЦЕНАРИЯ (ПЕРЕРАБОТАТЬ)")
# print("-------------")
#
# options = Options()
# options.add_experimental_option("prefs", {
#   "download.default_directory": fr"{download_dir}",
#   "download.prompt_for_download": True,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })
# driver = webdriver.Chrome(options)
# open_url(driver, "https://saby.ru/")
# driver.implicitly_wait(2)
#
# footer = find_element_by_css_selector(driver, '.sbisru-Footer.sbisru-Footer__scheme--default')
#
# footer_helpful_block = find_elements_by_css_selector(footer, '.sbisru-Footer__cell.pb-16.pb-sm-8')[2]
# helpful_links_list = find_elements_by_css_selector(footer_helpful_block, '.sbisru-Footer__list.sbisru-Footer__items--padding-left.sbisru-Footer__list--hidden')
# for helpful_links_elements in helpful_links_list:
#     helpful_links = find_elements_by_css_selector(helpful_links_elements, '.sbisru-Footer__list-item.pb-16')
#     for helpful_link in helpful_links:
#         if helpful_link.text == 'Скачать локальные версии':
#             download_link = find_element_by_css_selector(helpful_link, '.sbisru-Footer__link')
#             # print(download_link.text, download_link.get_attribute('href'))
#             click_element(download_link)
#             driver.implicitly_wait(5)
#
#             download_links = find_elements_by_css_selector(driver, '.sbis_ru-DownloadNew-loadLink__link.js-link')
#             for download_link in download_links:
#                 # print(download_link.text)
#                 if download_link.text == 'Скачать (Exe 10.42 МБ)':
#                     download_file(download_link.get_attribute('href'))
#                     check_file(download_dir, 'plagin.exe')
#
#
# driver.implicitly_wait(10)
# time.sleep(5)
#
# driver.quit()
