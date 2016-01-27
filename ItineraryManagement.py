__author__ = 'D15123543'

from InputOutput import *

class ItineraryManagement():
    '''
    Class for Running Main Program
    '''
    def __init__(self):
        self.load_aircrafts = Aircraft.load_aircrafts()
        self.airports_info = AirportsInfo()
        self.calculator = RouteCalculator()

    # display functionality options
    def display_menu(self):
        print("Choose an option from the menu below")
        print()
        print("1.Import an Itineraries .csv File")
        print("2.Export Itineraries File Sorted by Cheapest Route")
        print("3.Get Airport Details by Code")
        print("4.Get Euro Exchange Rate of a Country")
        print("5.Check the Range of an Aircaft")
        print("6.Get the Distance Between 2 Airports")
        print("0.Exit")
        print()

    # loop to ensure valid option chosen by user
    def choose_option(self):
        valid = False
        while not valid:
            try:
                option = int(input("Enter option number: "))
                if option >=0 and option <7:
                    valid = True
                else:
                    print("Enter a valid option")
            except ValueError:
                print("Please enter a valid option")
        return option

    # Manage user input by assigning number chosen to functionality
    def run_cmd_interface(self):
        print("*********************************************************")
        print()
        print("Welcome to the Itinerary Management Program")
        print()
        print("*********************************************************")
        print()
        no_exit = True
        while no_exit:
            self.display_menu()
            option = self.choose_option()
            if option == 1:
                print()
                file = input("Enter Name of File in the Input Directory (eg: testroutes.csv):")
                print()
                itineraries = InputOutput(file)
                print()
            elif option == 2:
                try:
                    itineraries.sort_routes(self.calculator,self.airports_info)
                    itineraries.export_routes()
                    print()
                    print("** File entitled 'Itineraries' exported to output directory. Exit menu to access **")
                    print()
                except UnboundLocalError:
                    print("Please load file first using option 1")
                    print()
                    pass
            elif option == 3:
                print()
                code = input("Enter Airport Code:")
                print(self.airports_info.get_airport(code))
                print()
            elif option == 4:
                print()
                country = input("Enter Country Name:")
                print(self.airports_info.get_currency_code(country))
                print()
            elif option == 5:
                print()
                aircraft = input("Enter Aircraft Type:")
                if Aircraft.check_aircraft_type(aircraft) is not False:
                    print()
                    print("The range of",aircraft,"is",Aircraft.check_aircraft_type(aircraft))
                else:
                    print()
                    print("You entered an invalid aircraft type")
                print()
            elif option == 6:
                print()
                code1 = input("Enter 3 Digit Home Airport Code:")
                code2 = input("Enter 3 Digit Destination Airport Code:")
                try:
                    print("Distance between",code1,"and",code2,"is",self.airports_info.get_dist_between_airports(code1,code2),"km")
                except:
                    print("Invalid Code Entered")
                print()
            elif option == 0:
                no_exit = False
        print("*********************************************************")
        print()
        print("You are now existing the Itinerary Management Program")
        print()
        print("*********************************************************")


def main():
    run_prog = ItineraryManagement()
    run_prog.run_cmd_interface()

if __name__ == '__main__':
    main()




