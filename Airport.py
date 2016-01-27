__author__ = 'D15123543'


class Airport:
    '''
    Airport class used to hold information about airports.
    '''
    def __init__(self, airport_name, city_name, country, code, latitude, longitude):
        self.airport_name = airport_name
        self.city_name = city_name
        self.country = country
        self.code = code
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        airport_str = ''
        return "Airport: {}, is in {},{} at latitude: {} and longitude: {}".format(self.airport_name,
                                                         self.city_name,self.country,
                                                         self.latitude, self.longitude)

def main():
    airport1 = Airport('Name','City','Country','Code','0.53','.65')
    print(airport1)

if __name__ == '__main__':
    main()














