# Python Script to Executable Converter

This Python project converts any given Python script into an executable file (`.exe`) using **PyInstaller**. It automatically checks if PyInstaller is installed and installs it if necessary.

## Features

- Automatically checks for **PyInstaller**.
- Installs **PyInstaller** if not already present.
- Converts any provided Python script into a standalone executable.
- The output `.exe` is located in the `dist` directory.

## Requirements

- **Python 3.x**
- **pip** (Python package manager)

## Installation

Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-to-exe.git
cd python-to-exe
```

### 2. Install Dependencies

The script will automatically install PyInstaller if it's not already installed. However, you can manually install PyInstaller using `pip` as well:

```bash
pip install pyinstaller
```

## Usage

1. Run the `script_to_exe.py` script.
   ```bash
   python script_to_exe.py
   ```

2. When prompted, enter the path of the Python script you want to convert to an executable.
   ```bash
   Enter the path of the Python script to convert: C:\path\to\your_script.py
   ```

3. The script will convert the Python script into an executable and place the output `.exe` file in the `dist` directory.
   
4. The output will be a standalone executable located in:
   ```
   ./dist/your_script.exe
   ```

### Example

```bash
python script_to_exe.py
```

**Output**:
```
Enter the path of the Python script to convert: C:\Users\example\reverse_shell.py
PyInstaller is already installed.
Converting 'C:\Users\example\reverse_shell.py' to executable...
Executable created successfully: C:\Users\example\dist\reverse_shell.exe
```

## Troubleshooting

- **PyInstaller Not Found**: If the script fails to install PyInstaller, try manually installing it using `pip install pyinstaller`.
- **Permission Denied**: Ensure you are running the script with appropriate permissions (Administrator/Root).
- **Executable Not Found**: Make sure the script exists and is provided with the correct path.

## Notes

- The generated executable will be located in the `dist` folder in the same directory where you run the script.
- By default, the script is packaged into a single file using the `--onefile` option of PyInstaller.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this script as you see fit.

---

This `README.md` provides clear instructions on how to use the project, including installation, usage, and troubleshooting steps. You can place this in the root folder of your project, and it will serve as a guide for users.