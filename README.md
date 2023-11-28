# COEN424Project: SmartCheckout

## Project Overview
The SmartCheckout System is a grocery checkout service that automates billing by scanning images of grocery items. It utilizes a custom vision AI to identify items and calculate the total bill.

## Features
- Image scanning and item identification via custom vision AI.
- RESTful API for item management and checkout process.
- CI/CD pipeline using Docker and GitHub Actions.
- Deployment on Azure cloud.

## Technologies Used
- Flask (Python)
- MongoDB
- Azure Custom Vision
- Docker
- GitHub Actions

## API Endpoints
Item:
GET /v2/Item
POST /v2/Item
GET /v2/Item/{ItemID}
PUT /v2/Item/{ItemID}
DELETE /v2/Item/{ItemID}

Customer:
GET /v2/Customer
POST /v2/Customer
POST /v2/Customer
GET /v2/Customer/{CustomerID}
PUT /v2/Customer/{CustomerID}
DELETE /v2/Customer/{CustomerID}

Supermarket:
GET /v2/Supermarket
POST /v2/Supermarket
POST /v2/Supermarket
GET /v2/Supermarket/{SupermarketID}
PUT /v2/Supermarket/{SupermarketID}
DELETE /v2/Supermarket/{SupermarketID}

Scanning Session:

## Custom Vision Integration
Custom vision is utilized to identify items from images. The system sends images to the Azure Custom Vision service, which returns predicted items based on the trained model.

## Deployment
The project is containerized using Docker and deployed to an Azure virtual machine. Ensure the VM has the necessary dependencies installed and is properly configured to run the Flask application.

## CI/CD Pipeline
The CI/CD pipeline is managed using GitHub Actions, which automates the process of building, testing, and deploying the Docker container to Azure.

### Docker Build and Push
The Docker image is built and pushed to a container registry using the `docker/build-push-action`.

### Continuous Integration
The CI process includes linting, testing, and building the application. Ensure that your test cases and linting rules are defined according to your project's requirements.

### Continuous Deployment
The CD process involves deploying the Docker container to the Azure VM. This process should be automated via GitHub Actions, triggered on pushes to the main branch or specific version tags.

## Local Development Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the Flask application: `python Server/App.py`.

## Contributing
- Yvon Wetie Mougang
- Athiru Pathiraja
- Amish Patel
- Amir Cherif 
---
