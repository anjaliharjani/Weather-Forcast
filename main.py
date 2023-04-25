import requests
from twilio.rest import Client

account_sid = "ACe4e0fef1d8ee72a420c7bf1b1588f4e5"
auth_token = "072a32d7b33f275b92db8867bd004721"
parameters = {
    "lat":25.321377,
    "lon":74.586952,
    "appid":"4032df154007844f63c1fa17f9b67b62",
    "exclude":"current,minutely,daily",
}
response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
it_will_rain = False
for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 810:
        it_will_rain = True
if it_will_rain:
    print("b")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today.Remember to bring an ☂️.",
        from_='+17706290966',
        to='+917691828194'
    )
    print(message.status)