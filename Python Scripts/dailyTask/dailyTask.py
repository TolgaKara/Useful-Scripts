from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from time import sleep
from tinydb import TinyDB, Query

# Menu
def app_menu():
  isExit=True
  while(isExit):
    print('Daily Task')
    print('A automation Script which should improve my workflow.')
    print('-----------------------------------------------------')
    print('01. 👔 Personal Branding')
    print('02. ♾️ Continuously Learning')
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

# Continuously Learning
def continously_learning():
  print('♾️ Continously Learning')

# Job Search
def job_search():
  print('🔍 Job Search')

# Project Related
def project_related():
  print('📦 Project related')

# Settings
def settings():
  print('05. ⚙️ Configuration')

if __name__ == '__main__':
  global db
  db = TinyDB('dailytaskdb.json')

  app_menu()
