import requests, json 
import googlemaps 

api_key = 'ppAIzaSyCcaDoTeMKK7wxl1bF8mr-EvbSFSXReO6E'
source = input() 
dest = input() 
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

r = requests.get(url + 'origins = ' + source + '&destinations = ' + dest + '&key = ' + api_key) 
                     

x = r.json() 
  
print(x) 

    