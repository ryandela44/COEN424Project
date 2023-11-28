import React, { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [customerID, setCustomerID] = useState('');
  const [sessionID, setSessionID] = useState('');
  const [scannedItems, setScannedItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('image_file', image);

    try {
      // Update the URL to include customerID and sessionID in the path
      const response = await fetch(`http://20.246.75.236:5000/v2/Customer/${customerID}/ScanningSession/${sessionID}/Scanner`, {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      if (data && data.scanned_items) {
        setScannedItems(data.scanned_items);
        setTotalPrice(data.total_price);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>Grocery Scanner</h1>
      <input type="file" onChange={handleImageChange} />
      <input
        type="text"
        placeholder="Customer ID"
        value={customerID}
        onChange={(e) => setCustomerID(e.target.value)}
      />
      <input
        type="text"
        placeholder="Session ID"
        value={sessionID}
        onChange={(e) => setSessionID(e.target.value)}
      />
      <button onClick={handleSubmit}>Scan Item</button>
      <div>
        <h2>Scanned Items</h2>
        <ul>
          {scannedItems.map((item, index) => (
            <li key={index}>{item.ItemID} - ${item.Price} x {item.Quantity}</li>
          ))}
        </ul>
        <h3>Total Price: ${totalPrice}</h3>
      </div>
    </div>
  );
}

export default App;