```
kubectl get pods -o jsonpath="{range .items[*]}{.spec.containers[*].image}{'\t'}{.spec.containers[*].name}{'\n'}{end}"
```
