# Crazy Port Scanner


## 1. Usage:
The 24, 16, 8 are done the same as how *NMAP* would do it

`ex: nmap 192.168.100.0/24`

`ex: nmap 192.168.0.0/16`

`ex: nmap 192.0.0.0/8`

The option 0 is to scan a single host

`ex: nmap 192.168.100.1`


```
python portscan.py ip iprange(ex: 24, 16, 8, 0) [OPTIONAL]timeout(ex: 0.5) [OPTIONAL]port
```

## 2. Examaple

```
python portscan.py 192.168.100.1 0
```
_Single Host Scan Option_


![Single Host](https://i.imgur.com/CdWkG4o.png)

_Nmap Command After Scan_


![NmapAdded](https://i.imgur.com/hyHNBet.png)
