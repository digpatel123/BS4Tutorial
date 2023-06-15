from bs4 import BeautifulSoup
import lxml
from chardet import detect


def get_encoding_type():
    with open("website.html", 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


with open('website.html', encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
all_p_tags = (soup.find_all(name="a"))

for tag in all_p_tags:
    print(tag.get("href"))

headings = soup.find(name="h1", id="name")

print(headings)
