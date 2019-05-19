#!/usr/bin/env python3
from lab7a import *

ip = IPAddress("192.168.2.1")
ip2 = IPAddress("10.1.1.1")
ip3 = IPAddress("99.1.4.2")
print(ip.isPrivate())
print(ip2.isPrivate())
print(ip3.isPrivate())
