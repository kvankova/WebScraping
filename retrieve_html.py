import requests
from bs4 import BeautifulSoup
import pandas as pd


class html_retriever:
    def __init__(self, URL):
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def save_exhibits_to_csv(self, museum, id, class_1, class_title, class_time):

        pd_exhibits = pd.DataFrame([], columns = ["Museum Name", "Exhibition Name", "When"])
	  
        results = self.soup.find(id=id)
        elements = results.find_all("div", class_=class_1)

        for i, element in enumerate(elements):
            try:
                title_element = element.find("div", class_=class_title).text
            except: 
                title_element = element.find(class_title, class_=class_title).text
			
            try:
                timeline_element = element.find("div", class_=class_time).text
            except: 
                timeline_element = element.find(class_time, class_=class_time).text

            pd_exhibits.loc[i,:] = [museum, title_element, timeline_element]

        print(pd_exhibits)
        try:
            f = open("exhibits.csv")
            f.close()
            pd_exhibits.to_csv("exhibits.csv", mode = "a", header = False)
        except:
            pd_exhibits.to_csv("exhibits.csv", mode = "w", header = True)

        return

# Albertina

albertina_exhibits = html_retriever(URL="https://www.albertina.at/en/exhibitions/")

albertina_modern_exhibits = html_retriever(URL="https://www.albertina.at/en/albertina-modern/exhibitions/")

albertina_exhibits.save_exhibits_to_csv(museum="Albertina", id="current", 
                                        class_1="col-md-12 box", class_title="h2", class_time="h3")

albertina_exhibits.save_exhibits_to_csv(museum="Albertina", id="preview", 
                     class_1="col-md-4 col-sm-6 col-xs-landscape-6 box", class_title="h2", class_time="h4")

# Albertina modern

albertina_modern_exhibits.save_exhibits_to_csv(museum="Albertina Modern", id="current", 
 					       class_1="col-md-12 box float-none", class_title="h2", class_time="h3")

albertina_modern_exhibits.save_exhibits_to_csv(museum="Albertina Modern", id="preview", 
					       class_1="col-md-12 box float-none", class_title="h2", class_time="h3")



## Drop Duplicates
pd_exhibits_csv = pd.read_csv("exhibits.csv").reset_index()
pd_exhibits_csv_dropDups = pd_exhibits_csv.drop_duplicates(["Museum Name", "Exhibition Name", "When"])
pd_exhibits_csv_dropDups[["Museum Name", "Exhibition Name", "When"]].to_csv("exhibits.csv")

