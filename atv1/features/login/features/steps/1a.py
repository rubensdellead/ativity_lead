from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("the user is in the login page")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/atv1/features/login/features/steps/driver/chromedriver")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()


@when("hey fills the username and password fields")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubensalunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()


@then("the system site redirects the user to the home page, but specifically, to the 'Start Menu'")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/nav/ul/div/li[1]/a[1]')))
    context.driver.quit()
