import time;
import sys;

import random;
import selenium.webdriver.chrome.service as service;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;


print("Number of emails: ");
ammount = raw_input();

print("This will take about" + ammount * 5 + "seconds");

time.sleep(5);

print("Working...");


# Get all the email usernames from emails.txt and store them inside an array

file = open("emails.txt", "r+");
x = file.read();

target_size = 10
count = len(x) / target_size;

emails = [ x[i:i+target_size] for i in range(0, len(x), target_size) ];

file.close();


# Connect to google.com to start sign up on the accounts

service = service.Service('../chromedriver');
service.start()
capabilities = {'chrome.binary': ''} # Enter path to chrome.exe in windows inside the '' tags.

driver = webdriver.Remote(service.service_url, capabilities);
driver.get('https://accounts.google.com/SignUp');

loopNumber = 0;

while loopNumber < ammount :

	time.sleep(2);

	Fname     = driver.find_element_by_name("FirstName");
	Lname     = driver.find_element_by_name("LastName");
	Address   = driver.find_element_by_name("GmailAddress");
	Password1 = driver.find_element_by_name("Passwd");
	Password2 = driver.find_element_by_name("PasswdAgain");

	Fname.clear();
	Lname.clear();
	Address.clear();
	Password1.clear();
	Password2.clear();

	Fname.send_keys("star");
	Lname.send_keys("bot");
	Address.send_keys(emails[loopNumber]); # Only unique thing in that will be set
	Password1.send_keys("StarBotttt");
	Password2.send_keys("StarBotttt");

	# Setting the birthday (Bloody nightmare to make)

	driver.find_element(By.XPATH, '//*[@id="BirthMonth"]/div[1]').click();
	driver.find_element(By.XPATH, '//*[@id=":4"]').click();

	time.sleep(5);

	driver.refresh();

	loopNumber = loopNumber + 1;

time.sleep(1);