# python 2

from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
import os

class OpenClassChecker:
   
    def __init__(self, classes):
        self.classes = classes


    def getClassStatus(self, class_code):
        os.environ['webdriver.chrome.driver'] = './chromedriver'
        self.browser = webdriver.PhantomJS('./phantomjs')
        
        self.browser.get("https://courses.illinois.edu/schedule/2018/fall/"+class_code[0]+'/'+class_code[1])
        page = requests.get("https://courses.illinois.edu/schedule/2018/fall/"+class_code[0]+'/'+class_code[1])
        
        #soup = BeautifulSoup(page.content, 'html.parser')
        soup = BeautifulSoup(self.browser.execute_script("return document.body.innerHTML"), 'lxml')
        #browser.quit()
        out = str(soup.findAll('span', {"class": 'sr-only'}))
        #print out
        status = []
        if 'restricted' in out:
            status.append('restricted')
        if 'open' in out:
            status.append('open')
        if 'closed' in out:
            status.append('closed')
        
        return status

    
    def getAllClassStatus(self):
        all = {}
        try:
            for class_code in self.classes:
                status = self.getClassStatus(class_code)
                code = class_code[0] + ' ' + class_code[1]
                all[code] = status
        except:
            pass
        return all
    
    
    
    def __del__(self):
        print('exiting...')
        self.browser.quit()