import socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    port = 5000
    s.bind((host,port))

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Has received "+data+" from "+ str(addr))
        data = data.upper()
        print('Sending '+data)
        s.sendto(data.encode('utf-8'),addr)

if __name__ == '__main__':
    main()