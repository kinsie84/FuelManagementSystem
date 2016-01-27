__author__ = 'D15123543'

from ItineraryManagement import *
import unittest

class TestAirportsInfo(unittest.TestCase):
    '''
    Class for AirportsInfo Unit Tests
    '''
    test_airports_info = AirportsInfo()
    airport_distances = (('DUB','LHR',448),('CDG','LHR',347),('ORD','BOG',4363))
    airport_codes = ['DUB','LHR','CDG']
    invalid_airport_codes = ['111','LLL','Y4!']

    def test_distance_between_airports(self):
        for airport1, airport2, distance in self.airport_distances:
           self.assertEqual(self.test_airports_info.get_dist_between_airports(airport1,airport2),distance)

    def test_distance_between_dublin_is_zero(self):
        airport1 = 'DUB'
        airport2 = 'DUB'
        self.assertEqual(self.test_airports_info.get_dist_between_airports(airport1,airport2),0)

    def test_search_for_valid_airport_code(self):
        for airport_code in self.airport_codes:
            self.assertTrue(self.test_airports_info.get_airport(airport_code))

    def test_search_for_invalid_airport_code(self):
        for invalid_code in self.invalid_airport_codes:
            self.assertEquals(self.test_airports_info.get_airport(invalid_code),"Invalid Code")  # "Invalid Code" is what is returned in the method.

    def test_load_airport_dictionary_with_invalid_file(self):
        invalid_csv = 'incorrect.csv'
        self.assertIsNone(self.test_airports_info.load_airports(invalid_csv))

    def test_load_airport_dictionary_with_valid_file(self):
        valid_csv = 'airport.csv'
        self.assertIsNone(self.test_airports_info.load_airports(valid_csv))

    def test_invalid_currency_code_of_a_country(self):
        invalid_code = 'VID'
        self.assertEquals(self.test_airports_info.get_exchange_rate(invalid_code),"Invalid currency code")

    def test_valid_exchange_rate_of_airport(self):
        airport = 'LHR'
        self.assertEquals(self.test_airports_info.get_country_exch_rate(airport),1.4029)

    def test_invalid_name_of_a_country(self):
        invalid_country = 1111
        self.assertEquals(self.test_airports_info.get_currency_code(invalid_country),"Invalid country name")

class TestItinerary(unittest.TestCase):
    '''
    Class for Itinerary Unit Tests
    '''
    Aircraft.load_aircrafts()

    def test_invalid_aircraft_object_not_created(self):
        invalid_aircraft = '744'
        route = ['DUB','ORD','AVI','JFK','LHR']
        test_itin = Itinerary(route,invalid_aircraft)
        self.assertEquals(test_itin.equipment,"Invalid Aircraft Type")

class TestAircraft(unittest.TestCase):
    '''
    Class for Aircraft Unit Tests
    '''
    Aircraft.load_aircrafts()
    test_aircraft = Aircraft('747')

    def test_invalid_aircraft_type_against_dictionary(self):
        invalid_type = 111
        self.assertFalse(Aircraft.check_aircraft_type(invalid_type))

    def test_check_distance_is_beyond_aircraft_range(self):
        self.assertEquals(self.test_aircraft.check_flight_dist(10000),"Cannot Make Distance") # range of 747 is 9800

    def test_check_distance_is_within_aircraft_range(self):
        self.assertEquals(self.test_aircraft.check_flight_dist(9000),"Possible") # range of 747 is 9800, fuel is 0

    def test_check_valid_distance_entered(self):
        self.assertEquals(self.test_aircraft.check_flight_dist('distance'),"Invalid Distance")

    def test_load_aircraft_dictionary_with_invalid_file(self):
        invalid_csv = 'incorrect.csv'
        self.assertIsNone(Aircraft.load_aircrafts(invalid_csv))

class TestRouteCalculator(unittest.TestCase):
    '''
    Class for RouteCalculator Unit Tests
    '''

    airport_info = AirportsInfo()
    test_aircraft5 = Aircraft('A330')
    route_calculator = RouteCalculator()
    valid_route = ['DUB','ORD','AVI','JFK','LHR']

    def test_number_of_permutations(self):
        self.assertEqual(len(self.route_calculator.get_route_perms(self.valid_route)),264)  # 264 is the number of unique permutations

    def test_confirm_cheapest_permutation_of_a_route(self):
        route = ['ORK','LHR','MAN','ORD','LIS']
        permutation = ['ORK', 'ORD', 'LIS', 'LHR', 'MAN', 'A330']
        self.assertEqual(self.route_calculator.get_cheapest_route(route,self.test_aircraft5,self.airport_info),permutation)

    def test_confirm_cheapest_permutation_of_a_route_has_extra_stop(self):
        route = ['DUB','AMS','KEF','JFK','LAX']
        permutation = ['DUB', 'KEF', 'LAX', 'JFK', 'KEF', 'AMS', 'A330']
        self.assertEqual(self.route_calculator.get_cheapest_route(route,self.test_aircraft5,self.airport_info),permutation)

    def test_no_route_returned_if_aircraft_cannot_make_any_permutation(self):
        test_aircraft6 = Aircraft('V22')
        self.assertEqual(self.route_calculator.get_cheapest_route(self.valid_route,test_aircraft6,self.airport_info),'No Route')

    def test_calculate_permutation_with_invalid_aircaft_type_returns_no_route(self):
        invalid_aircraft = Aircraft('111')
        route = ['DUB','AMS','KEF','JFK','LAX']
        self.assertEqual(self.route_calculator.get_cheapest_route(route,invalid_aircraft,self.airport_info),'No Route')

    def test_route_will_not_run_through_calculator_if_contains_invalid_airport(self):
        route = ['DUB','XXX','KEF','JFK','LAX']
        self.assertFalse(self.route_calculator.check_airport_code(route,self.airport_info))

    def test_route_will_run_through_calculator_if_all_airports_valid(self):
        route = ['DUB','ORK','KEF','JFK','LAX']
        self.assertTrue(self.route_calculator.check_airport_code(route,self.airport_info))

class TestInputOutput(unittest.TestCase):
    '''
    Class for InputOutput Unit Tests
    '''
    test_routes = "testroutes.csv"
    invalid_csv = 'invalid_csv'

    def test_load_input_output_list_with_invalid_file(self):
        self.assertEquals(InputOutput(self.invalid_csv).load_itineraries,"No File Found")

    def test_export_file_to_invalid_directory(self):
        invalid_directory = "D/Itineraries.csv"
        self.assertEquals(InputOutput(self.invalid_csv).export_routes(invalid_directory), "Invalid Directory")

    def test_load_itineraries_with_no_file_entered(self):
        no_file = ""
        self.assertEquals(InputOutput(no_file).load_itineraries,"No File Entered")

    def test_load_itineraries_with_valid_file(self):
        self.assertIsNone(InputOutput(self.test_routes).load_itineraries)

class TestSystem(unittest.TestCase):

    test_calculator = RouteCalculator()
    test_airports_info = AirportsInfo()
    test_route = ['LGW','LAX','LHR','ORD','LIS']

    def test_load_input_output_list_with_invalid_itinerary(self):
        self.assertIsNone(InputOutput('testroutes.csv').load_itineraries)

    def test_permutation_of_first_row_in_system_test_file_is_correct(self):
        test_aircraft1 = Aircraft('777')
        self.assertEquals(self.test_calculator.get_cheapest_route(self.test_route,
                                                                  test_aircraft1,self.test_airports_info),
                                                                    ['LGW', 'LIS', 'ORD', 'LAX', 'LHR', '777'])

    def test_permutation_of_second_row_in_system_test_file_returns_no_route(self):
        test_aircraft2 = Aircraft('BAE146')
        self.assertEquals(self.test_calculator.get_cheapest_route(self.test_route,
                                                              test_aircraft2,self.test_airports_info),
                                                                "No Route")
    def test_permutation_of_third_row_in_system_test_file_returns_no_route(self):
        test_aircraft3 = Aircraft('XXX')
        self.assertEquals(self.test_calculator.get_cheapest_route(self.test_route,
                                                              test_aircraft3,self.test_airports_info),
                                                                "No Route")

    def test_permutation_of_fourth_row_in_system_test_file_has_extra_stop(self):
        test_aircraft4 = Aircraft('737')
        test_extra_route = ['DUB', 'AMS', 'KEF', 'JFK', 'LAX']
        self.assertEquals(self.test_calculator.get_cheapest_route(test_extra_route,
                                                              test_aircraft4, self.test_airports_info),
                                                                ['DUB', 'AMS', 'KEF', 'JFK', 'LAX', 'JFK', '737'])

def suite():
    print()
    print ("Test Itinerary Management System")
    suite = unittest.TestSuite()
    #  AirportInfo Tests
    suite.addTest(TestAirportsInfo("test_distance_between_airports"))
    suite.addTest(TestAirportsInfo("test_distance_between_dublin_is_zero"))
    suite.addTest(TestAirportsInfo("test_search_for_valid_airport_code"))
    suite.addTest(TestAirportsInfo("test_search_for_invalid_airport_code"))
    suite.addTest(TestAirportsInfo("test_load_airport_dictionary_with_invalid_file"))
    suite.addTest(TestAirportsInfo("test_load_airport_dictionary_with_valid_file"))
    suite.addTest(TestAirportsInfo("test_invalid_currency_code_of_a_country"))
    suite.addTest(TestAirportsInfo("test_valid_exchange_rate_of_airport"))
    suite.addTest(TestAirportsInfo("test_invalid_name_of_a_country"))
    #  Itinerary Tests
    suite.addTest(TestItinerary("test_invalid_aircraft_object_not_created"))
    #  Aircraft Tests
    suite.addTest(TestAircraft("test_invalid_aircraft_type_against_dictionary"))
    suite.addTest(TestAircraft("test_check_distance_is_beyond_aircraft_range"))
    suite.addTest(TestAircraft("test_check_distance_is_within_aircraft_range"))
    suite.addTest(TestAircraft("test_check_valid_distance_entered"))
    suite.addTest(TestAircraft("test_load_aircraft_dictionary_with_invalid_file"))
    #  RouteCalculator Tests
    suite.addTest(TestRouteCalculator("test_number_of_permutations"))
    suite.addTest(TestRouteCalculator("test_confirm_cheapest_permutation_of_a_route"))
    suite.addTest(TestRouteCalculator("test_confirm_cheapest_permutation_of_a_route_has_extra_stop"))
    suite.addTest(TestRouteCalculator("test_no_route_returned_if_aircraft_cannot_make_any_permutation"))
    suite.addTest(TestRouteCalculator("test_calculate_permutation_with_invalid_aircaft_type_returns_no_route"))
    suite.addTest(TestRouteCalculator("test_route_will_not_run_through_calculator_if_contains_invalid_airport"))
    suite.addTest(TestRouteCalculator("test_route_will_run_through_calculator_if_all_airports_valid"))
    #  InputOutput Tests
    suite.addTest(TestInputOutput("test_load_input_output_list_with_invalid_file"))
    suite.addTest(TestInputOutput("test_export_file_to_invalid_directory"))
    suite.addTest(TestInputOutput("test_load_itineraries_with_no_file_entered"))
    suite.addTest(TestInputOutput("test_load_itineraries_with_valid_file"))
    # System Tests
    suite.addTest(TestSystem("test_load_input_output_list_with_invalid_itinerary"))
    suite.addTest(TestSystem("test_permutation_of_first_row_in_system_test_file_is_correct"))
    suite.addTest(TestSystem("test_permutation_of_second_row_in_system_test_file_returns_no_route"))
    suite.addTest(TestSystem("test_permutation_of_third_row_in_system_test_file_returns_no_route"))
    suite.addTest(TestSystem("test_permutation_of_fourth_row_in_system_test_file_has_extra_stop"))

    print ('\n')
    return suite

runnerS = unittest.TextTestRunner()
runnerS.run(suite())
