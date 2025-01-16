import time
from FirstTask import FirstTask
from SecondTask import SecondTask
from ThirdTask import ThirdTask

FirstTaskConst = {
    'tensor_url': 'https://tensor.ru/',
    'tensor_about_url': 'https://tensor.ru/about',
}

SecondTaskConst = {
    'current_region': 'г. Москва',
    'current_phone': '+7 495 532-02-27',
    'needed_region': 'Камчатский край',
    'needed_phone': '+7 4152 34-01-08'
}

ThirdTaskConst = {
    'filename': 'plugin.exe',
    'link_text': 'Скачать (Exe 10.42 МБ)',
    'file_size': 10.42
}


def test_first_task(browser):
    first_task = FirstTask(browser)

    first_task.open_saby_url()

    contacts_button = first_task.get_contacts_button()
    contacts_button.click()
    first_task.wait_browser(2)

    contacts_menu = first_task.get_contacts_menu()
    assert contacts_menu.is_displayed()

    first_task.open_tensor_url()
    assert first_task.get_current_url() == FirstTaskConst['tensor_url']

    power_in_people_text = first_task.get_power_in_people_text_element()
    assert power_in_people_text.is_displayed()

    power_in_people_more_button = first_task.get_power_in_people_more_button()
    power_in_people_more_button.click()
    first_task.wait_browser(2)
    assert first_task.get_current_url() == FirstTaskConst['tensor_about_url']

    is_width, is_height = first_task.is_equals_cards_size()
    assert is_width, is_height


def test_second_task(browser):
    second_task = SecondTask(browser)

    second_task.open_saby_url()

    contacts_button = second_task.get_contacts_button()
    contacts_button.click()
    second_task.wait_browser(2)

    contacts_menu = second_task.get_contacts_menu()

    current_region = second_task.get_current_region(contacts_menu)
    current_phone = second_task.get_current_phone(contacts_menu)

    assert current_region == SecondTaskConst['current_region']
    assert current_phone == SecondTaskConst['current_phone']

    region_button = second_task.get_region_button(contacts_menu)

    region_button.click()
    second_task.wait_browser(2)

    needed_region_button = second_task.find_region(SecondTaskConst['needed_region'])

    needed_region_button.click()
    time.sleep(1)

    new_region = second_task.get_current_region(contacts_menu)
    new_phone = second_task.get_current_phone(contacts_menu)

    assert new_region != current_region
    assert new_region == SecondTaskConst['needed_region']
    assert new_phone == SecondTaskConst['needed_phone']


def test_third_task(browser):
    third_task = ThirdTask(browser)

    third_task.open_saby_url()

    download_page_link = third_task.get_download_page_link()
    download_page_link.click()

    third_task.wait_browser(2)

    download_href = third_task.get_needed_download_button_href(ThirdTaskConst['link_text'])

    third_task.download_file(download_href, ThirdTaskConst['filename'])

    is_file_exist = third_task.is_file_exist(ThirdTaskConst['filename'])

    assert is_file_exist

    file_size = third_task.get_download_file_size(ThirdTaskConst['filename'])

    assert file_size == ThirdTaskConst['file_size']

    third_task.delete_file(ThirdTaskConst['filename'])
