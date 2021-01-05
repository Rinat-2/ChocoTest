# -*- coding: utf-8 -*-
import allure


@allure.step("Поиск города без значений")
def test_find_tickets_without_value(app):
    with allure.step("Открыть главную страницу"):
        app.open_home_page()
    with allure.step("Нажать на кнопку найти"):
        app.click_find_tickets_button()
    assert app.driver.find_element_by_css_selector("div.win-block").is_displayed()


@allure.step("Удаление города из поля 'Город отправления'")
def test_delete_value_departure_city(app):
    with allure.step("Открыть главную страницу"):
        app.open_home_page()
    with allure.step("Ввести город Алматы и нажать на крестик"):
        app.delete_departure_city_value(city_1="Алм")
    assert app.driver.find_element_by_id("city_1").get_attribute("value") == ""


def test_delete_value_arrival_city(app):
    app.open_home_page()
    app.delete_arrival_city_value(city_2="Аст")
    assert app.driver.find_element_by_id("city_2").get_attribute("value") == ""


def test_switch_city_with_values(app):
    app.open_home_page()
    app.set_departure_city_value(city_1="Алм")
    app.set_arrival_city_value(city_2="Аст")
    app.switch_city()
    assert app.driver.find_element_by_id("city_2").get_attribute("value") == "ALA"
    assert app.driver.find_element_by_id("city_1").get_attribute("value") == "NQZ"


def test_find_tickets_with_value(app):
    app.open_home_page()
    app.set_departure_city_value(city_1="Алм")
    app.set_arrival_city_value(city_2="Аст")
    app.set_date_value()
    app.click_find_tickets_button()
    assert app.driver.find_element_by_id("city_1").get_attribute("value") == "ALA"
    assert app.driver.find_element_by_id("city_2").get_attribute("value") == "NQZ"


def test_find_tickets_with_popular_destinations(app):
    app.open_home_page()
    app.set_popular_destinations()
    # assert app.driver.find_element_by_link_text("Нур-Султан").is_displayed(False)
