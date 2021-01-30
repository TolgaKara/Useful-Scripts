from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from time import sleep
from tinydb import TinyDB, Query
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
import webbrowser

load_dotenv()

LINKEDIN_USERNAME = os.getenv("LINKEDIN-USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN-PASSWORD")


# Menu
def app_menu():
  isExit=True
  while(isExit):
    print('Daily Task')
    print('A automation Script which should improve my workflow.')
    print('-----------------------------------------------------')
    print('01. 👔 Personal Branding')
    print('02. ♾️  Continuously Learning')
    print('03. 🔍 Job Search')
    print('04. 📦 Project related')
    print('05. ⚙️ Configuration')
    print('00. ❌ Exit')
    print('-----------------------------------------------------')
    user_selection = int(input('> '))
    if(user_selection == 1):
      personal_branding()
    elif (user_selection == 2):
      continously_learning()
    elif (user_selection == 3):
      job_search()
    elif (user_selection == 4):
      project_related()
    elif (user_selection == 5):
      settings()
    elif (user_selection == 0):
      print('❌ Exit')
      exit()
    else:
      print('❌❌❌ Sadly this menu point is not available ❌❌❌')





# Personal Branding
def personal_branding():
  print("👔 Personal Branding")
  print('-----------------------------------------------------')
  linkedin_network_url = 'https://www.linkedin.com/mynetwork/'
  webbrowser.register('chrome',
	  None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
  webbrowser.get('chrome').open(linkedin_network_url)
  isOnLinkedNetwork = True
  linkedin_network_user_input = ""
  while(isOnLinkedNetwork):
    linkedin_network_user_input=input('Have you connected with 3 relevant Networks? (y / n)')
    if(linkedin_network_user_input == 'y'):
      isOnLinkedNetwork = False
    else:
      isOnLinkedNetwork = True




  sleep(5)



# Continuously Learning
def continously_learning():
  print('♾️ Continously Learning')
  print('-----------------------------------------------------')


# Job Search
def job_search():
  print('🔍 Job Search')
  print('-----------------------------------------------------')


# Project Related
def project_related():
  print('📦 Project related')
  print('-----------------------------------------------------')


# Settings
def settings():
  print('05. ⚙️ Configuration')
  print('-----------------------------------------------------')


if __name__ == '__main__':
  global db
  db = TinyDB('dailytaskdb.json')

  app_menu()
