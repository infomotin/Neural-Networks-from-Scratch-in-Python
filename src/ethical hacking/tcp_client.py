import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1979
s.bind(('', port))
print("%s" % (port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('listing...')
    print('ok', addr)
