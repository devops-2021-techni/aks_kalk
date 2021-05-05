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
2. az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/b5ace221-8dbd-4bf8-8001-ca33c742b2e5"
3. az login --service-principal -u "http://azure-cli-2021-05-05-13-28-03/" -p "ZMlW1Vp3Hj4gR0d~p5okcVx1kkd_BK0.GL" --tenant "27d29e5d-64be-4e59-a5ec-3abc413c723c"
4. az account set --subscription="b5ace221-8dbd-4bf8-8001-ca33c742b2e5"

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

