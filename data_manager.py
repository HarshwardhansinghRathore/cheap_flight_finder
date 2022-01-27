import requests


class DataManager:
    def __init__(self, ):
        sheety_headers = {
            'Authorization': 'Bearer hhhfdja ghbajdnhabdjf dhnv'
        }

        response = requests.get(url='https://api.sheety.co/69f888dcecb38a8884b36ac1e4dc15fd/flightDeals/prices',
                                headers=sheety_headers)
        self.sheet_data = response.json()

    def update_iata_code(self):
        for city_data in self.sheet_data['prices']:
            kiwi_parameters = {
                'term': city_data['city']
            }
            headers = {
                'apikey': 'ywgGY_Bl60Yplxcf62nyxdBGmT2da_5_'
            }
            kiwi_url = 'https://tequila-api.kiwi.com/locations/query'
            kiwi_response = requests.get(url=kiwi_url, params=kiwi_parameters, headers=headers)
            kiwi_data = kiwi_response.json()
            city_name = kiwi_data['locations'][0]['code']
            edit_parameters = {
                'price': {
                    'iataCode': city_name
                }
            }
            edit_response = requests.put(url=f"https://api.sheety.co/69f888dcecb38a8884b36ac1e4dc15fd/flightDeals/prices/{city_data['id']}",
                                         json=edit_parameters, headers=headers)
            print(edit_response.json())
