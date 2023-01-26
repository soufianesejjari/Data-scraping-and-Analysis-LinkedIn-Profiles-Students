# In[1]:


import os, time 
from selenium import webdriver
from bs4 import BeautifulSoup




driver = webdriver.Chrome('chromedriver')




driver.get("https://www.linkedin.com/login/")


elementID = driver.find_element_by_id('username')
elementID.send_keys("")
elementID = driver.find_element_by_id('password')
elementID.send_keys("")
elementID.submit()




driver.get('https://www.linkedin.com/school/ecole-nationale-superieure-d-informatique-et-d-analyse-des-systemes/people/?educationEndYear=2021')

rep = 2 #determine the rep enough to scroll all the page
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(rep):
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  time.sleep(5)
  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
    break
  new_height = last_height




src = driver.page_source
soup = BeautifulSoup(src, 'lxml')


uls=soup.find('ul', {'class': 'display-flex list-style-none flex-wrap'})
pr=[]
for li in uls.findAll('li'):
    try:
        r =li.find('a', {'class':'app-aware-link'}).get('href')
        pr.append(r)
    except:
        pass

c=0
out = []
for p in pr:
    driver.get(p)
    time.sleep(8)
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
#ember37 > div.ph5.pb5 > div.mt2.relative > ul > li > button > span > div
    #scraping name
    name = soup.find('h1', {'class' :  'text-heading-xlarge inline t-24 v-align-middle break-words'}).get_text().strip()
    title=soup.find('div', {'class' :  'text-body-medium break-words'}).get_text().strip()
    location=soup.find('span', {'class': 'text-body-small inline t-black--light break-words'}).get_text().strip()
    det= soup.find('span', {'class' :  'pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small t-black'})
    company=det.find('div').get_text().strip()
    person={}
    person["name"]=name
    person["title"]=title
    person["location"]=location
    person["company"]=company
    out.append(person)
    c+=1
    if(c>59):
        break




import json
print(json.dumps(out))
with open("persons.json", "w") as f:
    f.write(json.dumps(out, indent=4))


driver.close()
driver.quit()
