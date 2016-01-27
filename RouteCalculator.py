__author__ = 'D15123543'

from InputOutput import *
from itertools import permutations

class RouteCalculator:
    '''
    Class to calculate the cheapest permutation of a route
    '''
    @classmethod

    # check all airport codes in route are valid
    def check_airport_code(cls,route,airport_info):
        for code in route:
            if airport_info.get_airport(code) == "Invalid Code":
                print(route,"contains invalid code:",code,",therefore excluded from itinerary output")
                return False
        return True

    # get all possible route permutations, including optional extra stop
    def get_route_perms(cls,route):
        permutations_list = []
        route_perms = (list(permutation) for permutation in permutations(route[1::]))  # all permutations excluding the home airport
        for perm in route_perms:
            permutations_list.append(perm)
        for airport in route[1::]:
            extra_stop = route[1::] + [airport] # create route containing extra stop
            extra_stop_perms = (list(permutation) for permutation in permutations(extra_stop))  # all permutations with extra stop
            for perm in extra_stop_perms:
                if perm not in permutations_list:  # prevent duplicates which occur due to extra stop
                    permutations_list.append(perm)
        return permutations_list  # return list containing all permutations of route and route with extra stop

    # cycle through all permutations, calculate distance and price for each leg, return cheapest route
    def get_cheapest_route(cls,route,aircraft,airport_info):
        route_cost = 0  # holds cost of the cheapest route
        cheapest_route = 'No Route'  # holds cheapest permutation. If still "No Route" after cycle means route cannot be made by aircraft
        # run only if all codes in route are valid
        if cls.check_airport_code(route,airport_info) is True:
            for permutation in cls.get_route_perms(route):
                full_perm = [route[0]] + permutation + [route[0]]  # entire permutation with home legs at each end
                perm_cost = 0  # holds total cost of a permutation
                index = 0  # holds value of current index, used to identify airports in leg
                # run loop, flying aircraft through all legs, for the length of a permutation
                while index != len(full_perm)-1:
                    leg_dist = airport_info.get_dist_between_airports(full_perm[index],full_perm[index+1])  # distance between 2 airports in leg
                    if aircraft.check_flight_dist(leg_dist) == "Cannot Make Distance":  # if aircraft can't make leg distance, reset perm cost and break loop
                        perm_cost = 0
                        break
                    leg_exch_rate = airport_info.get_country_exch_rate(full_perm[index])  # exchange rate of departing airport in leg
                    perm_cost += (leg_exch_rate * leg_dist)  # add cost of perm leg to perm total cost
                    index += 1  # increment the index by one i.e. move on to next leg (if there is one)
                # if the perm cost is less than the current route cost (& is not zero) update cheapest_route & route_cost
                if route_cost == 0 and perm_cost != 0 or route_cost > perm_cost != 0:
                    route_cost = perm_cost  # the current route cost is updated to the value of the perm cost
                    cheapest_route = [route[0]] + permutation + [aircraft.aircraft_type] # the current cheapest route is updated to the value of the cheapest permuation
            return cheapest_route  # contains cheapest route of all permutations (if there is one)


def main():
    calc = RouteCalculator()
    Aircraft.load_aircrafts()
    airport_info = AirportsInfo()
    test_route1 = ['LGW','LIS','LHR','LAX','ORD']
    test_route2 = ['DUB','AMS','KEF','JFK','LAX']
    test_route3 = ['ORK','LHR','MAN','ORD','LIS']
    test_route4 = ['YYY','LHR','MAN','ORD','LIS']
    aircraft1 = Aircraft('BAE146')
    aircraft2 = Aircraft('777')
    aircraft3 = Aircraft('737')
    aircraft4 = Aircraft('111')
    print("For",test_route1,"with BAE146, the cheapest route is:",calc.get_cheapest_route(test_route1,aircraft1,airport_info))
    print("For",test_route1,"with 777, the cheapest route is:",calc.get_cheapest_route(test_route1,aircraft2,airport_info))
    print("For",test_route2,"with 737, the cheapest route is:",calc.get_cheapest_route(test_route2,aircraft3,airport_info))
    print("For",test_route2,"with 777, the cheapest route is:",calc.get_cheapest_route(test_route2,aircraft2,airport_info))
    print("For",test_route3,"with 737, the cheapest route is:",calc.get_cheapest_route(test_route3,aircraft3,airport_info))
    print("For",test_route3,"with 777, the cheapest route is:",calc.get_cheapest_route(test_route3,aircraft2,airport_info))
    print("testing to ensure no route returned if invalid code")
    print("For",test_route4,"with 777, the cheapest route is:",calc.get_cheapest_route(test_route4,aircraft3,airport_info))
    print("testing to ensure no route returned if invalid aircraft")
    print("For",test_route3,"with 111, the cheapest route is:",calc.get_cheapest_route(test_route3,aircraft4,airport_info))

if __name__ == '__main__':

    main()
