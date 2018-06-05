from place import place 

class country:
    myself = None
    cities_list = []

    def __init__(self, myself):
        self.myself = myself
        self.cities_list = []

    def addCity(self, city):
        self.cities_list.append(city)
    
    def show(self):
        print("Country:",self.myself.name,"Url:",self.myself.url)
        for city in self.cities_list:
             print("City:",city.name,"Url:",city.url)

    






