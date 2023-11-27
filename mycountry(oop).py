class MyCountry:
    def __init__(self, country_name, city_list, area, continent):
        self.country_name = country_name
        self.city_list = city_list
        self.area = area
        self.continent = continent

    def Add_area(self, area_to_add, new_city):
        self.area += area_to_add
        self.city_list.append(new_city)

    def Is_it_big_enough(self):
        if len(self.city_list) <= 10 and self.area <= 100:
            return True
        return False

    def Change_continent(self):
        new_name = 'Vrolivia'
        self.continent = new_name

    def country_infocard(self):
        better_city_list = ''
        print(f"= Info Card of {self.country_name} Republic: =")
        print()
        for i in self.city_list:
            better_city_list += f'{i}, '

        print(f" Cities: {better_city_list}")
        print()
        print(f" Area: {self.area}(square meters)")
        print()
        print(f" Continent: {self.continent}")
        print()

# Twobahia

twobahia = MyCountry('Twobahia', ['St Mydawg', 'Eggland', 'Primerebest', 'Saupo San'], 360, 'Europe')
twobahia.Add_area(45, 'Arrysshorw')
twobahia.Change_continent()
twobahia.country_infocard()
print()
print(twobahia.Is_it_big_enough())




