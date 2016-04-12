# -*-coding.utf-8-*-
from selenium import webdriver
import time
import os
import sys

try:
    # open FF
	br = webdriver.Firefox()
	url = "https://servername/console/#/home"
	br.get(url)
	br.implicitly_wait(10)
	print "page open"
	# Logon
	br.find_element_by_name('userName').send_keys("userName")
	br.find_element_by_name('password').send_keys("password")
	br.find_element_by_xpath('//button[1]').click()
	br.implicitly_wait(10)
	# retrieve value



except EOFError:
	s = sys.exc_Info()
	print "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
finally:
	pass
