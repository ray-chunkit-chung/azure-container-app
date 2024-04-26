# azure-container-app

```bash
az login
az upgrade
az extension add --name containerapp --upgrade

# Register the Microsoft.App and Microsoft.OperationalInsights namespaces in your Azure subscription if you haven't
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights
```

```bash
source .env

az group create --name $RESOURCE_GROUP --location $LOCATION --subscription $SUBSCRIPTION_ID

# az containerapp create --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP --location $LOCATION --image $IMAGE --cpu 1 --memory 1 --port 80 --environment-variables $ENVIRONMENT_VARIABLES

# deploy app1
az containerapp up \
  --name my-container-app \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --subscription $SUBSCRIPTION_ID \
  --environment 'my-container-apps' \
  --image mcr.microsoft.com/k8se/quickstart:latest \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn

# deploy app2
az containerapp up \
  --name my-container-app2 \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --subscription $SUBSCRIPTION_ID \
  --environment 'my-container-apps' \
  --image index.docker.io/raychung/azure-docker-fastapi-nginx \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn


# deploy app3
az containerapp up \
  --name my-container-app3 \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --subscription $SUBSCRIPTION_ID \
  --environment 'my-container-apps' \
  --image index.docker.io/raychung/recommendation-engine-serving-container \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
```

```bash
az containerapp delete -y --name my-container-app2 --resource-group $RESOURCE_GROUP --subscription $SUBSCRIPTION_ID
az group delete --name my-container-apps
```

## AKS

```bash
# Create AKS cluster
az aks create --resource-group $RESOURCE_GROUP --name my-aks --subscription $SUBSCRIPTION_ID --node-count 3 --enable-addons monitoring --generate-ssh-keys

# Configure kubectl to use the credentials from the AKS cluster
az aks get-credentials --resource-group $RESOURCE_GROUP --subscription $SUBSCRIPTION_ID --name my-aks
```
