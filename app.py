from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder=".")
GoogleMaps(app)
app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"


@app.route("/")
def mapview():
# creating a map in the view
	mymap = Map(
	identifier="view-side",
	lat=50,
	lng=50,
	markers=[(50, 50)]
	)
	sndmap = Map(
	identifier="sndmap",
	lat=37.4419,
	lng=-122.1419,
	zoom=12,
    cluster=True,
	markers=[
	{
	'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
	'lat': 300.4657,
	'lng': 456.1419,
	'infobox': "<b>Hello World</b>"
	},
	{
	'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
	'lat': 37.4300,
	'lng': -122.1400,
	'infobox': "<b>Hello World from other place</b>"
	}
	]
	)
	return render_template('test.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run()