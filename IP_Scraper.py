from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("-----------Program to Get Top 20 Free IPs-----------")
url = "https://www.us-proxy.org/"
r = requests.get(url , verify=False ,headers={'Accept-encoding': 'gzip'}, timeout=12)

soup = BeautifulSoup(r.text,"html.parser")

TRs = soup.find_all("tr")
IP_port = []
first_row = True

for tr in TRs:
    TDs = tr.find_all("td")
    first_row = False
    for td in TDs:
        if first_row != True:
            IP_port.append(td.text)
print IP_port

file = open("proxies.txt",'w')
for x in xrange(0,1600):
    if x<12:
        print IP_port[x*8]+":"+IP_port[(x*8)+1]

        file.write(IP_port[x * 8] + ":" + IP_port[(x * 8) + 1])
        if x<11:
            file.write('\n')
