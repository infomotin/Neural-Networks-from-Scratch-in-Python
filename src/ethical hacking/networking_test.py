import socket
s = socket.socket()

port = 12345
s.bind(('', port))
print('Soket buid is %s' % (port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Listing")
    print(addr)
