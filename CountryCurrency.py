__author__ = 'D15123543'


class CountryCurrency():
    '''
    Class for storing currencies of countries
    '''
    def __init__(self,country_name, country_code, currency_name, currency_code):
        self.country_name = country_name
        self.country_code = country_code
        self.currency_name = currency_name
        self.currency_code = currency_code

    def __str__(self):
        currency_str = ''
        return '{} is the currency used in {},the currency code is {}'.format(self.currency_name,
                                                                                self.country_name,
                                                                                self.currency_code)

def main():
    test_currency = CountryCurrency('Ireland','IRL','Euro','EUR')
    print(test_currency)

if __name__ == '__main__':
    main()
