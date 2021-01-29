class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://chocotravel-test.apps.chocotravel.com/"

    def open_home_page(self):
        return self.driver.get(self.base_url)
