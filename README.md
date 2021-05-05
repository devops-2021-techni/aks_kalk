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
