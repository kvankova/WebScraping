import requests
from bs4 import BeautifulSoup
import pandas as pd


pd_exhibits = pd.DataFrame([], columns = ["Museum Name", "Exhibition Name", "When"])
pd_exhibits_future = pd_exhibits.copy()

## Albertina
URL = "https://www.albertina.at/en/exhibitions/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

current_results = soup.find(id="current")
future_results = soup.find(id="preview")

exhibition_elements = current_results.find_all("div", class_="col-md-12 box")
future_exhib_elements = future_results.find_all("div", class_="col-md-4 col-sm-6 col-xs-landscape-6 box")

print("Current Exhibitions")
for i, exhib_element in enumerate(exhibition_elements):
    title_element = exhib_element.find("div", class_="h2")
    timeline_element = exhib_element.find("div", class_="h3")
    pd_exhibits.loc[i,:] = ["Albertina", title_element.text, timeline_element.text]

print(pd_exhibits)
pd_exhibits.to_csv("exhibits.csv", mode = "a")

print("Upcoming Exhibitions")
for i, exhib_element in enumerate(future_exhib_elements):                             
    title_element = exhib_element.find("div", class_="h2")
    timeline_element = exhib_element.find("div", class_="h4")          
    pd_exhibits_future.loc[i,:] = ["Albertina", title_element.text, timeline_element.text]

print(pd_exhibits_future)
pd_exhibits_future.to_csv("exhibits.csv", mode = "a", header = False)

## Drop Duplicates
pd_exhibits_csv = pd.read_csv("exhibits.csv")
pd_exhibits_csv_dropDups = pd_exhibits_csv.drop_duplicates()
pd_exhibits_csv_dropDups[["Museum Name", "Exhibition Name", "When"]].to_csv("exhibits.csv")

