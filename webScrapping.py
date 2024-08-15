import requests
from bs4 import BeautifulSoup
import csv

# request to a rotten tomatoes' website using Requests library
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/genres:animation~sort:popular'
response = requests.get(url)

# store website html content in a variable using BeautifulSoap library
soup = BeautifulSoup(response.content, "html.parser")

# extract movie names, release dates and ratings data from web page using html tags and attributes
movie_names = soup.find_all('span', attrs={'data-qa': 'discovery-media-list-item-title'})
release_dates = soup.find_all('span', attrs={'data-qa': 'discovery-media-list-item-start-date'})
ratings = soup.find_all('rt-text', attrs={'slot': 'criticsScore'})

# store the extract data into a csv file
with open('Web Scrapping.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "release_date", "ratings"]
    writer.writerow(field)

    for i in range(len(movie_names)):
        movie_name = movie_names[i].text.replace("\n          ", "").replace("\n        ", "")
        released_date = release_dates[i].text.replace("\n            ", "").replace("\n          ", "").replace("Opened", "").replace("Re-released", "").replace("Opens", "")
        rating = ratings[i].text.replace(" ", "")

        writer.writerow([movie_name, released_date, rating])
