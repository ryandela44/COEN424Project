# GET /v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem
def list_scanned_items(sessionID, customerID):
    pass

# POST /v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem
def add_scanned_item(sessionID, customerID):
    pass

# GET, PUT, DELETE for specific scanned item by ScannedItemID, SessionID, and CustomerID
def get_scanned_item_by_id(scannedItemID, sessionID, customerID):
    pass

def update_scanned_item(scannedItemID, sessionID, customerID, scanned_item):
    pass

def delete_scanned_item(scannedItemID, sessionID, customerID):
    pass