import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is successfully")
except socket.error as e:
    print("some thing wrong %s" % (e))
p = 80

try:
    hot_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('Wrong')
    sys.exit()
s.connect((hot_ip, p))

print("somthing is %s" % (hot_ip))
