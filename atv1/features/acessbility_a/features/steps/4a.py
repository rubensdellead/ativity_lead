from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is logged into the site, and is on any screen of the site and the increase font function is "
       "available (4a)")
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


@when("they click on 'Increase Font")
def when(context):
    class_button = context.driver.find_element_by_xpath("courses")
    class_button.click()


@then("the font of the whole site is changed according to the clicks on the button the user is on")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, "mural")))
    context.driver.quit()
