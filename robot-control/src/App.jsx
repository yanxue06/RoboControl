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

  return (
    <>
      <div className="title"> RoboControl </div>

      <div className="controls"> 
        <Button onClick={handleGetStatus} variant="outlined"> Get Status </Button>
        <Button onClick={handleNavigate} variant="outlined"> Relocate </Button>
      </div> 
      
    </>
  ) 
}

export default App
