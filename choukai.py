import selenium
import pickle
import time
import io
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from string import Template

# you are using chrome or firefox?

#pathFirefoxDriver = '.\geckodriver'
pathChormDriver = '.\chromedriver'

# Lấy config account
acountFile = open("websiteLink.txt", "r")
link = acountFile.readline()

######################### you are using firefox or chrome? #########################

#driver = selenium.webdriver.Firefox(executable_path=pathFirefoxDriver)
driver = selenium.webdriver.Chrome(executable_path=pathChormDriver)
#driver.get(link)
lessonLink = "http://tiengnhat24h.com/vi/luyen-nghe-doc/6-choukai-tasuku/bai-"
for lessonNumber in range(33, 34):
	lessonLink += str(lessonNumber)
	driver.get(lessonLink)
	lessonLink = "http://tiengnhat24h.com/vi/luyen-nghe-doc/6-choukai-tasuku/bai-"
	links = driver.find_elements_by_xpath("//source[@src]")
	countOfItemShowAnswer = 1
	for link in links: # the number of link audio file
		#get all button with text: Xem đáp án
		countButtonShowAns = driver.find_element_by_xpath('//button[text()="Xem đáp án"]')
		print(countButtonShowAns.text)
		
		print(link.get_attribute("src"))
		
		contents = driver.find_elements_by_xpath("//span[@class = 'fontjp']")
		write2File = io.open(("bai " + str(lessonNumber)+".txt"), "w", encoding="utf-8")
		
		#right click on element -> inspect element -> right click on element -> copy -> xpath
		
		idOfShowAnswer = "show_ans" + str(countOfItemShowAnswer)
		xpathOfShowAnswer = '//*[@id="' + idOfShowAnswer + '"]'
		show_answer = driver.find_element_by_xpath(xpathOfShowAnswer)
		print(xpathOfShowAnswer)
		#Another element is covering the element you are trying to click.
		#You could use execute_script() to click on this.
		driver.execute_script("arguments[0].click();", show_answer)
		
		#click xong show answer thi lai tang countOfItemShowAnswer
		countOfItemShowAnswer += 1
		
		#get content of table
		tableAnswer = driver.find_element_by_class_name('tbl_hoithoai')
		rows = tableAnswer.find_elements(By.TAG_NAME, 'tr')
		print('rows len: ' + str(rows.__len__()))
		
		for content in contents[:-1]:
			write2File.write(content.get_attribute("textContent") + '\n')
			
			for row in rows:
				col = row.find_elements(By.TAG_NAME, 'td')[1]
				print(col.text)
				write2File.write(col.text + '\n')
			print('\n')
			#print(content.get_attribute("textContent"))	
		write2File.close()