import socket
import sys

class TCPClient:
    def __init__(self, name, host = '127.0.0.1', port=9090):
        self.name = name
        self.host = host
        self.port = port

    def start_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((self.host, self.port))
            while True:
                message = input("TCP> ").strip()
                if message is None:
                    continue
                if message.lower() == "exit":
                    print(f"[TCP] TCP client {self.name} exited")
                    server.close()
                    break
                server.sendall((message + '\n').encode('utf-8'))
                line = server.recv(1024).decode('utf-8').strip()
                print(f"[TCP] for {self.name}, message = {message}, output = {line}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter a name")
        sys.exit(1)
    else:
        client = TCPClient(sys.argv[1])
        client.start_client()