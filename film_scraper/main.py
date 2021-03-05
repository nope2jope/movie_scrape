import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://www.afi.com/afis-100-years-100-movies/')
response.raise_for_status()

source = response.text

document = BeautifulSoup(source, 'html.parser')

title_source = document.find_all(name='h6', class_='q_title', limit=100)
title_list = []

for title in title_source:
    title_list.append(title.getText())

with open("must_watch.txt", 'w') as file:
    for entry in title_list:
        file.write(str(entry) + "\n")
    file.close()



