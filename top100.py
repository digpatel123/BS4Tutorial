from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

titles = soup.find_all(name="h3", class_="title")

top_titles = [movies.getText() for movies in titles]

movies = top_titles[::-1]

with open("movies.txt", mode="w") as f:
    for movie in movies:
        f.write(f"{movie}\n")