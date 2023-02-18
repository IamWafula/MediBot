import requests
from bs4 import BeautifulSoup 

url = "https://dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list.html"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# list of all Ids
listIDs = ["text-43cfb32669", "text-84402644fd", "text-7e4efe8d98", "text-471d739f5e", "text-ec8a27b996", "text-6273ca25ea", "text-c3b1516d81", "text-8615eeae11", "text-d388d5e01a", "text-c4d5670117", "text-86861213ae", "text-e1f5bdd063"]

# change this to loop through all IDs
main_content = soup.find(id="text-84402644fd")

paragraphs = main_content.find_all('p')

for paragraph in paragraphs:
    print(paragraph.text)