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
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = cleantext.strip()

  return cleantext

def clean_stopwords(cleantext):
  stop_words = set(stopwords.words('english'))
  custom_stop_words=[";",":"]
  word_tokens = word_tokenize(cleantext)
  filtered_sentence = [w for w in word_tokens if not w in stop_words]
  filtered_sentence = [w for w in word_tokens if not w in custom_stop_words]

  filtered_sentence = []

  for w in word_tokens:
    if w not in stop_words and w not in custom_stop_words:
        filtered_sentence.append(w)
  return filtered_sentence

def get_counts_of_words(articles_content):
  words = clean_stopwords(articles_content)
  #clean trailing whitespaces
  words = list(map(lambda s: s.strip(), words))
  words_count_obj = {}
  for word in words:
    words_count_obj[word] = articles_content.count(word)
  print(words_count_obj)
  # TODO filter out values which are under 5 times appearance
  # TODO sort the entries and get the top 20
  exit()
  return words_count_obj

def get_devto_articles():
  dev_to_page = "1"
  dev_to_per_page = "1000"
  dev_to_tags = "javascript,webdev,beginners,programming,react,python,tutorial,csstechtalks,writing,bash,devjournal,performance,gatsby,code,firebase,agile,svelte,technology,oop,remotehelp,100daysofcode,git,database,codequality,news,laravel,graphql,codepen,watercooler,startup,functional,serverless,architecture,challenge,algorithms,vscode,todayilearned,django,learning,coding,motivation,development,npm,redux,frontend,api,sql,nextjs,mongodb,codenewbie,productivity,node,career,html,discuss,devops,vue,typescript,showdev,opensource,github,testing,php,security"
  dev_to_tags_exclude= "gamedev,flutter,rust,blockchain,kotlin,swift,ux,azure,cloud,computerscience,archlinux,ios,reactnative,kubernetes,wordpress,csharp,angular,dotnet,go,ruby,datascience,rails,cpp,mobile,android"
  dev_to_state = ["fresh","rising","all"]
  dev_to_top = 2
  dev_to_rest_url = "https://dev.to/api/articles?page={}?per_page={}?tags={}?tags_exclude={}?state={}?top={}".format(dev_to_page, dev_to_per_page, dev_to_tags, dev_to_tags_exclude, dev_to_state[2], dev_to_top)
  # TODO Future write one Developer from the Database of an desired company a (predefined message) or custom message
  dev_articles_json = requests.get(dev_to_rest_url).json()
  dev_articles_list = []
  #print(len(dev_articles_json))

  #print(dev_articles_json[0])
  for i in range(0,10):
    dev_articles_list.append({"id":dev_articles_json[i]['id'], "title":dev_articles_json[i]['title'],"description":dev_articles_json[i]['description'],"readable_publish_date":dev_articles_json[i]['readable_publish_date'],"url":dev_articles_json[i]['url'], "tags":dev_articles_json[i]['tags'],"user_name":dev_articles_json[i]['user']['name'],"user_username":dev_articles_json[i]['user']['username'], "user_github_username":dev_articles_json[i]['user']['github_username'], "user_profile_image":dev_articles_json[i]['user']['profile_image']})
  #print(dev_articles_list)

  #dev_to_articles_content_url =
  dev_full_articles_list=[]
  for article in dev_articles_list:
    article['content'] = cleanhtml(requests.get("https://dev.to/api/articles/{}".format(article['id'])).json()['body_html'])
    dev_full_articles_list.append(article)


  dev_final_article = []
  for article in dev_full_articles_list:
    article['content'] = get_counts_of_words(article['content'])
    dev_final_article.append(article)
  return dev_final_article

# Personal Branding
def personal_branding():
  print("👔 Personal Branding")
  print('-----------------------------------------------------')
  linkedin_network_url = 'https://www.linkedin.com/mynetwork/'
  webbrowser.register('chrome',
	  None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
  # Connect to 3 Developers
  webbrowser.get('chrome').open(linkedin_network_url)

  # Write prefessional Developers a Message and Network with them
  ## Fetch content and user and see if I find a topic which I can ask or give some compliment
  dev_to_articles = get_devto_articles()

  # After Completion
  isPersonalBranding = True
  personal_branding_user_input = ""
  while(isPersonalBranding):
    print("""
[1] Network with 3 Developers || Designers || Analysts
[2] Write a professional Developers a Message and Network with them
[3] Review LinkedIn and either solve one skill or work on the Branding
[4] Review GitHub and Change 1 Repos Description || Tags || Location, also Declutter
    """)
    personal_branding_user_input=input('Have you finished these Task for Personal Branding (y / n) ?')
    if(personal_branding_user_input == 'y'):
      isPersonalBranding = False
    else:
      isPersonalBranding = True




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
  # If possible add Developers from a desired company on linkedin to the database the url of them and write professional Message


if __name__ == '__main__':
  global db
  db = TinyDB('dailytaskdb.json')

  app_menu()
