// STATUS 
export const handleGetStatus = async () => {
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

export const handleGetLocation = async () => {
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

export const handleGetBattery = async () => { 
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
