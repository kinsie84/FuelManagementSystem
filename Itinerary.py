__author__ = 'D15123543'

from Aircraft import Aircraft

class Itinerary:
    '''
    Class for storing aircraft routes and Aircraft objects of the equipment argument.
    '''
    def __init__(self, route, equipment):
        self.route = route
        self.equipment = self.check_aircraft_type(equipment)

    def __str__(self):
        itinerary_str = ''
        return "The itinerary route is: {}. The aircraft for the itinerary is: {}".format(self.route, self.equipment)

    def check_aircraft_type(self,equipment):  # check if aircraft type is valid
        if Aircraft.check_aircraft_type(equipment) is not False:
            return Aircraft(equipment)  # if valid, create aircraft object
        else:
            return 'Invalid Aircraft Type'

def main():
    Aircraft.load_aircrafts()
    route = ['DUB','LHR','SYD','JFK','AAL']
    valid_aircraft = 'A330'
    test_itin = Itinerary(route,valid_aircraft)
    print(test_itin)
    invalid_aircaft = '£££'
    test_itin2 = Itinerary(route,invalid_aircaft)
    print(test_itin2)

if __name__ == '__main__':
    main()

