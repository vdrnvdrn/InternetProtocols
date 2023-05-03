import re

str1 = "1 2 ms 2 ms 1 ms 192.168.0.1"
ip1 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str1)

str2 = "2    26 ms     8 ms     9 ms  79.133.87.240"
ip2 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str2)

str4 = "4    49 ms    45 ms    40 ms  188.254.2.4"
ip4 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str4)

str5 = "5     *        *        *     Request timed out."
ip5 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str5)

str7 = "7    40 ms    40 ms    39 ms  srv164-137-240-87.vk.com [87.240.137.164]"
ip7 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str7)

# print(type(ip1[0]))
# print(len(ip2))
# print(ip4)
# print(len(ip5))
# print(ip7)

myMap = {}
str = "2 2 ms 2 ms 1 ms 192.168.0.1"

ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str)

if (len(ip) == 1 and str[0].isdigit()):
    print(str[0] + ". " + ip[0])

exp1 = "1 "
exp2 = "22"


if(str[0].isdigit() and str[1].isdigit()):
    n = str[0] + str[1]
    print(n + ". " + ip[0])
elif(str[0].isdigit() and not str[1].isdigit()):
    n = str[0]
    print(n + ". " + ip[0])