# python 2

from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
import os
from OpenClassChecker import OpenClassChecker

CLASSES     = [['ECE','411'],
               ['ECE','428'],
               ['CS','446'],
               ['CS','427'],
               ['CS','411'],
               ['ECE','435']]


def main():
    OpenClassChecker(CLASSES).getAllClassStatus()

if __name__ == "__main__":
    main()
