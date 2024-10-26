### Notes - IMP
```
$ - is not mandatory for the Kubectl commands
* - Wildcard char which means matching all
{} - Kubectl commands - we must enclose with parenthesis
\n - New line
\t - Tab space
```


* Root Node ($): Refers to the root of the JSON data.
* Dot Notation (.key): Accesses a child node by key.
* Bracket Notation (['key']): Alternative way to access child nodes by key.
* Wildcard (*): Selects all elements at the current level.
* Array Index ([index]): Selects a specific index within an array.
* Array Slice ([start:end:step]): Selects a slice of an array (similar to Python slicing).
* Filter (?(@.key < 10)): Allows filtering based on conditions.
* Recursive Descent (..): Searches all levels of the JSON hierarchy for a specific key.


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
#### Adhoc Commands
```
kubectl get hosts -o jsonpath="{$.items[?(@.spec.hostname=='localhost.com')].spec}"
kubectl get hosts -o jsonpath="{$.items[?(@.spec.hostname=='localhost.com')].metadata.annotations}"
kubectl get hosts -o jsonpath="{$.items[?(@.spec.hostname=='localhost.com')].metadata.labels}"
```

We can also use the custom columns option - to avoid the name loops usage in query
```
kubectl get pods -o custom-columns=IMAGE:.spec.containers[*].image,NAME:spec.containers[*].name
kubectl get pods -o custom-columns=NODENAME:.spec.nodeName,IMAGE:.spec.containers[*].image,NAME:spec.containers[*].name
```
