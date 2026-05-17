import socket

def process_line(line:str):
    first_char =  line[0]
    if first_char.lower() == 'a':
        return ''.join(sorted(line[1:], reverse=True))
    if first_char.lower() == 'c':
        return ''.join(sorted(line[1:]))
    if first_char.lower() == 'd':
        return line[1:].upper()
    return line

class UDPServer:
    def __init__(self, host='127.0.0.1', port=9999):
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind((self.host, self.port))
            while True:
                connection_server, address = server.recvfrom(1024)
                message = connection_server.decode('utf-8').strip()
                line = process_line(message)
                server.sendto((line + '\n').encode('utf-8'), address)

if __name__ == '__main__':
    server = UDPServer()
    server.start_server()

