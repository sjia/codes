# coding=utf-8

import os
import time

from selenium import webdriver

#open Browser
br=webdriver.Firefox()
url="https://login.taobao.com/member/login.jhtml"
br.get(url)
br.implicitly_wait(8)

#Logon
br.find_element_by_id("TPL_username_1").send_keys('jaja1989')
#br.find_element_by_id("J_PwdV").send_keys("pwd")
#br.find_element_by_id("J_SubmitStatic").submit()

