from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is logged into the site, and is on the 'Glossary' screen;")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/atv1/features/glossary/features/steps/driver/chromedriver")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubensalunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    glossary_button = context.driver.find_element_by_id("nav-item-6")
    glossary_button.click()


@when("they type in an existing term")
def when(context):
    mail_write = context.driver.find_element_by_id("search")
    mail_write.send_keys("Teste")

    search_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-glossary"
                                                         "/div/app-small-header/div[2]/div[1]/div/button")
    search_button.click()


@then("the corresponding search terms are listed for the user")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-glossary/div/app-small-header/div[2]/div['
                   '3]/div/label')))
    context.driver.quit()
