import socket
import sys

class UDPClient:
    def __init__(self, name, host = '127.0.0.1', port=9999):
        self.name = name
        self.host = host
        self.port = port

    def start_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.settimeout(5)
            server.connect((self.host, self.port))
            while True:
                message = input("UDP> ").strip()
                if not message:
                    continue
                if message.lower() == "exit":
                    print(f"[UDP] TCP client {self.name} exited")
                    server.close()
                    break
                server.sendto((message + '\n').encode('utf-8'), (self.host, self.port))
                try:
                    line, _ = server.recvfrom(1024)
                    line = line.decode('utf-8').strip()
                    print(f"[UDP] for {self.name}, message = {message}, output = {line}")
                except socket.timeout:
                    print("[UDP] No response received.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter an name")
        sys.exit(1)
    else:
        client = UDPClient(sys.argv[1])
        client.start_client()

