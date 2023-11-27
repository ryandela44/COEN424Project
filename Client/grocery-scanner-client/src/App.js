import React, { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [customerID, setCustomerID] = useState(''); // Placeholder for customerID
  const [sessionID, setSessionID] = useState(''); // Placeholder for sessionID
  const [items, setItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
   formData.append('customerID', customerID);
   formData.append('sessionID', sessionID);
   formData.append('image_file', image);

    try {
      const response = await fetch('http://127.0.0.1:5000/V2/CustomVision/scan-item', {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json',
        },
      });

      const data = await response.json();
      if (data && data.items) {
        setItems(data.items);
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
          {items.map((item, index) => (
            <li key={index}>{item.ProductName} - ${item.Price} x {item.Quantity}</li>
          ))}
        </ul>
        <h3>Total Price: ${totalPrice}</h3>
      </div>
    </div>
  );
}

export default App;