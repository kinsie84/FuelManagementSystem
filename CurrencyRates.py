__author__ = 'D15123543'


class CurrencyRates():
    '''
    Class for storing currency rates
    '''
    def __init__(self,currency_name, currency_code, conv_to_eur_rate, conv_from_eur_rate):
        self.currency_name = currency_name
        self.currency_code = currency_code
        self.conv_to_eur_rate = float(conv_to_eur_rate)
        self.conv_from_eur_rate = float(conv_from_eur_rate)

    def __str__(self):
        currency_rate_str = ''
        return 'The conversion rate from {} to Euro is {}'.format(self.currency_name,self.conv_to_eur_rate)


def main():
    test_rate = CurrencyRates('British Pound','EUR','1.4029','0.713')
    print(test_rate)

if __name__ == '__main__':
    main()
