import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 33.773560
MY_LONG = -84.296562
RAIN_LAT = -5.147665
RAIN_LONG = 119.432732
RAIN_param = (RAIN_LAT, RAIN_LONG)
q_param = (MY_LAT, MY_LONG)
MY_API = 'myapi'
twilio_account_sid = 'accountid'
twilio_auth_token = 'authtoken'

parameters = {#'lat': MY_LAT,
              #'lon': MY_LONG,
                'q': RAIN_param,
              'key': MY_API,
                'days': 2
}

rain_api = requests.get('http://api.weatherapi.com/v1/forecast.json', params=parameters)
rain_api.raise_for_status()
rain_text = rain_api.json()
# print(rain_text)
weather_codes_next_12_hours = []

will_rain = False

for _ in range(7, 19): # This would be from 7am to 6pm. which would be 12 hours somehow idk
    x = _
    weather_codes_next_12_hours.append(rain_text['forecast']['forecastday'][1]['hour'][x]['condition']['code'])
    if rain_text['forecast']['forecastday'][1]['hour'][x]['condition']['code'] > 1030:
        will_rain = True

# print('Complete')
# print(weather_codes_next_12_hours)
if will_rain:
   client = Client(twilio_account_sid, twilio_auth_token)
   message = client.messages \
       .create(
       body="Bring an Umbrella ☔️, It's going to rain. ",
       from_='twilionum',
       to='personalnum'
   )
   print(message.status)
