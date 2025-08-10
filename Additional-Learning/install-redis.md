
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm show values bitnami/redis > values.yaml
kubectl create secret generic redis-auth --from-literal=redis-password=""  
helm install my-redis bitnami/redis -f values.yaml
kubectl port-forward svc/my-redis-master 6379:6379
redis-cli -h 127.0.0.1 -p 6379 -a testmp


https://medium.com/@hamzanasir323/deploying-redis-on-kubernetes-with-helm-a-step-by-step-guide-2-c79e27035ef6
