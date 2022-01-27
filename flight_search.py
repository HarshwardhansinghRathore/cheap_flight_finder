import datetime
import requests
from flight_data import FlightData


class FlightSearch:
    def __init__(self):
        now = datetime.datetime.now()
        self.today = now.strftime('%d/%m/%Y')
        months_6 = now + datetime.timedelta(days=30*6)
        self.now_plus_6_months = months_6.strftime('%d/%m/%Y')

    def search_for_flight(self, fly_to, price_to):

        base_url = 'https://tequila-api.kiwi.com'
        search_end_point = '/v2/search'
        search_url = f"{base_url}{search_end_point}"
        api_key = 'ywgGY_Bl60Yplxcf62nyxdBGmT2da_5_'
        headers = {
            'apikey': api_key
        }
        parameters = {
            'date_from': self.today,
            'date_to': self.now_plus_6_months,
            'fly_from': 'LON',
            'fly_to': fly_to,
            'curr': 'GBP',
            'flight_type': 'round',
            'price_from': '0',
            'price_to': price_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0
        }
        search_response = requests.get(url=search_url, params=parameters, headers=headers)
        try:
            data = search_response.json()['data'][0]
        except:
            print(search_response.json())
            print(f"there was no flight found for {fly_to}")
            return None
        flight_data = FlightData(
            destination_city=data['cityTo'],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            price=data["price"],
            out_date=data["route"][0]["local_departure"].split("T")[0]
        )
        return flight_data
