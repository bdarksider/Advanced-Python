# get hostname
import socket
print(socket.gethostname())

hostname = socket.gethostname()
print(socket.gethostbyname(hostname))

print(socket.gethostbyname('localhost'))


