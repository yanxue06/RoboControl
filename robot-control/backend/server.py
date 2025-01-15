from flask import Flask, jsonify
from flask_cors import CORS
import commands

app = Flask(__name__)

CORS(app) #ensure correct port is requested 

@app.route('/status', methods=['GET'])
def status(): 
    print("Status endpoint hit") 

    commands.get_status()
    return jsonify({"message": "Got status successfully"})


@app.route('/navigate', methods=['POST'])
def navigate(): 
    print("Status endpoint hit")

    commands.navigate()
    return jsonify({"message": "Navigate command sent"})


if __name__ == '__main__':
    app.run(debug=True, port=5001) #or any port other than one already used