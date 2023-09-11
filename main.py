from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(page.text, "html.parser")

movies_name = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# print(movies_name)
movie_title = [movie.getText() for movie in movies_name]
movies=movie_title[::-1]
# print(movie_title)
with open("movies.txt","w") as file:
    for name in movies:
        file.write(f"{name}\n")