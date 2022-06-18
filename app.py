import errno

import geopy
from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = "manbearbird_MAMUDU"


@app.route("/")
def index():
    flash("Enter Geo Location Coordinates")
    return render_template("index.html")


@app.route("/get_postal_code", methods=['POST', 'GET'])
def get_postal_code():
    try:
        coordinates = (float(request.form['latitude']), float(
            request.form['longitude']))
    except:
        return render_template("index.html", error="Enter Valid Geo Coordinates")
    try:
        postcode = find_postcode(coordinates)
    except:
        return render_template("index.html", error="There's a problem with this geo coordinates")
    return render_template("index.html", postcode=postcode, coordinates=coordinates)


def find_postcode(coordinates):
    geolocator = geopy.Nominatim(user_agent='flask-geocoder')
    address = geolocator.reverse(coordinates)
    postcode = address.raw['address']['postcode']
    return postcode
