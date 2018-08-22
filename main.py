#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
import os
from OpenClassChecker import OpenClassChecker
from TwilioClient import TwilioClient
import time

CLASSES     = [['ECE','411'],
               ['ECE','428'],
               ['CS','446'],
               ['CS','427'],
               ['CS','411'],
               ['ECE','435']]


def main():
    _class = OpenClassChecker(CLASSES)
    base_status = _class.getAllClassStatus()

    while True:
        status = _class.getAllClassStatus()
        
        if base_status != status:
            msg = ""
            for k ,v in status.items():
                msg += str(k) + ' ' + str(v) + "\n"
            print(msg)

            TwilioClient().sendMessage(msg)
            base_status = status
        
        time.sleep(10)



if __name__ == "__main__":
    main()

