from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is logged into the platform and is on the 'Profile' page")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/2-prova/features/login/features/steps/driver/chromedriver")
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("rubens.moreira@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("mengao123")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'tabIndexMenuSidebar')))

    profile_button = context.driver.find_element_by_xpath(
        "/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul["
        "3]/li[1]/a")
    profile_button.click()

    WebDriverWait(context.driver, 40).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/ng-http-loader')))
    while context.driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed():
        pass


@when("the user correctly edits the required field 'Full name' and clicks 'Save data'")
def when(context):
    edition_name = context.driver.find_element_by_id("name")
    edition_name.send_keys("TESTE")

    edition_button = context.driver.find_element_by_id("save")
    edition_button.click()


@then("the Site returns a message confirming to the user that the 'Full Name' field has been changed.")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'profileUpdated')))
    context.driver.quit()
