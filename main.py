from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

movie_title_tags = soup.find_all(name="h3",class_="title")
movie_titles = []
index = 100
for movie_title_tag in movie_title_tags:
    try:
        title = movie_title_tag.getText().split(")")[1]
    except IndexError:
        title = movie_title_tag.getText().split(":")[1]
    movie_titles.append(f"{index}) {title}")
    index -= 1

print(movie_titles)

with open("movie_list.txt","w",encoding="utf-8") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")



# movie_list = [f"{str(num)} {movie}" for num,movie in enumerate(movie_titles[::-1],1)]
#
# with open("movie_list.txt","a",encoding="utf-8") as file:
#
#     for movie in movie_list:
#         file.write(f"{movie}\n")
