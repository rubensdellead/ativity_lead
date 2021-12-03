from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is on the login page")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/2-prova/features/login/features/steps/driver/chromedriver")
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()


@when("they fill in the username and password fields")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubens.moreira@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()


@then("the system site redirects the user to the home page.")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'create')))
    context.driver.quit()
