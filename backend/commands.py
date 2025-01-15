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
        response_data = response.hex()

        s.close() 

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

def move_forward(): 
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

        # header
        header = b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00"

        # JSON Data, can now edit these parameters freely and the translation range will also change 
        data = {"dist": 3.0, "vx": 0.5, "vy": 0} 
        
        # encoding data so robot can read 
        payload = json.dumps(data).encode('utf-8')

        # concatenating to make the full message
        message = header + payload 
       
        s.send(message)
        
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
    
def move_backward(): 
    try: 
        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00\x7B\x22\x64\x69\x73\x74\x22\x3A\x35\x2E\x30\x2C\x22\x76\x78\x22\x3A\x30\x2E\x35\x2C\x22\x76\x79\x22\x3A\x30\x2E\x35\x7D")
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

def move_left(): 
    try: 
        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00\x7B\x22\x64\x69\x73\x74\x22\x3A\x35\x2E\x30\x2C\x22\x76\x78\x22\x3A\x30\x2E\x35\x2C\x22\x76\x79\x22\x3A\x30\x2E\x35\x7D")
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

def move_right(): 
    try: 
        PORT = 19206

        s = socket.socket()  
        print("succesfully created Socket")
        # connecting to robot 
        s.connect((ROBOT_IP, PORT))
        print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

        s.send(b"\x5A\x01\x00\x01\x00\x00\x00\x1E\x0B\xEF\x00\x00\x00\x00\x00\x00\x7B\x22\x64\x69\x73\x74\x22\x3A\x35\x2E\x30\x2C\x22\x76\x78\x22\x3A\x30\x2E\x35\x2C\x22\x76\x79\x22\x3A\x30\x2E\x35\x7D")
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



