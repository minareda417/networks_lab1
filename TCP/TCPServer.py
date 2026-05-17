import socket
import threading

def process_line(line:str):
    first_char =  line[0]
    if first_char.lower() == 'a':
        return ''.join(sorted(line[1:], reverse=True))
    if first_char.lower() == 'c':
        return ''.join(sorted(line[1:]))
    if first_char.lower() == 'd':
        return line[1:].upper()
    return line

class TCPServer:
    def __init__(self, host = '127.0.0.1', port=9090, backlog=5):
        self.host = host
        self.port = port

    def __handle_client(self, communication_socket:socket, address):
        try:
            with communication_socket:
                while True:
                    message = communication_socket.recv(1024)
                    if not message:
                        print(f'[TCP] client {address} disconnected')
                        break
                    line = message.decode('utf-8').strip()
                    line = process_line(line)
                    communication_socket.sendall((line+'\n').encode('utf-8'))
        except ConnectionResetError:
            print(f'[TCP] client {address} disconnected with an error')
        finally:
            print(f'[TCP] connection with {address} closed')


    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, self.port))
            server.listen(5)

            while True:
                communication_socket, address = server.accept()
                client_thread = threading.Thread(
                    target= self.__handle_client,
                    args = (communication_socket, address),
                    daemon= True
                )
                client_thread.start()


if __name__ == '__main__':
    server = TCPServer()
    server.start_server()

