from notification_manager import NotificationManager
import flight_search
import requests

sheety_headers = {
            'Authorization': 'Bearer hhhfdja ghbajdnhabdjf dhnv'
        }
flight_search = flight_search.FlightSearch()
response = requests.get(url='https://api.sheety.co/69f888dcecb38a8884b36ac1e4dc15fd/flightDeals/prices',
                            headers=sheety_headers)
notification_manager = NotificationManager()
data = response.json()
for tour_data in data['prices']:
    destination = tour_data['iataCode']
    max_budget = tour_data['lowestPrice']
    match = flight_search.search_for_flight(destination, max_budget)
    try:
        notification_manager.send_mail(message=f'new cheap flight deal for {match.destination_city} with price lowest '
                                               f'as {match.price} Pounds on {match.out_date} return on '
                                               f'{match.return_date}')
    except:
        pass
