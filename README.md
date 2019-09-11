# IPMODULE

IPModule is a random IPv4 and mask generator

## Requirements

* random module

## Methods

```python
randip(n=1)
```

Returns a list of n random IPv4 addresses

```python
randmask(n=1, mode="p"):
```

Returns n numbers of random masks 

mode: "p": prefix format| "d": dotted decimal format

```python
randipmask(self, n=1, mask="p"):
```

Returns n numbers of IPv4 + mask addresses

mask= "p": prefix | "d": dotted

## Example

### Prefix format

Code:

```python
import ipmodule

ip = ipmodule.IPmodule()

for ips in ip.randipmask(5,mask="p"):
    print(ips)
```

Output:

```python
126.248.80.202 /11
91.106.184.71 /19
247.4.169.157 /11
223.14.74.97 /15
155.108.158.228 /12
```

### Dotted decimal format:

Code:

```python
import ipmodule

ip = ipmodule.IPmodule()

for ips in ip.randipmask(5,mask="d"):
    print(ips)
```

Output:

```python
237.186.189.199 248.0.0.0
159.21.229.128 255.252.0.0
20.152.62.11 255.255.255.254
145.88.122.19 248.0.0.0
149.103.30.42 128.0.0.0
```
