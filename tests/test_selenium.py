import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_alert_text(driver):
    alert = Alert(driver)
    text = alert.text
    alert.accept()
    return text

def test_empty_username(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    driver.find_element(By.NAME,"name").clear()
    driver.find_element(By.NAME,"pw").send_keys("password456")
    driver.find_element(By.NAME,"sb").click()

    time.sleep(1)

    alert_text = get_alert_text(driver)

    assert alert_text == "username can't be empty."


def test_empty_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    driver.find_element(By.NAME,"name").send_keys("indu")
    driver.find_element(By.NAME,"pw").clear()
    driver.find_element(By.NAME,"sb").click()

    time.sleep(1)

    alert_text = get_alert_text(driver)

    assert alert_text == "password can't be empty."

def test_pw_length(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    driver.find_element(By.NAME,"name").send_keys("indu")
    driver.find_element(By.NAME,"pw").send_keys("123")
    driver.find_element(By.NAME,"sb").click()

    time.sleep(1)

    alert_text = get_alert_text(driver)

    assert alert_text == "password must be atleast 6 characters long"

def test_validinput(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    driver.find_element(By.NAME,"name").send_keys("indu")
    driver.find_element(By.NAME,"pw").send_keys("12345678")
    driver.find_element(By.NAME,"sb").click()

    time.sleep(3)

    current_url = driver.current_url
    assert "/register" in current_url,f"Expected redirect to success.html but got {curret_url}"

    body_text = driver.find_element(By.TAG_NAME,"body").text
    assert "Registration successful, indu" in body_text,f"greeting not fund: {body_text}"

    