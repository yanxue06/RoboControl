import './App.css'
import Button from '@mui/material/Button';

function App() {
  const handleGetStatus = async () => {
    try {
      // Returns a promise, which comes to a Response object.
      const response = await fetch('http://localhost:5001/status');
      console.log("get status called"); 

      // Convert the response to JSON
      const data = await response.json();
      console.log('Status Response:', data);
      alert(`Status Response: ${data.message}`);
    } catch (error) {
      console.error('Error fetching status:', error);
    }
  };

  const handleNavigate = async () => {
    try {
      // Example POST to navigate
      const response = await fetch('http://localhost:5001/navigate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("handle navigation called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching navigate:', error);
    }
  };

  const moveForward = async () => { 
    try {
      // Post to moveForward
      const response = await fetch('http://localhost:5001/forward', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("forward  called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching foward:', error);
    }
  }

  const moveBackward = async () => { 
    try {
      const response = await fetch('http://localhost:5001/backward', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("backward  called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching backward:', error);
    }
  }

  const moveLeft = async () => { 
    try {
      
      const response = await fetch('http://localhost:5001/left', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("left called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching left:', error);
    }
  }

  const moveRight = async () => { 
    try {
      // Post to moveright
      const response = await fetch('http://localhost:5001/right', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      }); 

      console.log("right  called")
      const data = await response.json();
      console.log('Navigate Response:', data);
    } catch (error) {
      console.error('Error fetching foward:', error);
    }
  }

  return (
    <>
      <div className="title"> RoboControl </div>

      <div className="controls"> 
        <Button onClick={handleGetStatus} variant="outlined"> Get Status </Button>
        <Button onClick={handleNavigate} variant="outlined"> Relocate (does not work) </Button>
        <Button onClick={moveForward} variant="outlined"> Move Forward </Button>
        <Button onClick={moveBackward} variant="outlined"> Move Backward </Button>
        <Button onClick={moveLeft} variant="outlined"> Move Left </Button>
        <Button onClick={moveRight} variant="outlined"> Move Right </Button>
      </div> 
      
    </>
  ) 
}

export default App
