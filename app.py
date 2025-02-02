from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store the last known location
user_location = {"latitude": None, "longitude": None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track_location', methods=['POST'])
def track_location():
    global user_location
    data = request.get_json()
    user_location["latitude"] = data["latitude"]
    user_location["longitude"] = data["longitude"]
    return jsonify({"message": "Location received", "latitude": user_location["latitude"], "longitude": user_location["longitude"]})

if __name__ == '__main__':
    app.run(debug=True)
