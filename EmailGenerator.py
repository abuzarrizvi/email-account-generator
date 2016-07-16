import time;
import sys;

from selenium import webdriver;
import random
import selenium.webdriver.chrome.service as service;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;


print("Number of emails: ")
ammount = raw_input();

# Email address generator

print("Working...");

service = service.Service('../chromedriver');
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}

driver = webdriver.Remote(service.service_url, capabilities);
driver.get('https://www.random.org/strings/');

# Enter the ammount of emails into random.org to generate that ammount of strings
stringNumber = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/article/div/div[1]/div/form/div[1]/input');
stringNumber.clear();
stringNumber.send_keys(ammount);

# Enter the length of the strings
stringLength = driver.find_element(By.XPATH, '//*[@id="invisible"]/form/p[2]/input');
stringLength.clear();
stringLength.send_keys(ammount);

# Allow uppercase letters
uppercase = driver.find_element(By,XPATH, '//*[@id="invisible"]/form/p[3]/input[2]');
uppercase.click();

# Allow lowercase letters
lowercase = driver.find_element(By.XPATH, '//*[@id="invisible"]/form/p[3]/input[3]');
lowercase.click();

# Get strings
driver.find_element(By.XPATH, '//*[@id="invisible"]/form/p[6]/input[1]');