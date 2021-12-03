from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("that the user is logged into the site, and is on the 'General Report' screen")
def given(context):
    context.driver = webdriver.Chrome(
        "/home/rubens/PycharmProjects/Dellead/2-prova/features/report/features/steps/driver/chromedriver")
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

    report_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/nav/div/div["
                                                         "2]/ul[2]/li[2]/a")
    report_button.click()

    WebDriverWait(context.driver, 40).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/ng-http-loader')))
    while context.driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed():
        pass


@when("you select an existing edition")
def when(context):
    select = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-management-reports'
                                               '/div/app-general-report/div/div/app-custom-card/div/div['
                                               '2]/div/div/div/div[1]/app-filter-report/form/div[1]/div['
                                               '3]/ng-multiselect-dropdown/div/div[1]/span')
    select.click()

    option_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app"
                                                         "-management-reports/div/app-general-report/div/div/app"
                                                         "-custom-card/div/div[2]/div/div/div/div["
                                                         "1]/app-filter-report/form/div[1]/div["
                                                         "3]/ng-multiselect-dropdown/div/div[2]/ul[2]/li[1]/div")
    option_button.click()

    contraste_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app"
                                                            "-accessibility-bar/div/nav/div/ul/li[7]/a/span[2]")
    contraste_button.click()
    enter_button = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app'
                                                        '-management-reports/div/app-general-report/div/div/app'
                                                        '-custom-card/div/div[2]/div/div/div/div['
                                                        '1]/app-filter-report/form/div[2]/div/div[1]/button')
    enter_button.click()


@then("the edit selected by the user is exposed, making the edits for that option visible to the user")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'body')))
    context.driver.quit()
