__author__ = 'D15123543'

import os
import csv
from math import cos, pi, sin, acos
from Airport import Airport
from CountryCurrency import CountryCurrency
from CurrencyRates import CurrencyRates


class AirportsInfo:
    '''
    Class for storing information about all airports including currencies of counties in those airports
    and current exchange rates.
    '''
    airport_fn = "airport.csv"
    currency_fn = "countrycurrency.csv"
    exchange_rate_fn = "currencyrates.csv"

    def __init__(self, airport_file = airport_fn, currency_file = currency_fn, exchange_rate_file = exchange_rate_fn):
        # dictionary attributes can only be accessed from methods within the class
        self.__airport_dict = {}
        self.__currency_dict = {}
        self.__exchange_rate_dict = {}
        # above attributes can only be populated at instantiation by the below attributes which load csv files into them.
        self.create_airport_dict = self.load_airports(airport_file)
        self.create_currency_dict = self.load_currencies(currency_file)
        self.create_exchange_rate_dict = self.load_exchange_rates(exchange_rate_file)

    # import airport file & store rows as Airport objects in a dictionary
    def load_airports(self, airport_file):
        try:
            with open(os.path.join("input",airport_file), "rt", encoding="utf8") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        self.__airport_dict[row[4]] = Airport(row[1],row[2],row[3],row[4],float(row[6]),float(row[7]))
                    except KeyError:
                        pass
                    except IndexError:
                        print(row,"** Warning: Airports file contains row with incorrect format")
        except FileNotFoundError:
            print ("** Warning: No Airports file found")
        except IsADirectoryError:
            print("** Warning: No Airports file entered therefore no file loaded")


    # import currency file & store rows as CountryCurrency objects in a dictionary
    def load_currencies(self, currency_file):
        try:
            with open(os.path.join("input",currency_file), "rt", encoding="utf8") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if row[0] != 'name': # if first row is header, ignore.
                            self.__currency_dict[row[3]] = CountryCurrency(row[0],row[3],row[17],row[14])
                    except KeyError:
                        pass
                    except IndexError:
                        print(row,"** Warning: Country Currencies file contains row with incorrect format")
        except FileNotFoundError:
            print ("** Warning: No Country Currencies file found")
        except IsADirectoryError:
            print("** Warning: No Country Currencies entered therefore no file loaded")

    # import exchange rate file & store rows as CurrencyRates objects in a dictionary
    def load_exchange_rates(self, exchange_rate_file):
        try:
            with open(os.path.join("input",exchange_rate_file), "rt", encoding="utf8") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                       self.__exchange_rate_dict[row[1]] = CurrencyRates(row[0],row[1],float(row[2]),float(row[3]))
                    except KeyError:
                        pass
                    except IndexError:
                        print(row,"** Warning: Exchange Rates file contains row with incorrect format")
        except FileNotFoundError:
            print ("** Warning: No Exchange Rates file found")
        except IsADirectoryError:
            print("** Warning: No Exchange Rates file entered therefore no file loaded")

    # take airport code as input to see if there's a match in airport_dict.keys
    def get_airport(self,code):
        try:
            return self.__airport_dict[code.upper()]
        except KeyError:
            return "Invalid Code"

    @staticmethod
    # formula for calculating the great circle distance of two places
    def great_circle_dist(lat_one, long_one, lat_two, long_two):
        earth_radius = 6371
        rads = (pi / 180) # convert degrees to radians
        phi = 90 * rads
        lat1 = lat_one * rads
        long1 = long_one * rads
        lat2 = lat_two * rads
        long2 = long_two * rads
        try:
            calc_distance = int(acos(sin(phi-lat1) * sin(phi-lat2) *
                                        cos(long1-long2) + cos(phi-lat1) *
                                        cos(phi-lat2) ) * earth_radius)
            return calc_distance
        except ValueError:
            return 0

    # call the distance calculator with each airports lat & long as arguments.
    def get_dist_between_airports(self,code1,code2):
        airport1 = self.get_airport(code1)
        airport2 = self.get_airport(code2)
        return self.great_circle_dist(airport1.latitude, airport1.longitude, airport2.latitude,airport2.longitude)

    # take in a code, if valid, pass country value from dict to get_currency_code method
    def get_country_exch_rate(self,code):
        for key, value in self.__airport_dict.items():
            if code == key:
                return self.get_currency_code(value.country)
        else:
            return "Invalid airport code"

    # take in a country name, if valid, pass currency_code value from dict to get_exchange_rate method
    def get_currency_code(self,country):
        for key, value in self.__currency_dict.items():
            if country == value.country_name:
                return self.get_exchange_rate(value.currency_code)
        else:
            return  "Invalid country name"

    # take in a currency code, if valid, return the Euro conversion rate of that currency
    def get_exchange_rate(self,currency_code):
        for key, value in self.__exchange_rate_dict.items():
            if key == currency_code:
                return value.conv_to_eur_rate
        else:
            return "Invalid currency code"


def main():
    test_airport_info = AirportsInfo()
    print(test_airport_info.get_airport('ORD'))
    print("Euro Conv Rate:",test_airport_info.get_currency_code('Brazil'))
    print("Euro Exchange Rate in Heathrow is",test_airport_info.get_country_exch_rate('LHR'))
    print("Distance is:",test_airport_info.get_dist_between_airports('BOG','LHR'),"km")

if __name__ == '__main__':
    main()


