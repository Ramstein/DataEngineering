'''
You have a hierarchy of directories and some files in some of those directories:

/root/devops/dir1/file1.txt, file2.txt, ... 
/root/devops/dir2/file3.txt, file4, ...
/root/devops/file6.in, file7.out, ...
...
Some of these files contain IP addresses inside the text. An IP address is a string of form x.x.x.x where each x is a number from 0 to 255 (inclusive).

For example, say we have file1.txt that looks like this:

hello world 127.0.0.1 
this is some example 128.99.107.55 
file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addresses
This file contains only 3 IP addresses, namely 127.0.0.1, 128.99.107.55, and 128.128.4.11, since 0.11.1115.78 is not a valid IP address.

Your task is to find all distinct IP addresses from all the files in the /root/devops/ directory and print them in lexicographical order.

Example

For the following /root/devops/ directory:

/root/devops/dir1/file1.txt

    hello world 127.0.0.1 
    this is some example 128.99.107.55 
    file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addressesaddresses
/root/devops/dir1/file2.txt

    hello from 74.0.65.76 and 8.dd.99.88.907 good
    this is some example 306.5.76.35 
    file with some correct and incorrect 15.128.4.65 ip addresses
    0.0.0.0
/root/devops/dir2/file3.txt

    127.65.64.1 127.0.64.1 127.0.0.1
    exaMple 128.57.107.76 128.57.907.70 
    file with some correct and incorrect 67.128.4.11 ip addresses 7.7.7.8
/root/devops/dir2/file4.txt

    hello world 127.98.0.1 
    this is some example 128.96.107.55 
    file with some correct and incorrect 128.68.4.11 ip addresses
/root/devops/f.inp

    hello world 127.0.49.1 
    this is some example 128.99.58.55 8.88.888.88 77.255.255.254
    7.7.257.25 file with some correct and incorrect 26.56.4.23 ip addresses
the output should be

0.0.0.0
127.0.0.1
127.0.49.1
127.0.64.1
127.65.64.1
127.98.0.1
128.128.4.11
128.57.107.76
128.68.4.11
128.96.107.55
128.99.107.55
128.99.58.55
15.128.4.65
26.56.4.23
67.128.4.11
7.7.7.8
74.0.65.76
77.255.255.254
[execution time limit] 8 seconds (py3)

'''


import os
import re


# Your task is to find all distinct IP addresses from all the files in the /root/devops/ directory and print them in lexicographical order.

def findDistinctIPs(dir):
    ip_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                for line in f:
                    ip_list.extend(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))
    ip_list = list(set(ip_list))
    ip_list.sort()
    return ip_list