from ipwhois import IPWhois
# чтобы выявить локальный ли адрес, воспользоваться try / exc , где если поймана ошибка, то значит адрес локальный
# иначе - выполнить код, который ниже

obj = IPWhois('92.242.29.74')
res = obj.lookup_whois()

fakeName = res["name"]

name = res["nets"][0]["name"]
AS = res["asn"]
country = res["nets"][0]['country']

print(name + " " + fakeName)


