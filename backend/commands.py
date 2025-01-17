import socket 
import json 
import math 

ROBOT_IP = "192.168.9.201"

def get_status(): 
    try: 
        PORT = 19204

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        #message to send: "5A 01 00 01 00 00 00 00 03 E8 00 00 00 00 00 00"
        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xE8\x00\x00\x00\x00\x00\x00")
        print("sent message")
        # b"": Indicates a byte string (raw binary data).
        # \x: Specifies a single byte in hexadecimal format.
        # last few zeroes are reserved area
        # 03 E8 is for the API number / message type (1000 is 0x03E8) 
        # see "API introduction for what these mean"

        #try to receive the message
        response = s.recv(1024)
        s.close() 

        return response 

    except Exception as e: 
        print(f"Error: {e}")

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
        print(f"response: {response}")

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