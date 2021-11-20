from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("the user is logged into the platform and is in any function of the site (4b)")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/atv1/features/acessbility_a/features/steps/driver/chromedriver")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubensalunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()


@when("they clicks on the 'Toggle high-contrast' function of the site")
def when(context):
    contrast_button = context.driver.find_element_by_id("bt-highContrast")
    contrast_button.click()


@then("the site returns only two colors, black and yellow, to the user")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, "mural")))
    context.driver.quit()

