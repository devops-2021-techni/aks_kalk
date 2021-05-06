# aks_kalk
Repository de l'application web flaskalk


Liste des commandes pour l'utiliser en local (besoin de kubectl installé ainsi que Azure CLI) :

az login

az aks get-credentials --name tff1_test01 --resource-group tff1

sudo snap install helm --classic

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress-basic --set controller.replicaCount=2 --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux

kubectl apply -f flaskalk.yaml --namespace ingress-basic

kubectl apply -f ingress.yaml

kubectl --namespace ingress-basic get services -o wide -w nginx-ingress-ingress-nginx-controller

---
TERRAFORM
---
---------------------------------------------
Log to Azure and configure Terraform
---------------------------------------------

Step 1 : Login to Azure

1. az login
2. az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/<subscription_id>"
3. az login --service-principal -u <service_principal_name> -p "<service_principal_password>" --tenant "<service_principal_tenant>"
4. az account set --subscription="<subscription_id>"
(Replace <> fields with your credentials)

Step 2 : Verify Terraform version and configure

1. terraform -version
-- Create config file and upload to Azure
2. terraform init
3. terraform plan -out terraform_plan.tfplan
4. terraform apply terraform_plan.tfplan
-- Terraform is configured !

---------------------------------------------
Create a Kubernetes cluster with AKS using Terraform
---------------------------------------------

Step 1 : Create the directory structure

1. cd clouddrive
2. mkdir terraform-aks-k8s
3. cd terraform-aks-k8s

Step 2 : Declare the Azure provider

1. code main.tf
-- Enter Configuration

Step 3 : Define a Kubernetes cluster

1. code k8s.tf
-- Enter Configuration

Step 4 : Declare the variables

1. code variables.tf
-- Enter Configuration

Step 5 : Create a Terraform output file

1. code output.tf
-- Enter Configuration

Step 6 : Set up Azure storage to store Terraform state

a) Aller dans les comptes de stockage, en sélectionner un et prendre note de son nom (on en a besoin plus tard)
b) Une fois le compte sélectionné, aller dans les clés d'accès et copier le champs "Key1"
c) Entrez la commande ci dessous dans Azure Shell et remplacer les valeurs par celles récupérées :
1. az storage container create -n tfstate --account-name <YourAzureStorageAccountName> --account-key <YourAzureStorageAccountKey>

Step 7 : Create Kubernetes Cluster

a) Dans le shell entrez les commandes en remplaçant les valeurs par celles récupérées précédement : 
1. terraform init -backend-config="storage_account_name=<YourAzureStorageAccountName>" -backend-config="container_name=tfstate" -backend-config="access_key=<YourStorageAccountAccessKey>" -backend-config="key=codelab.microsoft.tfstate"
2. export TF_VAR_client_id=<service-principal-appid>
3. export TF_VAR_client_secret=<service-principal-password>
4. terraform plan -out out.plan
5. terraform apply out.plan

Step 8 : Test Kubernetes Cluster

1. echo "$(terraform output kube_config)" > ./azurek8s
2. export KUBECONFIG=./azurek8s
3. kubectl get nodes
-- S'il n'y a aucuns nodes, c'est qu'il y a une erreur et il faut donc inspecter tous les fichiers de conf pour trouver cette/ces erreur(s).



