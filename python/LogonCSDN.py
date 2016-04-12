#coding=utf-8
import os
from selenium import webdriver
try:
    # open Browser
    br=webdriver.Firefox()
    url="http://passport.csdn.net/"
    br.get(url)

    # Logon
    br.find_element_by_xpath("//input[@name='username']").send_keys("sjiammm@gmail.com")
    br.find_element_by_xpath("//input[@name='password']").send_keys("Inpwd")
    br.find_element_by_xpath("//form[@id='fm1']/input[@tabindex='5']").click()

    #To Blog Page
    br.find_element_by_link_text("博客").click()
except:
    print "Error Occur.Please check the Scripts"
finally: pass