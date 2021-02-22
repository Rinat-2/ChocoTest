from selenium import webdriver


def departure_city_value(city_1, driver):
    driver.find_element_by_id("city_1_user").click()
    driver.find_element_by_id("city_1_user").clear()
    driver.find_element_by_id("city_1_user").send_keys(city_1)
    driver.find_element_by_xpath("//div[@id='city_result_1']/ul/li").click()


def arrival_city_value(city_2, driver):
    driver.find_element_by_id("city_2_user").click()
    driver.find_element_by_id("city_2_user").clear()
    driver.find_element_by_id("city_2_user").send_keys(city_2)
    driver.find_element_by_xpath("//div[@id='city_result_2']/ul/li/div/span").click()


class HomePage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://chocotravel-test.apps.chocotravel.com/")

    def set_departure_city_value(self, city_1):
        driver = self.driver
        departure_city_value(city_1, driver)

    def set_arrival_city_value(self, city_2):
        driver = self.driver
        arrival_city_value(city_2, driver)

    def set_date_value(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='calen']/div/div[4]/div[3]/span[25]").click()

    def click_find_tickets_button(self):
        driver = self.driver
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

    def delete_departure_city_value(self, city_1):
        driver = self.driver
        departure_city_value(city_1, driver)
        driver.find_element_by_xpath("//form[@id='search_form']/div/div[5]/div/div").click()

    def delete_arrival_city_value(self, city_2):
        driver = self.driver
        arrival_city_value(city_2, driver)
        driver.find_element_by_xpath("//form[@id='search_form']/div/div[5]/div[2]/div").click()

    def switch_city(self):
        driver = self.driver
        driver.find_element_by_xpath("//form[@id='search_form']/div/div[5]/button/div").click()

    def set_popular_destinations(self):
        driver = self.driver
        driver.find_element_by_id("city_1_user").clear()
        driver.find_element_by_id("city_2_user").clear()
        # driver.find_element_by_link_text("Нур-Султан").click()
        # driver.find_element_by_link_text("Шымкент").click()

    def destroy(self):
        self.driver.quit()
