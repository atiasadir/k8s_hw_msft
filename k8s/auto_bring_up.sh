#!/bin/bash

auto_completion_kubectl(){
source <(kubectl completion bash)
}

auto_deployment()
{
echo "-I- Bring up service A"
kubectl apply -f  service_and_deployment_a.yaml
echo "-I- Bring up service B"
kubectl apply -f service_and_deployment_b.yaml
echo "-I- Bring up Network Policy"
kubectl apply -f deny-from-other-namespaces.json
}

auto_cleanup()
{
kubectl delete all --all
}
