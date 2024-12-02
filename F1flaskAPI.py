from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Route: Home
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "round": "R24.ABU DHABI",
        "date":"06-08",
        "month":"DEC",
        "flag":"🇦🇪",
        "fp1time":"03:00 PM",
        "fp2time":"06:30 PM",
        "fp3time":"04:00 PM",
        "q1time":"07:30 PM",
        "racetime":"06:30 PM",
        "imglink":"https://media.formula1.com/image/upload/f_auto,c_limit,w_1440,q_auto/f_auto/q_auto/content/dam/fom-website/2018-redesign-assets/Track%20icons%204x3/Abu%20Dhab%20carbon"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port="10000")
