import React, { useState } from "react";
import './App.css'
import Button from '@mui/material/Button';
import TextField from "@mui/material/TextField";

//TO ACTIVATE THE ENV: source env/bin/activate

function App() {

  // STATUS 
  const handleGetStatus = async () => {
    try {
      // Returns a promise, which comes to a Response object.
      const response = await fetch('http://localhost:5001/status');
      console.log("get status called"); 

      // Convert the response to JSON
      const data = await response.json();
      console.log('Status Response:', data);
    } catch (error) {
      console.error('Error fetching status:', error);
    }
  };

  const handleGetLocation = async () => {
    try {
      // Returns a promise, which comes to a Response object.
      const response = await fetch('http://localhost:5001/location');
      console.log("get location called"); 

      // Convert the response to JSON
      const data = await response.json();
      console.log('Status Response:', data);
    } catch (error) {
      console.error('Error fetching status:', error);
    }
  };

  const handleGetBattery = async () => { 
    try {
      const response = await fetch('http://localhost:5001/battery')
      console.log("get battery called")
      // Convert the response to JSON
      const data = await response.json();
      console.log('Status Response:', data);
    } catch (error) {
      console.error('Error fetching status:', error);
    }
  }

  // CONTROLS 
  const handleRelocate = async () => {
    try {
      // Example POST to navigate
      const response = await fetch('http://localhost:5001/relocate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("handle navigation called")
      const data = await response.json();
      console.log('relocate Response:', data);
    } catch (error) {
      console.error('Error fetching relocate:', error);
    }
  };


  const handleSoundPlay = async () => { 
    try { 
      const response = await fetch('http://localhost:5001/soundPlay', {
        method: 'POST', 
        headers: { 
          'Content-Type': 'application/json'
        }
      }); 
    } catch (error) {
      console.error('Error fetching relocate:', error); 
    }
  } 
   
  const handleSoundPause = async () => { 
    try { 
      const response = await fetch('http://localhost:5001/soundPause', {
        method: 'POST', 
        headers: { 
          'Content-Type': 'application/json'
        }
      });
    } catch (error) {
      console.error('Error fetching relocate:', error); 
    }
  }
  
  //NAVIGATE 
  
  //FORWARD 
  const moveForward = async () => { 
    try {
      // TESTING DATA, in the form of a dictionary 
      const testData = {
        distance: Number(valueForward) //convert string to int
      };
      if (!testData.distance) {
        alert("Please enter a valid distance!");
        return;
      }

      console.log('sending forward:', valueForward, ' meters');

      // Post to moveForward
      const response = await fetch('http://localhost:5001/forward', { //waits for http request to complete 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(testData) // change into a JSON to use in the Post Request 
      }); 

      console.log("forward called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching foward:', error);
    }
  }

  const [valueForward, setForwardValue] = useState("");

  const handleForwardChange = (event) => {
    setForwardValue(event.target.value)
  }
  /*
  event is the event object provided by the onChange handler.
  event.target refers to the input element that triggered the event.
  event.target.value contains the current text entered by the user.
  */

  //BACK 
  const moveBackward = async () => { 
    try {
      const testData = {
        distance: Number(valueBackward) //convert string to int
      };
      if (!testData.distance) {
        alert("Please enter a valid distance!");
        return;
      }

      const response = await fetch('http://localhost:5001/backward', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        'body': JSON.stringify(testData)
      }); 

      console.log("backward  called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching backward:', error);
    }
  }

  const [valueBackward, setBackwardValue] = useState("");

  const handleBackwardChange = (event) => {
    setBackwardValue(event.target.value)
  }

  //ROTATE
  const [valueAngleLeft, setAngleValue] = useState("");

  const handleAngleLeftChange = (event) => {
    setAngleValue(event.target.value)
  }

  const rotateLeft = async () => { 
    try {
      const testData = {
        angle: Number(valueAngleLeft) //convert string to int
      };
      if (!testData.angle) {
        alert("Please enter a valid angle in degrees!");
        return;
      }

      const response = await fetch('http://localhost:5001/rotateLeft', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }, 
        body: JSON.stringify(testData)
      }); 

      console.log("rotate left called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching backward:', error);
    }
  }

  const [valueAngleRight, setAngleRightValue] = useState("");

  const handleAngleRightChange= (event) => {
    setAngleRightValue(event.target.value)
  }

  const rotateRight = async () => { 
    try {
      const testData = {
        angle: Number(valueAngleRight) //convert string to int
      };
      if (!testData.angle) {
        alert("Please enter a valid angle in degrees!");
        return;
      }

      const response = await fetch('http://localhost:5001/rotateRight', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }, 
        body: JSON.stringify(testData)
      }); 

      console.log("rotate left called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching backward:', error);
    }
  }

  return (
    <>
      <div className="title"> Robot Control System</div>
      <div className="container">
        <div className="column">
          <h2>Status</h2>
          <Button onClick={handleGetStatus} variant="outlined">
            Get General Info
          </Button>
          <Button onClick={handleGetLocation} variant="outlined">
            Get Location 
          </Button>
          <Button onClick={handleGetBattery} variant="outlined">
            Get Battery 
          </Button>
        </div>

        <div className="column">
          <h2>Control</h2> 
          <Button onClick={handleRelocate} variant="outlined">
            Relocate
          </Button>
          <Button onClick={handleSoundPlay} variant="outlined">
            Play Sound
          </Button>
          <Button onClick={handleSoundPause} variant="outlined">
            Pause Sound 
          </Button>
        </div>

        <div className="column">
          <h2>Navigation</h2>
          <div className = "attached"> 
            <Button onClick={moveForward} variant="outlined" sx={{width: "11rem"}}>
              Move Forwards
            </Button>
            <TextField 
              id="outlined-basic" 
              label="distance" 
              variant="outlined" 
              size="small"
              value={valueForward}
              onChange={handleForwardChange}
              sx={{
                "& .MuiOutlinedInput-root": {
                  "& fieldset": {
                    borderColor: "beige", // Default border color
                  },
                }, 
                "& .MuiInputLabel-root": {
                    color: "grey", // Default label color
                },
                "& .MuiInputBase-input": {
                    color: "beige", // Change the text color
                },
                width: "150px"
              }} 
            />
          </div> 
          <div className = "attached"> 
            <Button onClick={moveBackward} variant="outlined" sx={{width: "11rem"}}>
              Move Backward
            </Button>
            <TextField 
              id="outlined-basic" 
              label="distance" 
              variant="outlined" 
              size="small"
              value={valueBackward}
              onChange={handleBackwardChange}
              sx={{
                  "& .MuiOutlinedInput-root": {
                    "& fieldset": {
                      borderColor: "beige", // Default border color
                    },
                  },
                  "& .MuiInputLabel-root": {
                    color: "grey", // Default label color
                  },
                  "& .MuiInputBase-input": {
                    color: "beige", // Change the text color
                  },
                  width: "150px"
                }} 
              />
          </div>
          <div className="attached"> 
            <Button onClick={rotateLeft} variant="outlined" sx={{width: "11rem"}}>
              Rotate Left
            </Button>
            <TextField 
              id="outlined-basic" 
              label="angle" 
              variant="outlined" 
              size="small"
              value={valueAngleLeft}
              onChange={handleAngleLeftChange}
              sx={{
                  "& .MuiOutlinedInput-root": {
                    "& fieldset": {
                      borderColor: "beige", // Default border color
                    },
                  },
                  "& .MuiInputLabel-root": {
                    color: "grey", // Default label color
                  },
                  "& .MuiInputBase-input": {
                    color: "beige", // Change the text color
                  },
                  width: "150px"
                }} 
              />
          </div>

          <div className="attached"> 
            <Button onClick={rotateRight} variant="outlined" sx={{width: "11rem"}}>
              Rotate Right
            </Button>
            <TextField 
              id="outlined-basic" 
              label="angle" 
              variant="outlined" 
              size="small"
              value={valueAngleRight}
              onChange={handleAngleRightChange}
              sx={{
                  "& .MuiOutlinedInput-root": {
                    "& fieldset": {
                      borderColor: "beige", // Default border color
                    },
                  },
                  "& .MuiInputLabel-root": {
                    color: "grey", // Default label color
                  },
                  "& .MuiInputBase-input": {
                    color: "beige", // Change the text color
                  },
                  width: "150px"
                }} 
              />
          </div>
          
        </div>
      </div>

      
    </>
  ) 
}

export default App