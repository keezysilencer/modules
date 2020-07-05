import socket


def main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen(3)
    c, addr = s.accept()
    print("Connection has been accepted from " + 'on ' + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("has recieved " + data + ' from ' + str(addr))
        data = data.upper()
        print("Sending " + data)
        c.send(data.encode("utf-8"))
    s.close()


if __name__ == '__main__':
    main()
