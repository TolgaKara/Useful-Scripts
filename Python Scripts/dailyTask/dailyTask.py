from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from time import sleep



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
    print('00. ❌ Exit')
    print('-----------------------------------------------------')
    user_selection = int(input('> '))
    if(user_selection == 1):
      print("👔 Personal Branding")
    elif (user_selection == 2):
      print('♾️ Continously Learning')
    elif (user_selection == 3):
      print('🔍 Job Search')
    elif (user_selection == 4):
      print('📦 Project related')
    elif (user_selection == 0):
      print('❌ Exit')
      exit()





# Personal Branding
def personal_branding():
  Screen().printf('hello')

  return "hello"

# Continuously Learning

# Job Search

# Project Related

if __name__ == '__main__':
  app_menu()
