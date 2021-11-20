from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is logged into the site and is on the 'My Courses' screen")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/atv1/features/curses /features/steps/driver/chromedriver")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubensalunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    curses_button = context.driver.find_element_by_id("nav-item-1")
    curses_button.click()


@when("the user clicks on 'Enter the Class'")
def when(context):
    class_button = context.driver.find_element_by_xpath("courses")
    class_button.click()


@then("all the content corresponding to that lesson is presented, including videos and exercises")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, "mural")))
    context.driver.quit()
