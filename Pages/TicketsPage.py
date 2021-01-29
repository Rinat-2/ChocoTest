from selenium import webdriver

from Pages.HomePage import HomePage


class TicketsPage(HomePage):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://chocotravel-test.apps.chocotravel.com/")

    def destroy(self):
        self.driver.quit()
