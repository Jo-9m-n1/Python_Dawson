'''
There are many ways to write an e-mail addresses.
--> Take a gmail address and add a + and a vaild
    Examples:
    louisa.harutyunyan@gmail.com
    louisa.harutyunyan@gmail.com
--> Dots before the @ symbol are also ignored
    Examples:
    louisa.harutyunyan@gmail.com
    lou.is.a.har.uty.un.yan@gmail.com
--> Upper case and lowercase differences throughout
    the addresses are also ignored
    Examples:
    louisa.harutyunyan@gmail.com
    LouiSa.HaRutyunYan@gmail.com

Given email addresses, determine the number of them
that are unique.
The rules for e-mail addresses are the same as above.
--> Characters from + symbol to the @ symbol are ignored
--> Dots are ignored
--> Case throughout the entire address is ignored

Input specification:
--> First line of input is integer n:
    Designating number of e-mail addresses to read
--> The next n lines are the n addresses
'''

n = int(input())
addresses = []

def clean(address):
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('+')
        address = address[:plus_index] + address[at_index:]
    address = address.replace('.' + '')
    address = address.lower()
    return address
for i in range(n):
    address = input()
    address = clean(address)
    if address not in addresses:
        addresses.append(address)