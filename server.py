import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind(('127.0.0.1',8765))
s1.listen(5)
while True:
    conn,adds=s1.accept()
    while True:
        try:
            receives_commands=conn.recv(1024)
            receives_commands=receives_commands.decode('utf-8')
            print(f'来自客户端的消息{receives_commands}')
        except ConnectionResetError:
            print('客户端终端')
            break
conn.close()
s1.close()
                                
