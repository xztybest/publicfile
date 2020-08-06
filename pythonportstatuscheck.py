import socket
port_number = [8864 ,192  ,8866 ,30050,8871 ,8873 ,843  ,80   ,443  ,8860 ,8861 ,8862 ]
  
for index in port_number:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', index))
    if result == 0:
        print("Port %d is open" % index)
    else:
        print("Port %d is not open" % index)
    sock.close()