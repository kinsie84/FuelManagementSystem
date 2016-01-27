__author__ = 'D15123543'

import csv
import os

class Aircraft:
    '''
    Aircraft class used to hold aircraft types and their ranges.
    '''
    aircraft_fn = 'aircraft.csv'  # file used to load range dict, same for all instances.
    __range_dict = {}  # dictionary containing range for each aircraft type, loaded by static method only

    def __init__(self,aircraft_type):
        self.aircraft_type = aircraft_type
        if self.check_aircraft_type(aircraft_type) is not False: # assign the range of the aircraft type
            self.range = int(self.__range_dict[self.aircraft_type])
        else:
            self.range = 0


    @staticmethod
    # used to load range_dict that all instances will use
    def load_aircrafts(aircraft_file=aircraft_fn):
        try:
            with open(os.path.join("input",aircraft_file), "rt", encoding="utf8") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if row[0] != 'code':  # ignore header in aircraft file if exists
                           Aircraft.__range_dict [row[0]] = row[4]
                    except KeyError:
                        pass
                    except IndexError:
                        print("** Warning: Aircraft file contains row with incorrect format")
        except FileNotFoundError:
            print("** Warning: No Aircraft file found")
        except IsADirectoryError:
            print("** Warning: No Aircraft file entered therefore no file loaded")

    @staticmethod
    # check validity of aircraft types
    def check_aircraft_type(type):
        try:
            return Aircraft.__range_dict[str.upper(type)] # convert letter strings to upper case and check dict for string
        except (KeyError,TypeError):
            return False

    # check if distance is within aircraft range & how much fuel is needed to make distance
    def check_flight_dist(self,distance):
        try:
            if distance > self.range:
                return "Cannot Make Distance"
            else:
                return "Possible"
        except TypeError:
            return "Invalid Distance"

    def __str__(self):
        aircraft_str = ''
        return "{} has a range of {}".format(self.aircraft_type, self.range)


def main():
    Aircraft.load_aircrafts('invalid.csv')
    test_aircraft = Aircraft('777')
    print(test_aircraft)

    Aircraft.load_aircrafts()
    test_aircraft1 = Aircraft('330')
    print(test_aircraft1)

    Aircraft.load_aircrafts()
    test_aircraft2 = Aircraft('A330')
    print(test_aircraft2)
    print(test_aircraft2.check_flight_dist('10000'))
    print(test_aircraft2.check_flight_dist(15000))
    print(test_aircraft2.check_flight_dist(1000))

if __name__ == '__main__':
    main()
