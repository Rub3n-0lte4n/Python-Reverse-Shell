import os
import subprocess
import sys

def check_pyinstaller_installed():
    """Check if PyInstaller is installed, if not, install it."""
    try:
        # Check if PyInstaller is installed
        __import__('PyInstaller')
        print("PyInstaller is already installed.")
    except ImportError:
        # Install PyInstaller if not installed
        print("PyInstaller is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")

def convert_to_executable(script_path):
    """Converts a Python script to an executable using PyInstaller."""
    if not os.path.exists(script_path):
        print(f"The script '{script_path}' does not exist.")
        return

    # Run PyInstaller command to package the script as an executable
    print(f"Converting '{script_path}' to executable...")
    subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", script_path], check=True)

    # After conversion, show where the executable is located
    dist_dir = os.path.join(os.getcwd(), "dist")
    exe_name = os.path.splitext(os.path.basename(script_path))[0] + ".exe"
    exe_path = os.path.join(dist_dir, exe_name)

    if os.path.exists(exe_path):
        print(f"Executable created successfully: {exe_path}")
    else:
        print("Something went wrong. Executable not found.")

def main():
    # Check if PyInstaller is installed
    check_pyinstaller_installed()

    # Get the Python script path from the user
    script_path = input("Enter the path of the Python script to convert: ")

    # Convert the script to an executable
    convert_to_executable(script_path)

if __name__ == "__main__":
    main()