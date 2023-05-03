import ipaddress
import re

myMap = {}

with open('tracert.txt', 'r') as f:
    # на строках 1-4 инфа, которая не используется
    for i in range(4):
        f.readline()
    # читаем файл с 5 строки
    for line in f:
        num = ''
        str = line.strip()
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str)
        if str and str[0].isdigit():
            if len(ip) == 1:
                ip_address = ipaddress.ip_address(ip[0])
                if(ip_address.is_private):
                    print(str[0] + ". " + ip[0])
                    print("local")
                    print()
                else:
                    print(str[0] + ". " + ip[0])
                    print("Some info about ADRESS") #библиотека хуИС
                    print()
                # myMap[str[0]] = ip[0]
            else:
                print(str[0] + ". *")
                print()

    for key, value in myMap.items():
        print(key + ". " + value)