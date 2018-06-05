import requests
from bs4 import BeautifulSoup
from country import country 
from place import place
class twirends:
    countries_list = None
    website = None
    soup = None

    def __init__(self):
        self.countries_list = []
        self.website = "https://trends24.in/"
        page = requests.get(self.website)
        self.soup = BeautifulSoup(page.content,'html.parser')
        for country_link in self.soup.find_all('ul',{'class':'location-menu__city-list'}):
            locations = [] 
            for location_link in (country_link.children):
                locations.append(location_link.a)
            
            loc = locations.pop(0)

            p = place(loc.get_text(), loc["href"])
            c = country(p)
    
            for loc in locations:
                p = place(loc.get_text(), loc["href"])
                c.addCity(p)

            self.countries_list.append(c)
            
    def show(self):
        for country in self.countries_list:
            country.show()


if __name__ == "__main__":
    trends = twirends()
    






