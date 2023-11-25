import connexion
import uvicorn

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('COEN424_Raptors-SmartCheckout-v2.0-resolved.json')

if __name__ == '__main__':
    uvicorn.run("App:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)
