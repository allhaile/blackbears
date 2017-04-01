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
	lat=122.4148,
	lng=37.7599,
	markers=[(122.4148, 37.7599)]
	),
	{
	'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
	'lat': 122.4148,
	'lng': 37.7599,
	'infobox': "<b>Hello World from other place</b>"
	}
	return render_template('test.html', mymap=mymap)

if __name__ == "__main__":
    app.run()