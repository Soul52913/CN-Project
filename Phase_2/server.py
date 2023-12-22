import socket
import message

server_ip = "192.168.56.1"
server_port = 7414

def main():
    server = socket.socket()
    server.bind((server_ip, server_port))
    server.listen(5)

    print(f'Listening on {server_ip}:{server_port}')
    print('wait for connection...')

    while True:
        c, (client_IP, client_port) = server.accept()
        print(f"connected from IP: {client_IP}, Port: {client_port}")
        # indata = str(client.recv(2048), encoding='utf-8')
        # print(f"message from client {str(addr)}: {indata}")
        # outdata = "hello!"
        # client.sendall(outdata.encode())
        c.recv(1000)
        c.send(b'HTTP/1.0 200 OK\r\n')
        c.send(b'Content-Type: text/html\r\n')
        c.send(b'\r\n')
        with open('homepage.html', 'rb') as f:
            html = f.read()
        c.send(html)
        c.close()

main()
