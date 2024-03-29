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

class TestRPA1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_rPA1(self):
    self.driver.get("https://idealconsult.fortiddns.com:18124/syracuse-main/html/main.html?url=%3Frepresentation%3Dhome.%2524landing%26profile%3D~(loc~%27en-US~role~%27893b8bfc-13d6-4d7a-8d30-bc5a43590347~ep~%27b17dd696-d9c9-4f77-aa32-8e3121b4a992~appConn~())")
    self.driver.set_window_size(1101, 875)
    element = self.driver.find_element(By.LINK_TEXT, "video_stopSUNWAY")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_profile_bar_bookmark_dropdown:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_profile_bar_iconlink_sitemap .s_profile_bar_iconlink_i")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_profile_bar_iconlink_sitemap .s_profile_bar_iconlink_i")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_overlay_transparent")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "s_app").click()
    self.driver.find_element(By.CSS_SELECTOR, ".s_profile_bar_bookmark_dropdown:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "List of invoices").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "4-60-input").click()
    element = self.driver.find_element(By.ID, "4-61-input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_overlay_transparent")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "s_app").click()
    self.driver.find_element(By.CSS_SELECTOR, ".s_overlay_transparent").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_overlay_transparent")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".s-enter").click()
    self.driver.find_element(By.ID, "5-6-input").click()
    self.driver.find_element(By.ID, "5-6-input").send_keys("s3")
    self.driver.find_element(By.ID, "5-6-input").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".s-record-enter > .s-grid-cell:nth-child(2) > .s-inplace-value-read").click()
    self.driver.find_element(By.LINK_TEXT, "").click()
    self.driver.find_element(By.LINK_TEXT, "").click()
    element = self.driver.find_element(By.LINK_TEXT, "")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.LINK_TEXT, "").click()
    self.driver.find_element(By.LINK_TEXT, "").click()
    self.driver.find_element(By.CSS_SELECTOR, ".s-calendar-select").click()
    self.driver.find_element(By.LINK_TEXT, "Search").click()
    element = self.driver.find_element(By.LINK_TEXT, "Search")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".s-mn-list-btn > .s_btn_i").click()
    self.driver.find_element(By.LINK_TEXT, "CSV export").click()
    self.driver.find_element(By.LINK_TEXT, "Export").click()
    element = self.driver.find_element(By.LINK_TEXT, "Export")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s-field-file-link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".s-field-file-link").click()
    self.vars["win6675"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win6675"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_modal_page_head .s_page_header_subheader span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.LINK_TEXT, "close")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".s_modal_close_i").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_modal_close_i")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.ID, "4-60-input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_overlay_transparent")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "s_app").click()
    self.driver.find_element(By.LINK_TEXT, "").click()
    self.driver.find_element(By.ID, "7-5-input").click()
    self.driver.find_element(By.ID, "7-5-input").send_keys("s3")
    self.driver.find_element(By.ID, "7-5-input").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".s-record-enter > .s-grid-cell:nth-child(1) > .s-inplace-value-read").click()
    self.driver.find_element(By.LINK_TEXT, "Search").click()
    element = self.driver.find_element(By.LINK_TEXT, "Search")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".s-mn-list-btn > .s_btn_i").click()
    self.driver.find_element(By.LINK_TEXT, "CSV export").click()
    element = self.driver.find_element(By.LINK_TEXT, "CSV export")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Export").click()
    element = self.driver.find_element(By.LINK_TEXT, "Export")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".s-field-file-link").click()
    self.vars["win2168"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win2168"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    element = self.driver.find_element(By.CSS_SELECTOR, ".s_modal_close_i")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".s_modal_close_i").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
