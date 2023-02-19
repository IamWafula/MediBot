
<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import re 
'''
=======
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

>>>>>>> 4714dd793d002130c9483211b3fe3dade1541178
url = "https://dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list.html"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# list of all Ids
listIDs = ["text-43cfb32669", "text-84402644fd", "text-7e4efe8d98", "text-471d739f5e", "text-ec8a27b996", "text-6273ca25ea", "text-c3b1516d81", "text-8615eeae11", "text-d388d5e01a", "text-c4d5670117", "text-86861213ae", "text-e1f5bdd063"]

# change this to loop through all IDs
main_contents=[]
paragraphs=[]
diseases=[]
for ids in listIDs:
    main_contents.append(soup.find(id=ids))

for elements in main_contents:
    paragraphs=elements.find_all('p')
    for paragraph in paragraphs:
        if "\n" in paragraph.text:
            k=paragraph.text
        
            diseases.append(k.replace("\n", ""))
        else:
            diseases.append(paragraph.text)
'''

url2 = 'https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'

page2 = requests.get(url2)
#body > div > table > tbody > tr > td:nth-child(3) > p > span
soup2 = BeautifulSoup(page2.content, 'html.parser')

rows = soup2.find_all('tr')

symptoms = []
for row in rows:
    symptom = row.find_all('td')[2].text[15:]
    symptoms.append(symptom)

print(symptoms)
print(len(rows))

#print(diseases)