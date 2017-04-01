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

@app.route("/map")
def mapview():
	
	geolocator = Nominatim()
	location = geolocator.geocode("1839 Euclid Ave Berkeley CA")
	mylat, mylng = location.latitude, location.longitude
	mymap = Map(
	    identifier="view-side",  # for DOM element
	    varname="mymap",  # for JS object name
	    lat=mylat,
	    lng=mylng,
	    markers=[(mylat, mylng)]
	)

	# mymap=my_location
	return render_template('test.html', lat=mylat, lng=mylng, mymap=mymap)
	# return location_page

if __name__ == "__main__":
    app.run()
