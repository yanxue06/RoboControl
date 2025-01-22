import socket 
import json 
import math 
import uuid
import time 

ROBOT_IP = "192.168.9.201"

# status 

def get_status(): 
    PORT = 19204

    try:
        s = socket.socket()
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # Send the get-status command
        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xE8\x00\x00\x00\x00\x00\x00")
        print("sent message")

        response = s.recv(4096)
        json_bytes = response[16:] 
        json_str = json_bytes.decode("utf-8", errors="ignore")
        
        print(json_str)
        
        s.close()

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

def charge(): 
    PORT = 19206 #port of navigation APIs 
    try: 
        s = socket.socket() #creating a socket object to communicate with robot from client

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to robot at {ROBOT_IP}:{PORT}") 

        # NOW, go to chargin port 
        data = {
            # "source_id": "SELF_POSITION",
            "id": "CP3",
            "max_speed": 0.3,
            "max_wspeed": 0.3,
            "max_wacc": 0.2,
            "task_id": "12345"
        }
        
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
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

        # NOW, go to chargin port 
        data = {
            "source_id": "SELF_POSITION",
            "id": site,
            "max_speed": 0.3,
            "max_wspeed": 0.3,
            "max_wacc": 0.2,
            "task_id": "12345"
        }
        
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
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

        s.close() 

    except Exception as e: 
        print(f"Error: {e}")

def dNav(stations): 
    # body in as a dictionary (flask did json to arry of dictionary conversion for me)

    try: 
        PORT = 19206

        s = socket.socket() 
        print("created socket")

        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")
        
        move_task_list = [] 
        print("Type of stations:", type(stations))
        print(stations)


        for i, station in enumerate(stations): #according to the doc, then i have to start at an actual site 
            print("Stations:", stations)
            if i == 0: 
                to_site(station["id"])
            if i>0: 
                move_task_list.append({"id": station["id"], "source_id": stations[i-1]["id"], "task_id": str(uuid.uuid4())[:8] }) 

        payload_dict = {"move_task_list": move_task_list}
        payload_bytes = json.dumps(payload_dict, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)

        print("Payload:", payload_bytes.decode('utf-8'))  # Debug: Print the JSON being sent

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xFA\x00\x00\x00\x00\x00\x00") 
        header_array[7] = length_byte     # set the 8th byte to the actual length, can only do this with an array

        message = bytes(header_array) + payload_bytes

        # QUERIES WHETHER THE ROBOT HAS MOVED TO THE STARTING POINT
        while (True): 
            status = getNavStatus()
            if status == 4: 
                break
            else: 
                print(f"current status: {status}")
            # add a delay so my calls arent too often 
            time.sleep(0.8)

        # DO NOT SEND THE NEW MESSAGE UNTIL THE ROBOT HAS MOVED TO THE STARTING POINT 
        s.send(message)

        print("sent message")

        response = s.recv(1024) 

        json_bytes = response[16:] 
        print(json_bytes.decode("utf-8", errors="ignore"))

        s.close() 

    except Exception as e: 
        print(f"error {e}")

def getNavStatus(): 
    PORT = 19204 

    s = socket.socket() 
    s.connect(ROBOT_IP, PORT)

    s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xFC\x00\x00\x00\x00\x00\x00")

    response = s.recv(1024) 

    response = json.load(response)

    return response["task_status"]

     

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