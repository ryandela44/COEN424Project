import React, { useState } from 'react';
import './App.css';
import { AppBar, Toolbar, Typography, Button, TextField, Card, CardContent, List, ListItem, ListItemText } from '@mui/material';
import CameraIcon from '@mui/icons-material/PhotoCamera';

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
      <AppBar position="static">
        <Toolbar>
          <CameraIcon edge="start" color="inherit" aria-label="logo" sx={{ mr: 2 }} />
          <Typography variant="h6" color="inherit" noWrap>
            Smart Checkout
          </Typography>
        </Toolbar>
      </AppBar>
      <div style={{ margin: '20px' }}>
        <input type="file" onChange={handleImageChange} />
        <TextField label="Customer ID" value={customerID} onChange={(e) => setCustomerID(e.target.value)} variant="outlined" margin="normal" fullWidth />
        <TextField label="Session ID" value={sessionID} onChange={(e) => setSessionID(e.target.value)} variant="outlined" margin="normal" fullWidth />
        <Button variant="contained" color="primary" onClick={handleSubmit} fullWidth>
          Scan Item
        </Button>
        <Card variant="outlined" style={{ marginTop: '20px' }}>
          <CardContent>
            <Typography variant="h5" component="h2">
              Scanned Items
            </Typography>
            <List>
              {scannedItems.map((item, index) => (
                <ListItem key={index}>
                  <ListItemText primary={`${item.ItemID} - $${item.Price} x ${item.Quantity}`} />
                </ListItem>
              ))}
            </List>
            <Typography variant="h6">
              Total Price: ${totalPrice}
            </Typography>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

export default App;