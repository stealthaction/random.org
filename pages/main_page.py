from playwright.sync_api import Page


class MainPageSelectors:
    INPUT_MIN_NUMBER = "//input[contains(@id, 'min')]"
    INPUT_MAX_NUMBER = "//input[contains(@id, 'max')]"
    GENERATING_NUM = "//span[contains(@id, 'result')]//span[contains(@style, 'font-weight:bold')]"


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = MainPageSelectors

    def open_page(self, url: str) -> None:
        self.page.goto(url)

    def fill_min_number(self, num: str) -> None:
        self.page.locator(self.selectors.INPUT_MIN_NUMBER).fill(num)

    def fill_max_number(self, num: str) -> None:
        self.page.locator(self.selectors.INPUT_MAX_NUMBER).fill(num)

    def generate_number(self, min_number: str, max_number: str) -> None:
        self.fill_min_number(min_number)
        self.fill_max_number(max_number)

    def assert_result(self, min: str, max: str) -> None:
        result = self.page.locator(self.selectors.GENERATING_NUM).first.text_content()
        min_number = int(min)
        max_number = int(max)
        assert min_number <= int(result) <= max_number, f"Сгенерированное значение {result} не находится в диапазоне {min_number}-{max_number}"