from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
# from geolocation.main import GoogleMaps
from flask_googlemaps import Map
# from flask.ext.googlemaps import GoogleMaps
from geopy.geocoders import Nominatim
app = Flask(__name__, template_folder=".")
# app.config['GOOGLEMAPS_KEY'] = "AIzaSyCMxYp4233mPYNzrEdBW2FUr_wUnDPhBkw"
GoogleMaps(app, key="AIzaSyCMxYp4233mPYNzrEdBW2FUr_wUnDPhBkw")


# app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"

# GoogleMaps(app)

@app.route("/")
def mapview():
	
	geolocator = Nominatim()
	location = geolocator.geocode("1839 Euclid Ave Berkeley CA")
	mylat, mylng = location.latitude, location.longitude
	print("My lat is: " + str(mylat))
	print("My lng is: " + str(mylng))

	# google_maps = googlemaps.Client(key='AIzaSyBVrDBqpFutaI79007lafIzKXc4qcrszvdZ7w') Geocode API key
	# google_maps = GoogleMaps('8JZ7i18MjFuM35dJHq70n3Hx4') 

	# address = "New York City Wall Street 12"
# location = google_maps.search(location=address) # sends search to Google Maps.
# my_location = google_maps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# mylat, mylng = google_maps.address_to_latlng(address)


# print(my_location.city)
# print(my_location.route)
# print(my_location.street_number)
# print(my_location.postal_code)

# for administrative_area in my_location.administrative_area:
#     print("{}: {} ({})".format(administrative_area.area_type, 
#                                administrative_area.name, 
#                                administrative_area.short_name))

# print(my_location.country)
# print(my_location.country_shortcut)

# print(my_location.formatted_address)

# print(my_location.lat)
# print(my_location.lng)


# my_location = google_maps.search(lat=lat, lng=lng).first()
#{{googlemap("my_awesome_map", lat=37.871853, lng=-122.258423, markers=[(37.871853, -122.258423)], zoom=17)}}

# creating a map in the view
	mymap = Map(
	    identifier="view-side",  # for DOM element
	    varname="mymap",  # for JS object name
	    lat=mylat,
	    lng=mylng,
	    markers=[(mylat, mylng)]
	)
	# mymap=my_location
	return render_template('test.html', lat=mylat, lng=mylng, mymap=mymap)

if __name__ == "__main__":
    app.run()
