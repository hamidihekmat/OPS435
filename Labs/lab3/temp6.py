#!/usr/bin/env python3 
import os
import sys
import subprocess

os.system('ls')
os.system('whoami')
os.system('')

p = subprocess.Popen(['date'], stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)

output = p.communicate()
print(output)
print(output[0])
stdout = output[0].decode('utf-8').strip()
print(stdout)
