import os, re
import ipaddress
from ipwhois import IPWhois
import socket

IP_or_DNS = input("Write IP or DNS: ")

# Проверяем, является ли IP адрес корректным
try:
    socket.inet_aton(IP_or_DNS) # если IP адрес валиден, то используем его
    target_address = IP_or_DNS
except socket.error: # если IP адрес не валиден, то пытаемся получить его по DNS имени
    try:
        target_address = socket.gethostbyname(IP_or_DNS)
    except socket.gaierror: # если DNS имя не найдено, выводим сообщение об ошибке и выходим из программы
        print("Incorrect input")
        exit()

command = "tracert " + target_address

os.system("chcp 65001 > nul")
os.system(command + ">> temp.txt")

myMap = {}
with open('temp.txt', 'r') as f:
    for i in range(3):
        f.readline()
    for line in f:
        num = ''
        str = line.strip()
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str)
        if str and str[0].isdigit() and not str[1].isdigit():
            if len(ip) == 1:
                ip_address = ipaddress.ip_address(ip[0]) # конкретнее пояснить эту строчку
                if(ip_address.is_private): # проверяем является ли адрес локальным
                    print(str[0] + ". " + ip[0])
                    print("local")
                    print()
                else:
                    print(str[0] + ". " + ip[0])
                    obj = IPWhois(ip[0]) # пользуемся библиотекой хуИС
                    res = obj.lookup_whois()

                    name = res["nets"][0]["name"]
                    AS = res["asn"]
                    country = res["nets"][0]['country']

                    print(name + ", " + AS + ", " + country)
                    print()

            else: # если айпи адрес не присутствует в строке
                print(str[0] + ". *")
                print()
        elif str and str[0].isdigit() and str[1].isdigit():
            n = str[0] + str[1]
            if len(ip) == 1:
                ip_address = ipaddress.ip_address(ip[0]) # конкретнее пояснить эту строчку
                if(ip_address.is_private): # проверяем является ли адрес локальным
                    print(n + ". " + ip[0])
                    print("local")
                    print()
                else:
                    print(n + ". " + ip[0])
                    obj = IPWhois(ip[0]) # пользуемся библиотекой хуИС
                    res = obj.lookup_whois()

                    name = res["nets"][0]["name"]
                    AS = res["asn"]
                    country = res["nets"][0]['country']

                    print(name + ", " + AS + ", " + country)
                    print()

            else: # если айпи адрес не присутствует в строке
                print(n + ". *")
                print()

    #for key, value in myMap.items():
        #print(key + ". " + value)

path = 'C:/Users/Semyon/PycharmProjects/tracert/temp.txt'
os.remove(path)