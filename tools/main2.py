import os, re
import sys
from ipwhois import IPWhois

IP_or_DNS = input("Write IP or DNS: ")

# if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$|^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\
#                      (\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))+$', IP_or_DNS):
#     print(IP_or_DNS + " is invalid")
#     sys.exit()
#
# else:
command = ''
command = "tracert " + IP_or_DNS

os.system("chcp 65001 > nul")
os.system(command + ">> tracert.txt")

myMap = {}
with open('tracert.txt', 'r') as f:
    for i in range(4):
        f.readline()
    for line in f:
        str = line.strip()
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str)

        if str and str[0].isdigit():
            if (len(ip) == 1):
                if ip[0].startswith('192.168.'):
                    print(str[0] + ". " + ip[0])
                    print("local")
                    print()
                else:
                    print(str[0] + ". " + ip[0])
                    obj = IPWhois(ip[0])
                    res = obj.lookup_whois()

                    name = res["nets"][0]["name"]
                    AS = res["asn"]
                    country = res["nets"][0]['country']
                    print(name + " " + AS + " " + country)
                    print()
            else:
                print(str[0] + ". " + '*')
                print()


path = '/tracert.txt'
os.remove(path)

# ipwhois.exceptions.IPDefinedError