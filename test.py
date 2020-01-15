import json
from web3 import Web3,HTTPProvider,IPCProvider
w3 = Web3(HTTPProvider("http://localhost:8585"))
print(w3.vns.getBlock(w3.toHex(3263921)))
a = w3.vns.getBlock(w3.toHex(3263921))
b = json.dumps(a)
print(b)

number = 0
block_uncles = []
for i in range (0,3321940):
    block = w3.vns.getBlock(w3.toHex(i))
    a = len(block['uncles'])
    number=a+number
    if a>0:
        block_uncles.append(block['uncles'])
    print(a)
print(block_uncles)
print(number)


2440000
f = open('/Users/bill_yu/Downloads/降低奖励之前.rtf', 'r' )


b = []
for i in list1:
    if i not in b:
        b.append(i)

print("去重操作后：")
print(b)


import re

f = open('data.txt', 'r')
r = re.compile(r'[(](.*?)[)]', re.S)
data = f.read()
result = re.findall(r, data)
print(len(result))

s = set()
for i in range(0, len(result)):
 s.add(result[i])

print(len(s))