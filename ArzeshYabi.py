from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
url = "http://saba.sums.ac.ir/"
UserName = ""
PassWord = ""
Driver = webdriver.Chrome(
	"D:\programming\PROJECT\-----SOURCE-----\86\chromedriver.exe")
Driver.get(url)
Driver.maximize_window()
Driver.find_element_by_xpath(
	'/html/body/div[4]/div[2]/div[1]/a[1]/span[2]').click()
time.sleep(1.5)
Driver.switch_to_frame(Driver.find_element_by_id("iframe_040101"))
Driver.find_element_by_xpath(
	'/html/body/form/div[3]/div/div[1]/div[1]/div[3]/div/input').send_keys(UserName)
Driver.find_element_by_xpath(
	'/html/body/form/div[3]/div/div[1]/div[1]/div[4]/div/input').send_keys(PassWord)
Driver.find_element_by_xpath(
	'/html/body/form/div[3]/div/div[1]/div[1]/div[6]/input').click()

Driver.switch_to_frame(Driver.find_element_by_id("iframe_FLASH_URL_TAB_ID"))
Driver.find_element_by_xpath(
	'/html/body/form/div[5]/div/div/table/tbody/tr/td[7]/input').click()


def choose_12():
	for i in range(2, 12):
		x_path = '/html/body/form/div[4]/div/div/table/tbody/tr[' + \
			str(i)+']/td[12]/input[9]'
		Driver.find_element_by_xpath(x_path).click()


def choose_16():
	for i in range(2, 12):
		x_path = '/html/body/form/div[4]/div/div/table/tbody/tr[' + \
			str(i)+']/td[12]/input[5]'
		Driver.find_element_by_xpath(x_path).click()


while True:
	Driver.switch_to.default_content()
	time.sleep(2)
	iframe = Driver.find_elements_by_tag_name('iframe')
	Driver.switch_to_frame(iframe[1])  # ListOstad
	Driver.find_element_by_xpath(
		'/html/body/form/div[5]/div/div/table/tbody/tr[1]/td[12]/input').click()
	Driver.switch_to.default_content()
	time.sleep(1)
	iframe = Driver.find_elements_by_tag_name('iframe')
	Driver.switch_to_frame(iframe[2])  # Nomre
	#choose_12()
	choose_16()
	Driver.find_element_by_xpath('/html/body/form/div[3]/input').click()  # Sabt
