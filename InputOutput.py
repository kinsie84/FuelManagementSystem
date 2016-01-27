__author__ = 'D15123543'

from RouteCalculator import *
from Itinerary import *
from AirportsInfo import *

class InputOutput:
    '''
    Class to load & store itineraries from .csv and export sorted itineraries into another .csv.
    '''
    def __init__(self,itinerary_file):
        self.__itineraries = [] # populated when class instantiated, only accessed by methods in this class
        self.load_itineraries= self.import_itineraries(itinerary_file)
        self.__cheapest_routes = []  # populated by sort_routes method, only accessed by methods in this class

    # import itineraries csv file from input folder.
    def import_itineraries(self,itinerary_file):
        try:
            with open(os.path.join("input",itinerary_file), "rt", encoding="utf8") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        row = Itinerary(row[0:5], row[5])
                        self.__itineraries.append(row)
                    except IndexError: # don't load rows with that are not of the correct format
                        print(row,"not loaded. Itinerary must contain 5 airports and 1 aircraft")
                        pass
                    except KeyError:  # don't load rows with bad data
                        pass
        except FileNotFoundError:
                print("Invalid filename or directory, no file loaded")
                return "No File Found"
        except IsADirectoryError:
                print("No file entered therefore no file loaded")
                return "No File Entered"

    # calls pricing calculator to sort routes and appends to cheapest_route attribute.
    def sort_routes(self,calculator,airports_info):
        for itin in self.__itineraries:
            if itin.equipment != "Invalid Aircraft Type":  # do not run calculation for invalid aircraft types
                new_route = calculator.get_cheapest_route(itin.route,itin.equipment,airports_info)  # call route calculator
                if new_route != "No Route":  # No Route means aircraft could not make journey distance
                    self.__cheapest_routes.append(new_route)  # if valid route, append to cheapest_routes attribute
                else:
                    print(itin.equipment,"cannot make journey",itin.route,"therefore excluded from itinerary output" )
            else:
                print(itin.route,"contains an invalid aircraft type therefore excluded from itinerary output" )

    # export cheapest routes to csv file in output folder
    def export_routes(self,export_file="Itineraries.csv"):
        try:
            with open(os.path.join("output",export_file), "w", newline='') as file:
                writer = csv.writer(file, delimiter=",")
                for itinerary in self.__cheapest_routes:
                    try:
                        if itinerary is not None: # ignore itineraries that have routes with invalid airports
                            csvrow = itinerary
                            writer.writerow(csvrow)
                    except TypeError:  # if itinerary data type is not what is expected ignore.
                            pass
        except OSError:
                return "Invalid Directory"


def main():
    Aircraft.load_aircrafts()
    itin_file = InputOutput('testroutes.csv')
    calculator = RouteCalculator()
    airports_info = AirportsInfo()
    itin_file.sort_routes(calculator,airports_info)
    itin_file.export_routes()

if __name__ == '__main__':
    main()
