import socket 
import json

ROBOT_IP = "192.168.9.201"

#created a socket object
s = socket.socket()  
print ("succesfully created Socket")


user = input("1 for status req, 2 for navigation")

if (user == "1"): 
    try: 
        PORT = 19204  #for robot status API 
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
        print(f"response: {response}")

    except Exception as e: 
        print(f"Error: {e}")
elif (user == "2"): 
    try: 
        PORT = 19205
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

    except Exception as e: 
        print(f"Error: {e}")

s.close()










