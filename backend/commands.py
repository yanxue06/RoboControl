import socket 
import json 

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

def navigate(): 
    try: 
        PORT = 19205
        
        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        # dictionary
        # data = { 
        #     "x":10.0,   
        #     "y":3.0,
        #     "angle":0
        # }
        # should directly be able to steralize this data 

        #try to do manual entering later... 
        s.send(
            b"\x5A\x01\x00\x01\x00\x00\x00\x1C\x07\xD2\x00\x00\x00\x00\x00\x00"
            b"\x7B\x22\x78\x22\x3A\x31\x30\x2E\x30\x2C\x22\x79\x22\x3A\x33\x2E\x30"
            b"\x2C\x22\x61\x6E\x67\x6C\x65\x22\x3A\x30\x7D"
        )
        
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

        data = {"dist": distance, "vx": 0.5, "vy": 0}
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
    
def move_backward(): 
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

        data = {"dist": 5.0, "vx": -0.5, "vy": 0}
        payload_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
        length_byte = len(payload_bytes)  # e.g. 28

        # Convert the header into a mutable bytearray
        header_array = bytearray(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00")
        header_array[7] = length_byte     # set the 8th byte to the actual length

        message = bytes(header_array) + payload_bytes
        s.send(message)

        
        print("sent message")
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


