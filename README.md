## **aks_kalk**

---
---

#### Prérequis :  

- Kubectl
- Azure CLI

Liste des commandes pour l'utiliser en local (besoin de kubectl installé ainsi que Azure CLI) :
Repository de l'application web flaskalk

az login

az aks get-credentials --name tff1_test01 --resource-group tff1

sudo snap install helm --classic

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress-basic --set controller.replicaCount=2 --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux

kubectl apply -f flaskalk.yaml --namespace ingress-basic

kubectl apply -f ingress.yaml

kubectl --namespace ingress-basic get services -o wide -w nginx-ingress-ingress-nginx-controller

---
---

# **TERRAFORM**  

---

## Log to Azure and configure Terraform  
### Step 1 : Login to Azure  
#### Entrer les commandes suivantes une par une :  
```sh
az login
```
```sh
az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/<subscription_id>"
```
```sh
az login --service-principal -u <service_principal_name> -p "<service_principal_password>" --tenant "<service_principal_tenant>"
```
```sh
az account set --subscription="<subscription_id>"
```
> Replace <> fields with your credentials

### Step 2 : Verify Terraform version and configure  
#### Entrer les commandes suivantes une par une :  
```sh
terraform -version
```
```sh
terraform init
```
```sh
terraform plan -out terraform_plan.tfplan
```
```sh
terraform apply terraform_plan.tfplan
```

## Create a Kubernetes cluster with AKS using Terraform  
### Step 1 : Create the directory structure  
#### Entrer les commandes suivantes une par une :  
```sh
cd clouddrive
```
```sh
mkdir terraform-aks-k8s
```
```sh
cd terraform-aks-k8s
```

### Step 2 : Declare the Azure provider  
```sh
code main.tf
```
```sh
=> Enter Configuration <=
```

### Step 3 : Define a Kubernetes cluster  

```sh
code k8s.tf
```
```sh
=> Enter Configuration <=
```

### Step 4 : Declare the variables  
```sh
code variables.tf
```
```sh
=> Enter Configuration <=
```

### Step 5 : Create a Terraform output file  
```sh
code output.tf
```
```sh
=> Enter Configuration <=
```

### Step 6 : Set up Azure storage to store Terraform state  
1) Aller dans les comptes de stockage.
2) Sélectionner un compte de stockage et prendre note de son nom (il sera utilisé plus tard).
3) Une fois le compte sélectionné, aller dans les clés d'accès et copier le champs ***"Key1"***.
4) Entrez la commande ci dessous dans Azure Shell et remplacer les valeurs < > par celles récupérées :
```sh
az storage container create -n tfstate --account-name <YourAzureStorageAccountName> --account-key <YourAzureStorageAccountKey>
```

### Step 7 : Create Kubernetes Cluster  
#### Dans le shell entrez les commandes en remplaçant les valeurs < > par celles récupérées précédement : 
```sh
terraform init -backend-config="storage_account_name=<YourAzureStorageAccountName>" -backend-config="container_name=tfstate" -backend-config="access_key=<YourStorageAccountAccessKey>" -backend-config="key=codelab.microsoft.tfstate"
```
```sh
export TF_VAR_client_id=<service-principal-appid>
```
```sh
export TF_VAR_client_secret=<service-principal-password>
```
```sh
terraform plan -out out.plan
```
```sh
terraform apply out.plan
```

### Step 8 : Test Kubernetes Cluster  
```sh
echo "$(terraform output kube_config)" > ./azurek8s
```
```sh
export KUBECONFIG=./azurek8s
```
```sh
kubectl get nodes
```
> S'il n'y a aucuns nodes, c'est qu'il y a une erreur et il faut donc inspecter tous les fichiers de conf pour trouver cette/ces erreur(s).
