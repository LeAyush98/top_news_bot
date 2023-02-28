from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/")

html = response.text

tomato = BeautifulSoup(html, "html.parser")

# print(tomato.title.string)

# tomato_list = tomato.find_all(name="a")

# for _ in tomato_list:
#     print(_.getText())
#     print(_.get("href"))
#     print("\n\n")

tomato_score = tomato.select(selector = ".score")

tomato_points = []

for _ in tomato_score:
    tomato_points.append(int(_.getText().split(" ")[0])) 

# print(max(tomato_points))        

tomato_texts = tomato.select(selector= "tr td span.titleline")

tomato_text = []

for _ in tomato_texts:
    tomato_text.append(((_.find(name="a").getText()),(_.find(name="a").get("href"))))

tomato_dict = dict(zip(tomato_text, tomato_points))

for text, point in tomato_dict.items():
    if point == max(tomato_points):
        print(f"Article with most points ({point}) is: {text[0]} and the link is: {text[1]} ")