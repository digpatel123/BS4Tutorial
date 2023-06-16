from bs4 import BeautifulSoup
import requests


# with open('website.html', encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'html.parser')
# all_p_tags = (soup.find_all(name="a"))
#
# for tag in all_p_tags:
#     print(tag.get("href"))
#
# headings = soup.find(name="h1", id="name")
#
# print(headings)

response = requests.get("https://news.ycombinator.com/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

article_tags = soup.find_all(name="span", class_="titleline")
article_scores = soup.find_all(name="span", class_="score")

article_list = []
score_list = []

for heading_links, highest_score in zip(article_tags, article_scores):
    a = heading_links.find(name="a").get("href")
    text = heading_links.find(name="a").getText()
    numbers = int(highest_score.getText().split()[0])
    score_list.append(numbers)
    article_list.append((numbers, text, a))

print(article_list)

max_score = max(score_list)
max_article_index = score_list.index(max_score)
max_article = article_list[max_article_index]

print("Article with the highest score!:")
print(f"Title: {max_article[1]}")
print(f"URL: {max_article[2]}")
print(f"Score: {max_article[0]}")