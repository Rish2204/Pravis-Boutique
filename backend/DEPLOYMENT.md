# Pravis Boutique Backend Deployment Guide

This document outlines the steps to deploy the Pravis Boutique FastAPI backend application both locally and on Azure.

## Prerequisites

- Python 3.8+ installed
- PostgreSQL database
- Azure account for cloud deployment
- Azure CLI installed for Azure deployments

## Local Development Environment Setup

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd pravis-boutique/backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Copy the example .env file
   cp .env.example .env

   # Edit the .env file with your local configuration
   # Particularly, configure the database connection
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Access the API**:
   - API Documentation: http://localhost:8000/docs
   - API Endpoints: http://localhost:8000/api/v1/...

## Azure Deployment

### Deployment with Azure App Service

1. **Login to Azure CLI**:
   ```bash
   az login
   ```

2. **Create resource group (if needed)**:
   ```bash
   az group create --name pravis-boutique-rg --location eastus
   ```

3. **Create Azure App Service Plan**:
   ```bash
   az appservice plan create --name pravis-boutique-plan --resource-group pravis-boutique-rg --sku B1 --is-linux
   ```

4. **Create Azure Web App**:
   ```bash
   az webapp create --resource-group pravis-boutique-rg --plan pravis-boutique-plan --name pravis-boutique-api --runtime "PYTHON|3.8"
   ```

5. **Configure environment variables**:
   ```bash
   az webapp config appsettings set --resource-group pravis-boutique-rg --name pravis-boutique-api --settings \
     ENVIRONMENT=production \
     DATABASE_URL="postgresql://username:password@your-azure-db-server.postgres.database.azure.com:5432/dbname" \
     AZURE_STORAGE_CONNECTION_STRING="your-azure-storage-connection-string" \
     AZURE_STORAGE_CONTAINER_NAME=backups \
     SECRET_KEY="your-secure-secret-key" \
     FRONTEND_URL="https://your-frontend-app.azurewebsites.net"
   ```

6. **Deploy code to Azure**:
   ```bash
   # ZIP the project files
   zip -r backend.zip . -x "venv/*" -x "*.git*" -x "__pycache__/*" -x "*.pyc"

   # Deploy the ZIP file
   az webapp deployment source config-zip --resource-group pravis-boutique-rg --name pravis-boutique-api --src backend.zip
   ```

7. **Configure startup command**:
   ```bash
   az webapp config set --resource-group pravis-boutique-rg --name pravis-boutique-api --startup-file "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app"
   ```

8. **Apply database migrations**:
   ```bash
   # You can run migrations manually or set up a deployment script
   # Example of a migration script that could be run on deployment:
   az webapp ssh --resource-group pravis-boutique-rg --name pravis-boutique-api
   # Then in the SSH session:
   cd /home/site/wwwroot
   alembic upgrade head
   exit
   ```

### Deployment with Azure Container Registry and Container Instances

For more complex deployments, you can use Docker containers:

1. **Create a Dockerfile in your project root**:
   ```Dockerfile
   FROM python:3.8-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8000

   CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
   ```

2. **Build and push the Docker image to Azure Container Registry**:
   ```bash
   # Create ACR
   az acr create --resource-group pravis-boutique-rg --name pravisboutiqueacr --sku Basic

   # Log in to ACR
   az acr login --name pravisboutiqueacr

   # Build and push the image
   az acr build --registry pravisboutiqueacr --image pravis-boutique-api:latest .
   ```

3. **Deploy to Azure Container Instances**:
   ```bash
   az container create \
     --resource-group pravis-boutique-rg \
     --name pravis-boutique-api-container \
     --image pravisboutiqueacr.azurecr.io/pravis-boutique-api:latest \
     --dns-name-label pravis-boutique-api \
     --ports 8000 \
     --environment-variables \
       ENVIRONMENT=production \
       DATABASE_URL="postgresql://username:password@your-azure-db-server.postgres.database.azure.com:5432/dbname" \
       AZURE_STORAGE_CONNECTION_STRING="your-azure-storage-connection-string" \
       FRONTEND_URL="https://your-frontend-app.azurewebsites.net"
   ```

## Continuous Integration/Continuous Deployment (CI/CD)

For automated deployments, set up a GitHub Actions workflow:

1. Create a `.github/workflows/backend-deploy.yml` file in your repository
2. Configure the workflow to deploy on merge to main branch
3. Use Azure credentials to authenticate and deploy automatically

Example GitHub Actions workflow can be found in the `scripts/github-actions` directory.

## Database Management

- **Backup**: Schedule regular database backups to Azure Storage
- **Migrations**: Use Alembic for database schema migrations
- **Scaling**: Configure Azure Database for PostgreSQL for auto-scaling

## Monitoring and Logging

- Set up Application Insights for monitoring
- Configure log streaming to Azure Monitor
- Set up alerts for critical application metrics

## Troubleshooting

- Check application logs in Azure App Service
- Verify environment variables are correctly set
- Test database connectivity from the App Service
- Ensure Azure Storage permissions are properly configured

For assistance, contact the DevOps team or reference the Azure documentation.
