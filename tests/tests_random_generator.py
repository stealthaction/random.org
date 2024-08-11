import time

import allure
import pytest
from playwright.sync_api import BrowserContext


@allure.suite("Сценарные тесты")
@allure.sub_suite("Главная страница")
class TestsMainPage:
    @allure.feature("[UI] Главная страница")
    @allure.description("Автотест проверяет вывод результата при вводе диапазона числа")
    @pytest.mark.parametrize(
        "min_number, max_number", [("1", "100"), ("1", "1"), ("23", "13")]
    )
    def test_generate_number_in_range(
        self, main_page, min_number, max_number, context: BrowserContext
    ):
        with allure.step("Открытие страницы"):
            main_page.open_page("https://www.random.org/")
        with allure.step(f"Ввод чисел от {min_number} до {max_number}"):
            main_page.generate_number(min_number, max_number)
        with allure.step("Проверка результата"):
            main_page.assert_result(min_number, max_number)
