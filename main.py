import phonenumbers
import opencage
import folium
from my_phone import number

from phonenumbers import geocoder

k_number=phonenumbers.parse(number)
location=geocoder.description_for_number(k_number, "en")
print(location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

api_key="14c194deba51452882ffa87ae3a37c79"

geocoder=OpenCageGeocode(api_key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat=results[0]["geometry"]["lat"]
lng=results[0]["geometry"]["lng"]

print(lat,lng)

my_map=folium.Map(location=[lat, lng],zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

my_map.save("mylocation.html")
