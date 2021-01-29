def test_find_tickets_with_value(app):
    app.open_home_page()
    app.set_departure_city_value(city_1="Алм")
    app.set_arrival_city_value(city_2="Аст")
    app.set_date_value()
    app.click_find_tickets_button()
    assert app.driver.find_element_by_css_selector("div.logoair_1").get_attribute("title") == ""
    assert app.driver.find_element_by_id("city_1").get_attribute("value") == "ALA"
    assert app.driver.find_element_by_id("city_2").get_attribute("value") == "NQZ"
