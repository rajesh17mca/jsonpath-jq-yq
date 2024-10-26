#### Get the Image details from all PODs
```
kubectl get pods -o jsonpath="{.items[*].spec.containers[*].image}"
```
#### Get the Image and Container name from all PODs
```
kubectl get pods -o jsonpath="{.items[*].spec.containers[*].image}{.items[*].spec.containers[*].name}"
```
#### Get the Image and Container name from all PODs - Formating as line-by-line - Image Name in one line and Container name in another line
```
kubectl get pods -o jsonpath="{.items[*].spec.containers[*].image}{'\n'}{.items[*].spec.containers[*].name}"
```
#### Get the Image and Container name from all PODs - With loops custom the above output
```
kubectl get pods -o jsonpath="{range .items[*]}{.spec.containers[*].image}{'\t'}{.spec.containers[*].name}{'\n'}{end}"
```
