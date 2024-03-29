# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDodaj():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dodaj(self):
    self.driver.get("https://thermores.pwr.edu.pl/panel/description/index/page_id/8/")
    self.driver.set_window_size(930, 788)
    self.vars["starttitle"] = self.driver.title
    if self.driver.execute_script("return (arguments[0] == \"Katedra Termodynamiki i Odnawialnych Źródeł Energii - Panel / Logowanie\")", self.vars["starttitle"]):
      self.driver.find_element(By.ID, "other-accounts").click()
      self.driver.find_element(By.ID, "login").send_keys(self.vars["username"])
      self.driver.find_element(By.ID, "password").send_keys(self.vars["password"])
      self.driver.find_element(By.CSS_SELECTOR, ".submit").click()
    self.vars["elementCount"] = len(self.driver.find_elements(By.XPATH, "//tr[td/a/text() = \"self.vars[\"title\"]\"]"))
    if self.driver.execute_script("return (arguments[0] > 0)", self.vars["elementCount"]):
      self.driver.find_element(By.XPATH, "//tr[td/a/text() = \"self.vars["title"]\"]/td[9]/div/a[1]").click()
    else:
      self.driver.get("https://thermores.pwr.edu.pl/panel/description/add/page_id/8/")
    self.driver.find_element(By.LINK_TEXT, "Publikowanie").click()
    self.vars["elementCount"] = len(self.driver.find_elements(By.XPATH, "//input[@id = \"approved\"]"))
    if self.driver.execute_script("return (arguments[0] == 0)", self.vars["elementCount"]):
      self.driver.find_element(By.ID, "draft").click()
      self.driver.find_element(By.ID, "approved").click()
      self.driver.find_element(By.ID, "published").click()
    self.driver.find_element(By.LINK_TEXT, "Treść").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys(self.vars["title"])
    self.driver.switch_to.frame(0)
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'self.vars[\"content\"]'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".pwr-btn-submit").click()
  
