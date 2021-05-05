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

Connect to azure and set account

1. az login
2. az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/b5ace221-8dbd-4bf8-8001-ca33c742b2e5"
3. az login --service-principal -u "http://azure-cli-2021-05-05-13-28-03/" -p "ZMlW1Vp3Hj4gR0d~p5okcVx1kkd_BK0.GL" --tenant "27d29e5d-64be-4e59-a5ec-3abc413c723c"
4. az account set --subscription="b5ace221-8dbd-4bf8-8001-ca33c742b2e5"

Verify Terraform version and configure

1. terraform -version
-- Create config file and upload to Azure
2. terraform init
3. terraform plan -out terraform_plan.tfplan
4. terraform apply terraform_plan.tfplan
-- Terraform is configured !

