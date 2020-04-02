
import urllib.request
import json
import pprint

APIKEY = 'YOUR_OWN_APIKEY'
city = 'Wellesley'
country_code = 'us'
#url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
url = f'http://api.openweathermap.org/data/2.5/weather?q=Wellesley,us&APPID=5272dec9cc9693dd8ad00386f1e9b430'
# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?
print(response_data['main']['temp'])