# minimal-spanning-subnet



## Run

```bash
python3 main.py
```

## Input

Locate the `ip_list` variable at the end of `main.py` and modify accordingly. The default example is:

```python
ip_list = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.127']
```

## Example output

```bash
$ python3 main.py 
Provided list of IPs:
Binary                              Dotted-decimal notation    int           Comments            
11000000101010000000000000000001    192.168.0.1                3232235521
11000000101010000000000000000010    192.168.0.2                3232235522
11000000101010000000000000000011    192.168.0.3                3232235523
11000000101010000000000000000100    192.168.0.4                3232235524
11000000101010000000000001111111    192.168.0.127              3232235647
--------------------------------------------------------------------------------------------

Step 1: Narrowing down the problem by finding the min/max IPs
11000000101010000000000000000001    192.168.0.1                3232235521    (min)
11000000101010000000000001111111    192.168.0.127              3232235647    (max)

Step 2: locate different bits with XOR (1=different)
00000000000000000000000001111110

Step 3: find common prefix (leading zeros of the XOR result)
00000000000000000000000001111110
                        ^ 25 found

Step 4: find subnet mask, apply it to min IP
11000000101010000000000000000001    192.168.0.1                3232235521    (min)
11111111111111111111111110000000    255.255.255.128            4294967168    (subnet mask)
11000000101010000000000000000000    192.168.0.0                3232235520    (network address)

Step 5: Result
192.168.0.0/25
```

Most of the lines printed have the following format:

    IP (binary)    IP (dotted-decimal notation)    IP (integer)    (comment if any)


### Approach

 - Step 1: focus on the min/max of the IPs provided
 - Step 2, 3: use XOR to find their common prefix
 - Step 4: use the subnet mask and the min IP to find the network address
 - return result in CIDR notation

 ### result: `0.0.0.0/0`

 In case the IP addresses provided have no common prefix (for example `10.0.0.0` and `128.0.0.0`) the returned result is ``0.0.0.0/0``

 ```bash
Binary                              Dotted-decimal notation   
00001010000000000000000000000000    10.0.0.0               
10000000000000000000000000000000    128.0.0.0              
 ```
