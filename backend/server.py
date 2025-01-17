from flask import Flask, jsonify, request #eventually want ot make it so user can manually enter and it gets passed into functions
from flask_cors import CORS
import commands

app = Flask(__name__)

CORS(app) #ensure correct port is requested 

@app.route('/status', methods=['GET']) #useful to tell us what map is currently in use 
def status(): 
    print("Status endpoint hit") 

    commands.get_status()
    return jsonify({"message": "Got status successfully"})

@app.route('/location', methods=['GET']) #useful to tell us what map is currently in use 
def location(): 
    print("Status endpoint hit") 

    commands.get_location()
    return jsonify({"message": "Got location successfully"})

@app.route('/battery', methods=['GET']) #useful to tell us what map is currently in use 
def battery(): 
    print("Status endpoint hit") 

    commands.get_battery()
    return jsonify({"message": "Got battery successfully"})

@app.route('/navigate', methods=['POST']) #might need a map 
def navigate(): 
    print("Status endpoint hit")

    commands.relocate()
    return jsonify({"message": "Navigate command sent"})


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

    return jsonify({"message": "Right command sent"})


if __name__ == '__main__':
    app.run(debug=True, port=5001) #or any port other than one already used