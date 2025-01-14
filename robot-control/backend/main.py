import socket 

ROBOT_IP = "198.102.9.201"
PORT = 19204  #for robot status API 

#created a socket object
s = socket.socket()  
print ("succesfully created Socket")

try: 
    # connecting to robot 
    s.connect((ROBOT_IP, PORT))
    print(f"Connected to the robot at {ROBOT_IP}:{PORT}")

    


