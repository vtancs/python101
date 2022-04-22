import requests
"""
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])
"""
# GET CURRENT PRICE DATA
def get_current_data(from_sym='BTC', to_sym='USD', exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price'    
    
    parameters = {'fsym': from_sym,
                  'tsyms': to_sym }
    
    if exchange:
        print('exchange: ', exchange)
        parameters['e'] = exchange
        
    # response comes as json
    response = requests.get(url, params=parameters)   
    data = response.json()
    
    return data
    
print(get_current_data('BTC','USD','coinbase'))