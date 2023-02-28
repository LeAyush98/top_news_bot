from bs4 import BeautifulSoup as tomato

html = open("index.html", "r")

soup = tomato(html, "html.parser")

print(soup.title.string)