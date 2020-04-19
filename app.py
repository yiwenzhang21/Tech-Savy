from flask import Flask, render_template, request, redirect, url_for

from mbta_finder import get_json, get_lat_long, get_nearest_station, find_stop_near

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        place = request.form["b"]
        if place == "":
            return render_template("index.html")

        station_name,wheelchair_boarding = find_stop_near(place)
        
        if station_name != "False":    
            return redirect(url_for("result", sn=station_name, wb=wheelchair_boarding))
        else:
            return redirect(url_for("error"))

    return render_template("index.html")


@app.route("/error/")
def error():
    return render_template("error.html") 

@app.route("/results/<sn><wb>")
def result(sn, wb):
    return render_template(
             "mbta_station.html", station_name=sn, wheelchair_boarding=wb
                 )

if __name__ == '__main__':
    app.run(debug=True)
