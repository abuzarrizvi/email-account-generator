import time;
import sys;

from selenium import webdriver;
import selenium.webdriver.chrome.service as service;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;

print("Username: ");
USER = raw_input();

print("Password: ");
PASS = raw_input();

print("Working...");

service = service.Service('../chromedriver');
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}

driver = webdriver.Remote(service.service_url, capabilities);
driver.get('https://www.instagram.com/justinbieber/followers/');


username = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/div[1]/input');
password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/div[2]/input');

login    = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/span/button');

username.clear();
username.send_keys(USER);

password.clear();
password.send_keys(PASS);

login.click();

print("Please wait...");

time.sleep(8);

loop = 1;

while (loop < 10) :

	driver.refresh();

	# Click followers
	driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]/a').click();

	time.sleep(2);

	# Click on random person
	driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[1]/div/div[1]/a').click();

	time.sleep(2);

	# Check if the person has a public account
	if (driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/div/h2').size() > 0) :
		# Click on users latest picture
		driver.find_element(By.XPATH, '//*[@id="pImage_49"]').Click();
		# Like the picture
		driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/article/div[2]/section[2]/a');
	else :
		break;

	loop = loop + 1;