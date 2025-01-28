import socket # key to communicate with the robot 
import json # for converting between JSON and Python Dictionaries 
import math # converting degrees to radians (which the robot uses for angles)
import uuid # for random id generation - useful when assigning task id 
import time # for adding delays to avoid overly frequent requests 

ROBOT_IP = "192.168.9.201"

''' 
Note

The robot can only receive hexidecimal, so we always convert messages from 
JSON to Hexidicemial prior to sending messages 

All functions follow the same general structure 
1. create a connection between client socket and robot port 
2. get the message we want to send to the robot in JSON
3. edit the 8th bit of the header array to match the length of message 
4. send messages and print out the response (for debugging)

For GET functions, since there is no message, all that is required to be sent 
is the header array 

To be more clear, I labeled what each line does for the get_status() 
function below - all the GET request calls follow this similar format

Some of the post requests like dNav are a tiny bit more complicated, but I 
will be sure to document them with comments such that they are less 
confusing 

I fully labeled **the charge function** as a representation of what most of the
POST functions look like. 

In addition, I also labeled the dNav function as it might be a bit confusing 
'''
# Status 

def get_status(): 
    PORT = 19204
    try:
        # creating a socket on the client 
        s = socket.socket()
        
        # connecting that socket to the robot's IP and Port (lets you use a specific API)
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # Send the get-status command
        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xE8\x00\x00\x00\x00\x00\x00")
        print("sent message")

        response = s.recv(4096) # recieving a 4096 bytes message 
        json_bytes = response[16:] # we only need after the 16th byte  
        json_str = json_bytes.decode("utf-8", errors="ignore") # decode the response into a format we can read
        
        print(json_str) # print that decoded messages
        
        s.close() #close the socket 

    except Exception as e:
        print(f"Error: {e}")
        return None


    
def get_location(): 
    try: 
        PORT = 19204
        
        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xEC\x00\x00\x00\x00\x00\x00")
       
        response = s.recv(1024)
        json_bytes = response[16:]  # skip the 16-byte header

        json_str = json_bytes.decode("utf-8", errors="ignore")  
        print("Decoded JSON snippet:", json_str)

        s.close() 

        response = json_str 
        return response 
    
    except Exception as e: 
        print(f"Error: {e}")    

def get_battery(): 
    try: 
        PORT = 19204
        
        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xEF\x00\x00\x00\x00\x00\x00")
       
        response = s.recv(1024)
        print(f"response: {response}")

        s.close() 

    except Exception as e: 
        print(f"Error: {e}")    

def charge():  # FIRST POST REQUEST !! 

    PORT = 19206 #port of navigation APIs 
    try: 
        s = socket.socket() #creating a socket object to communicate with robot from client

        s.connect((ROBOT_IP, PORT)) # connecting to robot 
        print(f"Connected to robot at {ROBOT_IP}:{PORT}") 

        # data in json format 
        data = { 
            # "source_id": "SELF_POSITION",
            "id": "CP3",
            "max_speed": 0.3,
            "max_wspeed": 0.3,
            "max_wacc": 0.2,
            "task_id":  str(uuid.uuid4())[:8]
        }
        
        # JSON.dumps first converted JSON to a Python Dictionary,
        # then encoding it into 
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')

        # we need the length of our data so that we can manipulate the header 
        # is our message to reflect that 
        length_byte = len(payload_bytes)

        # Convert the header into a mutable bytearray
        header_array = bytearray(b'\x5A\x01\x00\x01\x00\x00\x00\x1C\x0B\xEB\x00\x00\x00\x00\x00\x00') 
        header_array[7] = length_byte   # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        response = s.recv(1024)
        print(f"response: {response}")

        # Parse the response header and payload
        header = response[:16]  # First 16 bytes are the header
        payload = response[16:]  # Remaining bytes are the JSON payload
        print(f"Response header: {header}")
        print(f"Response payload: {payload.decode('utf-8')}")

    except Exception as e: 
        print(f"Error: {e}")


# Control 

def relocate(x,  y): 
    PORT = 19205
    
    try: 
        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        data = {
            "x": x,
            "y": y,
            "angle": 0.0,
            "length": 1.0,
            "home": False
        }

        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)

        # Convert the header into a mutable bytearray
        header_array = bytearray(b'\x5A\x01\x00\x01\x00\x00\x00\x1C\x07\xD2\x00\x00\x00\x00\x00\x00') 
        header_array[7] = length_byte   # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        response = s.recv(1024)
        print(f"response: {response}")

        # Parse the response header and payload
        header = response[:16]  # First 16 bytes are the header
        payload = response[16:]  # Remaining bytes are the JSON payload


        print(f"Response header: {header}")
        print(f"Response payload: {payload.decode('utf-8')}")

    except Exception as e: 
        print(f"Error: {e}")   

def soundPlay(): 
    #other API port: 19210...
    try: 
        PORT = 19210

        s = socket.socket()
        print("succesfully created Socket")

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")
        
        data = {"name":"collision","loop":False}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)

        # Convert the header into a mutable bytearray
        header_array = bytearray(b'\x5A\x01\x00\x01\x00\x00\x00\x20\x17\x70\x00\x00\x00\x00\x00\x00') 
        header_array[7] = length_byte   # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        print("send message")
        #try to receive the message
        response = s.recv(1024)
        print(response)

        s.close() 

        return response
    except Exception as e: 
        print(f"Error: {e}")


def soundPause(): 
    #other API port: 19210...
    try: 
        PORT = 19210

        s = socket.socket()
        print("succesfully created Socket")

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")
        
        data = {"name":"collision","loop":False}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)

        # Convert the header into a mutable bytearray
        header_array = bytearray(b'\x5A\x01\x00\x01\x00\x00\x00\x00\x17\x7A\x00\x00\x00\x00\x00\x00') 
        header_array[7] = length_byte   # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        print("send message")
        #try to receive the message
        response = s.recv(1024)
        print(response)

        s.close() 

        return response
    except Exception as e: 
        print(f"Error: {e}")

# Navigation

def to_site(site): 
    PORT = 19206 #port of navigation APIs 
    try: 
        s = socket.socket() #creating a socket object to communicate with robot from client

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to robot at {ROBOT_IP}:{PORT}") 

        # NOW, whatever site was passed in 
        data = {
            "source_id": "SELF_POSITION",
            "id": site,
            "max_speed": 0.3,
            "max_wspeed": 0.3,
            "max_wacc": 0.2,
            "task_id":  str(uuid.uuid4())[:8]
        }
        
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)

        # Convert the header into a mutable bytearray
        header_array = bytearray(b'\x5A\x01\x00\x01\x00\x00\x00\x1C\x0B\xEB\x00\x00\x00\x00\x00\x00') 
        header_array[7] = length_byte   # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        response = s.recv(1024)

        s.close() 

        print(f"response: {response}")

        # Parse the response header and payload
        header = response[:16]  # First 16 bytes are the header
        payload = response[16:]  # Remaining bytes are the JSON payload
        print(f"to_site9) response header: {header}")
        print(f"to_site() payload: {payload.decode('utf-8', errors="ignore")}")

    except Exception as e: 
        print(f"Error: {e}")

def dNav(stations): 
    # stations comes in as a python dictionary (flask did json to arry of dictionary conversion for already) 

    # The original problem I had while making this function was that the Robot requires that you
    # are at your starting station before completing a chain of destinations 
    # therefore, I created a to_site() function which make the robot first go to the first 
    # destination the user inputs, and then complete the rest of the destinations 

    try: 
        PORT = 19206

        s = socket.socket() 
        print("created socket")

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")
        
        move_task_list = [] 
        print("Type of stations:", type(stations)) # Python lists 
        print(stations) #prints all the statiosn 


        for i, station in enumerate(stations): 
            #according to the doc,  i have to start at an actual site 
            print("Stations:", stations)
            if i == 0:  # if we are not yet at our first station, lets go to our first station with to_site()
                to_site(station["id"]) 
            if i>0:  # we are just adding the stations into an array, NOT calling any movement functions yet 
                # consider at i=1, stations[i-1] should have been the first station here,
                # which we have / are moving to because we call to_site() 
                move_task_list.append({"id": station["id"], "source_id": stations[i-1]["id"], "task_id": str(uuid.uuid4())[:8] }) 

        # converting to a dictionary of arrays (as required by the API documentation)
        payload_dict = {"move_task_list": move_task_list}
        # converting dictionary to JSON
        payload_bytes = json.dumps(payload_dict, separators=(',', ':')).encode('utf-8')
        # calculating length 
        length_byte = len(payload_bytes)

        print("pre-send payload:", payload_bytes.decode('utf-8'))  # Debug: Print the JSON being sent

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xFA\x00\x00\x00\x00\x00\x00") 
        # set the 8th byte to the actual length, can only do this with an array
        header_array[7] = length_byte     
        
        # concatante to create a message that can be sent to the robot 
        message = bytes(header_array) + payload_bytes

        # QUERIES WHETHER THE ROBOT HAS MOVED TO THE STARTING POINT
        # this is necessary because to go through the rest of the navigation, the robot 
        # must have first moved to the first location
        # ex. if it was (LM1, LM2, CP3), we need to make sure our to_site() call has effetively 
        # gotten our robot to LM1 first

        while True: 
            try:
                status = getNavStatus()  # gets the status of our navigation 
                print(f"status type: {type(status)}") # DEBUGGING 

                # Safely access "task_status"
                task_status = status.get("task_status")
                print(f"Task Status: {task_status}")

                if task_status == 4: # 4 means that the robot has succesfully moved 
                    break
                else:
                    print(f"Current status: {status}")

                # Add a delay to make sure we do not repeatedly call getNavStatus, since we can't have 
                # too frequent calls 
                time.sleep(0.8)  

            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
            except Exception as e:
                print(f"Unexpected Error: {e}")


        # DO NOT SEND THE NEW MESSAGE UNTIL THE ROBOT HAS MOVED TO THE STARTING POINT 
        s.send(message)

        # at this point, the robot should finally start doing its origin requested path 

        print("sent message")

        response = s.recv(1024) 

        json_bytes = response[16:] 
        print(json_bytes.decode("utf-8", errors="ignore"))

        s.close() 

    except Exception as e: 
        print(f"error {e}")

def getNavStatus(): 

    PORT = 19204 
    try: 
        s = socket.socket() 
        s.connect((ROBOT_IP, PORT))  # note the tuple (ROBOT_IP, PORT)

        # Send whatever query you need:
        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xFC\x00\x00\x00\x00\x00\x00")
        
        response_bytes = s.recv(1024)
        s.close()

        # Separate header (16 bytes) from payload
        payload = response_bytes[16:]      # JSON portion
        
        print(f"payload type {type(payload)}") 
        
        payload_dict = None 

        try:
            payload_dict = json.loads(payload)  # Ensure valid JSON
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            return json.dumps({"error": "Invalid JSON"})

        print(f"current status {payload_dict.get("task_status")}")
        return payload_dict
    
    except Exception as e: 
        print(f"error {e}")

def getTaskStatus(): 
    try: 
        PORT = 19204
        
        s = socket.socket()
        s.connect((ROBOT_IP, PORT))

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x04\x56\x00\x00\x00\x00\x00\x00")

        response = s.recv(1024) 
        print(f"response: {response}")
    except Exception as e: 

        print(f"error while getting status: {e}")

def move_forward(distance): 
    try: 
        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # // move straight for 5m
        # 5A 01 00 01 00 00 00 1E 0B EF 00 00 00 00 00 00 
        # 7B 22 64 69 73 74 22 3A 35 2E 30 2C 22 76 78 22 
        # 3A 30 2E 35 2C 22 76 79 22 3A 30 2E 35 7D

        data = {"dist": distance, "vx": 1.5, "vy": 0}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)  # e.g. 28

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00") 
        header_array[7] = length_byte     # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes
        s.send(message)

        
        print(f"sent message to move {distance} meters")
        # b"": Indicates a byte string (raw binary data).
        # \x: Specifies a single byte in hexadecimal format.
        # last few zeroes are reserved area
        # 03 E8 is for the API number / message type (1000 is 0x03E8) 
        # see "API introduction for what these mean"

        #try to receive the message
        response = s.recv(1024)
        print(response)

        s.close() 

        return response

    except Exception as e: 
        print(f"Error: {e}")
    
def move_backward(distance): 
    try: 
        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # // move straight for 5m
        # 5A 01 00 01 00 00 00 1E 0B EF 00 00 00 00 00 00 
        # 7B 22 64 69 73 74 22 3A 35 2E 30 2C 22 76 78 22 
        # 3A 30 2E 35 2C 22 76 79 22 3A 30 2E 35 7D

        data = {"dist": distance, "vx": -1.5, "vy": 0}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)  # e.g. 28

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00")
        header_array[7] = length_byte     # set the 8th byte to the actual length

        message = bytes(header_array) + payload_bytes
        s.send(message)

        
        print(f"sent message to move {distance} meters")

        # b"": Indicates a byte string (raw binary data).
        # \x: Specifies a single byte in hexadecimal format.
        # last few zeroes are reserved area
        # 03 E8 is for the API number / message type (1000 is 0x03E8) 
        # see "API introduction for what these mean"

        #try to receive the message
        response = s.recv(1024)
        print(response)

        s.close() 

        return response

    except Exception as e: 
        print(f"Error: {e}")

def rotate_left(angle): 
    try: 

        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # {"angle":3.14,"vw":1.6}
        # // rotate 3.14 rad with rotation speed 1.6rad/s
        # 5A 01 00 01 00 00 00 17 0B F0 00 00 00 00 00 00 
        # 7B 22 61 6E 67 6C 65 22 3A 33 2E 31 34 2C 22 76 
        # 77 22 3A 31 2E 36 7D

        data = {"angle": math.radians(angle), "vw": 1.5}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)  # e.g. 28

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x17\x0B\xF0\x00\x00\x00\x00\x00\x00")
        header_array[7] = length_byte    # set the 8th byte to the actual length

        message = bytes(header_array) + payload_bytes
        s.send(message)

        
        print(f"sent message to move {angle} degrees")

        # b"": Indicates a byte string (raw binary data).
        # \x: Specifies a single byte in hexadecimal format.
        # last few zeroes are reserved area
        # 03 E8 is for the API number / message type (1000 is 0x03E8) 
        # see "API introduction for what these mean"

        #try to receive the message
        response = s.recv(1024)
        print(response)

        s.close() 

        return response
     
    except Exception as e: 
        print(f"Error: {e}")


def rotate_right(angle): 
    try: 

        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # {"angle":3.14,"vw":1.6}
        # // rotate 3.14 rad with rotation speed 1.6rad/s
        # 5A 01 00 01 00 00 00 17 0B F0 00 00 00 00 00 00 
        # 7B 22 61 6E 67 6C 65 22 3A 33 2E 31 34 2C 22 76 
        # 77 22 3A 31 2E 36 7D

        data = {"angle": math.radians(angle), "vw": -1.5}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)  # e.g. 28

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x17\x0B\xF0\x00\x00\x00\x00\x00\x00")
        header_array[7] = length_byte    # set the 8th byte to the actual length

        message = bytes(header_array) + payload_bytes
        s.send(message)

        
        print(f"sent message to move {angle} degrees")

        # b"": Indicates a byte string (raw binary data).
        # \x: Specifies a single byte in hexadecimal format.
        # last few zeroes are reserved area
        # 03 E8 is for the API number / message type (1000 is 0x03E8) 
        # see "API introduction for what these mean"

        #try to receive the message
        response = s.recv(1024) #max 1024 bytes 
        print(response)

        s.close() 

        return response
     
    except Exception as e: 
        print(f"Error: {e}")