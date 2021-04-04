import requests
from bs4 import BeautifulSoup
from replacements import current_id_replacements, verse_replacements, synonyms_replacements, translation_replacements, purport_replacements

url = "https://vanisource.org/wiki/SB_1.1.1"

_source = requests.get(url)

soup = BeautifulSoup(_source.content, 'html.parser')

current_id = str(soup.find("h1", {"id": "firstHeading"}))
current_id = current_id_replacements(current_id)

verse = str(soup.find("div", {"class":"verse"}))
verse = verse_replacements(verse)

synonyms = str(soup.find("div", {"class": "synonyms"}))
synonyms = synonyms_replacements(synonyms)

translation = str(soup.find("div", {"class":"translation"}))
translation = translation_replacements(translation)

purport = str(soup.find("div", {"class": "purport"}))
purport = purport_replacements(purport)




knowledge = {"page_id": current_id, "verse": verse, "synonyms": synonyms, "translation": translation, "purport": purport}

# print(knowledge)
# print(type(knowledge))

with open('/home/somit/Projects/web-scraping/Srimad-Bhagavatam/First_Canto/Creation/Questions_By_The_Sages/SB_1.1/sb_1.1.1.json', 'w') as json_file:
    print(knowledge, file=json_file)