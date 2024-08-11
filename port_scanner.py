import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # This line should be on one line
        sock.settimeout(3)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False

def main():
    target_ip = "127.0.0.1"
    for port in [80, 443, 22]:
        if scan_port(target_ip, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()
