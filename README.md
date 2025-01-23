### Robot Control System

## Overview

The Robot Control System is a prototype web application designed to interface with SEER Robotics warehouse robots. This application enables users to monitor the robot's status, issue control commands, and navigate the robot in a simulated warehouse environment. The system is built using a React front-end with Vite, a Flask backend, and Python socket programming to communicate with the robot's API. The robot's IP address is configurable and may differ depending on the deployment environment.

This project demonstrates the potential to optimize warehouse operations, increasing efficiency for robotic systems in logistics and inventory management.

## Features

1. Status Monitoring

Get General Info: Retrieve basic information about the robot.

Get Location: Display the robot's current location.

Get Battery: Monitor the robot's battery status.

2. Control Commands

Charge Robot: Initiate charging for the robot.

Manual Relocate: Relocate the robot to specific coordinates (x, y).

Play Sound / Pause Sound: Control the robot's audio output.

3. Navigation

Bot Navigation: Manage the robot's navigation through predefined landmarks.

Move Forwards / Backwards: Move the robot a specified distance.

Rotate Left / Right: Rotate the robot by a specified angle.

4. Display Console

A built-in console dynamically displays:

Status codes.

API responses.

Error messages.

Tech Stack

Frontend

React with Vite: User interface for interacting with the robot.

Backend

Flask: REST API backend for handling commands and routing.

Python Socket Programming: Communication with the robot's API.

Robot API Integration

Extensive work with the robot's API to implement commands like move, relocate, and play sound.

Parsing API responses to extract useful information, such as current_map and battery status.

Dependencies

Below is a complete list of dependencies for the project:

Python Dependencies

Flask: For building the REST API.

Flask-SocketIO: For enabling real-time WebSocket communication (if required).

subprocess: For managing terminal commands.

socket: For low-level socket communication with the robot.

json: For parsing API responses.

JavaScript (React with Vite) Dependencies

Dependencies

@emotion/react: For styling React components.

@emotion/styled: For creating styled components.

@mui/material: For Material UI components.

react: For building the user interface.

react-dom: For rendering the UI.

uuid: For generating unique IDs.

DevDependencies

@eslint/js: For linting JavaScript.

@types/react: For React type definitions.

@types/react-dom: For React DOM type definitions.

@vitejs/plugin-react-swc: For optimized React integration with Vite.

eslint: For identifying and reporting code issues.

eslint-plugin-react: For React-specific linting rules.

eslint-plugin-react-hooks: For linting React hooks.

eslint-plugin-react-refresh: For React fast refresh support.

globals: For defining global variables in linting.

vite: For building and running the React application.

Ensure all dependencies are installed by running:

npm install

How It Works

Frontend (React with Vite):

Provides a user-friendly interface with buttons and fields for robot control.

Displays logs and API responses dynamically in the "Display Console" area.

Backend (Flask):

Handles API requests from the React front-end.

Translates commands into socket communications for the robot.

Socket Communication:

Connects to the robot on a configurable port (default: 19204).

Sends commands in binary format (e.g., \x5A\x01\x00\x01...).

Receives and processes robot responses (JSON embedded in binary payloads).

Console Display:

Logs API calls, status codes, and responses in real-time on the web app.

How to Run

1. Backend

Install dependencies:

pip install flask flask-socketio

Run the Flask server:

python app.py

2. Frontend

Navigate to the React project directory.

Install dependencies:

npm install

Start the React app:

npm run dev

3. Robot Connection

Ensure the SEER Robotics robot is connected and accessible at the specified IP and port.

Test connection by triggering commands (e.g., Get Battery).

Contribution

If you would like to contribute:

Fork the repository.

Create a new branch for your feature or bug fix.

Submit a pull request with a detailed description of your changes.

Acknowledgments

Robot API Documentation: Provided essential guidance for integrating commands.

