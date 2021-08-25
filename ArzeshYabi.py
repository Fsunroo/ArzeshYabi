from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
url = "http://saba.sums.ac.ir/Hermes.html"
UserName = ""
PassWord = ""
Driver = webdriver.Chrome()
Driver.get(url)
Driver.maximize_window()
delay = 10 # seconds
try:
    myElem = WebDriverWait(Driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe_-1')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
 
time.sleep(1)
Driver.find_element_by_xpath('/html/body/div[1]/div/div/app-root/app-profile-public/div/app-public/mat-sidenav-container/mat-sidenav-content/div/div/div[3]/mat-list[1]/div/mat-grid-list/div/mat-grid-tile[1]').click()
Driver.switch_to.default_content()
try:
    myElem = WebDriverWait(Driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe_37483724')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
#login fame
#Driver.switch_to_frame(Driver.find_element_by_id("iframe_37483724"))
#username
time.sleep(1)
Driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/p[1]/mat-form-field/div/div[1]/div/input").send_keys(UserName)
#password
Driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/p[2]/mat-form-field/div/div[1]/div/input").send_keys(PassWord)
#button
Driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/div/mat-card-actions/div/button").click()
#Dashbord frame
Driver.switch_to.default_content()
time.sleep(1)
Driver.switch_to_frame(Driver.find_element_by_id("iframe_-1"))
#Arzesh Yabi form
Driver.find_element_by_xpath('/html/body/form/div[5]/div/div/table/tbody/tr/td[7]/input').click()

while True:
	time.sleep(1)
	#Arzesh Yabi frame
	Driver.switch_to.default_content()
	try:
		myElem = WebDriverWait(Driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe_New_EvalAnswerSubject1_Tab')))
		print ("Page is ready!")
	except TimeoutException:
		print ("Loading took too much time!")
	#Driver.switch_to_frame(Driver.find_element_by_id("iframe_New_EvalAnswerSubject1_Tab"))
	#proffesors#1
	time.sleep(1)
	Driver.find_element_by_xpath('/html/body/form/div[5]/div/div/table/tbody/tr[1]/td[12]/input').click()
	#question frame
	Driver.switch_to.default_content()
	try:
		myElem = WebDriverWait(Driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe_New_EvalAnswerListItem_Tab')))
		print ("Page is ready!")
	except TimeoutException:
		print ("Loading took too much time!")
	#Driver.switch_to_frame(Driver.find_element_by_id("iframe_New_EvalAnswerListItem_Tab"))
	#NO Answer
	time.sleep(1)
	for i in range(2,12):
		xpath = f'/html/body/form/div[4]/div/div/table/tbody/tr[{i}]/td[12]/input[10]'
		Driver.find_element_by_xpath(xpath).click()
	Driver.find_element_by_xpath('/html/body/form/div[3]/input').click()
	time.sleep(1)
