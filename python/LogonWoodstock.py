# -*- coding: utf-8 -*-

from selenium import webdriver
import os

#open browser
br=webdriver.Firefox()
url='http://c4t01811.itcs.hp.com/pages/login'
br.get(url)
br.implicitly_wait(6)

# logon
br.find_element_by_id('email').send_keys('en-luan.jia@hp.com')
br.find_element_by_id('password').send_keys('3edcvfr4%tgb')
br.find_element_by_xpath("//input[@name='commit']").submit()

#open file compare tool
br.find_element_by_xpath("//ul[@class='ws-nav']/li[3]/a").click()
br.find_element_by_xpath("//a[@href='/commands/file_compare']").click()
br.implicitly_wait(20)

#import source and target file, failed, un-locatable
#br.switch_to_frame('_sl_historyFrame')



