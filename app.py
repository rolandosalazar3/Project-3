from flask import Flask, render_template, jsonify
import pandas
import json

app = Flask(__name__)

@app.route("/")
def index():
    team_list = ["Jumpers", "Dunkers", "Dribblers", "Passers"]
    return render_template("index.html", list=team_list)

@app.route("/api/v1.0/data")
def source_data():
    df=pandas.read_csv ("university_data.csv")
    data = {x: df[x].tolist() for x in df.columns}
    return jsonify(data)


@app.route("/api/v1.0/lat_long")
def lat_long():
    df=pandas.read_csv ("university_data.csv")
    data = {
      'lat': df["latitude"].tolist(),
      'long': df["longitude"].tolist(),
      'another_col': ['data_here']
    }
    return jsonify(data)


    

if __name__ == "__main__":
    app.run(debug=True)
    