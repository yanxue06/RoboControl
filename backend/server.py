from flask import Flask, jsonify, request #eventually want ot make it so user can manually enter and it gets passed into functions
from flask_cors import CORS
import commands
import json

# source env/bin/activate
 
app = Flask(__name__)

# Load the .smap file !! 

SMAP_FILE = "./maps/warehouse.smap"

CORS(app) #ensure correct port is requested 


# note that request.get_json() gets the body in which was sent to it 
# during the POST request 


@app.route('/map', methods=['GET'])
def get_map():
    try:
        with open(SMAP_FILE, "r") as f:
            smap_data = json.load(f)  # Parse the file's content as JSON
        return jsonify(smap_data)  # Send it as a JSON response
    except FileNotFoundError:
        return jsonify({"error": "SMAP file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in SMAP file"}), 400 

@app.route('/status', methods=['GET']) #useful to tell us what map is currently in use 
def status(): 
    print("Status endpoint hit") 

    commands.get_status()
    return jsonify({"message": "Got status successfully"})

@app.route('/location', methods=['GET']) #useful to tell us what map is currently in use 
def location():
    json_str = commands.get_location()
    if not json_str:
        return jsonify({"error": "Could not get location"}), 500
    
    # Convert that string to an actual Python dict so we can return real JSON
    try:
        loc_dict = json.loads(json_str)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON from robot"}), 500
    
    return jsonify(loc_dict)

@app.route('/battery', methods=['GET']) #useful to tell us what map is currently in use 
def battery(): 
    print("Status endpoint hit") 

    commands.get_battery()
    return jsonify({"message": "Got battery successfully"})

@app.route('/charge', methods=['POST']) 
def charge(): 
    commands.charge() 
    return jsonify({"message": "charging command called"})

@app.route('/relocate', methods=['POST']) #might need a map 
def relocate(): 
    print("Status endpoint hit")
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    commands.relocate(x, y)
    return jsonify({"message": "relocate command sent"})

@app.route('/soundPlay', methods=['POST']) 
def soundPlay(): 
    print("Status endpoint hit")

    commands.soundPlay()
    return jsonify({"message": "sound command sent"})

@app.route('/soundPause', methods=['POST']) 
def soundPause(): 
    print("Status endpoint hit")

    commands.soundPause()
    return jsonify({"message": "sound command sent"})

# NAVIGATION !! 

@app.route('/dNav', methods = ['POST'])  #dNav is an endpoint, and it is a post method 
def dNav(): 
    # get json payload from body of post request
    data = request.get_json() 
    print(f"data: {data}")
    commands.dNav(data) 

    return jsonify({"message": "dNav command sent"})

@app.route('/getNavStatus', methods = ["GET"])
def NavStatus(): 
    print("get nav status")
    commands.getNavStatus() 

    return jsonify({"message": "sent nav status message"})

@app.route('/getTaskStatus', methods = ["GET"])
def TaskStatus():
    print("status endpoint hit")
    commands.getTaskStatus() 

    return jsonify({"message": "sound command sent"})

@app.route('/forward', methods=['POST'])
def forward(): 
    print("Status endpoint hit")

    commands.move_forward(request.get_json().get('distance')) #this inside should be the user sent data 
    
    return jsonify({"message": "forward command sent"})

@app.route('/backward', methods=['POST'])
def backward(): 
    print("Status endpoint hit")

    commands.move_backward(request.get_json().get('distance'))
    
    return jsonify({"message": "backward command sent"})

@app.route('/rotateLeft', methods=['POST'])
def rotate_left(): 
    print("Status endpoint hit")

    commands.rotate_left(request.get_json().get('angle'))

    return jsonify({"message": "backward command sent"})

@app.route('/rotateRight', methods=['POST'])
def rotate_right(): 
    print("Status endpoint hit")

    commands.rotate_right(request.get_json().get('angle'))

    return jsonify({"message": "Right  command sent"})


if __name__ == '__main__':
    app.run(debug=True, port=5001) #or any port other than one already used