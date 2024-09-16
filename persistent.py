import os
import subprocess

def make_persistent():
    # Get the path to the Python executable and the current script
    python_path = os.path.realpath(os.__file__).replace('lib\\os.py', 'python.exe')
    script_path = os.path.realpath(__file__)

    # PowerShell script to create startup and shutdown scheduled tasks
    powershell_script = f'''
    $action = New-ScheduledTaskAction -Execute "{python_path}" -Argument "{script_path}"
    $startupTrigger = New-ScheduledTaskTrigger -AtStartup
    $shutdownTrigger = New-ScheduledTaskTrigger -AtLogon
    Register-ScheduledTask -Action $action -Trigger $startupTrigger -TaskName "PersistentPythonScript_Startup" -Description "Runs the Python script at system startup"
    Register-ScheduledTask -Action $action -Trigger $shutdownTrigger -TaskName "PersistentPythonScript_Shutdown" -Description "Runs the Python script at system shutdown"
    '''

    # Running the PowerShell script to create the tasks
    subprocess.run(["powershell", "-Command", powershell_script], shell=True)

# Check if the script is already persistent
def is_persistent():
    result = subprocess.run(["powershell", "-Command", "Get-ScheduledTask -TaskName PersistentPythonScript_Startup"], capture_output=True, text=True)
    return "PersistentPythonScript_Startup" in result.stdout

if __name__ == "__main__":
    # Check if the script is already registered as persistent
    if not is_persistent():
        make_persistent()
        print("The script has been made persistent.")
    else:
        print("The script is already persistent.")

    # Add the main logic of your script here
    print("Running the main part of the script...")

    # Your existing code continues here...