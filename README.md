# Mouse Cursor Mover

This Python program automates moving the mouse cursor to a specific location on the screen at a specified time. It is useful for automation tasks or keeping a system active.

## Features

- Move the mouse cursor to a predefined location.
- Simulate mouse activity periodically to keep the system active.
- Lightweight and straightforward script.

## Requirements

- Python 3.6 or higher
- The following Python libraries:
  - `pyautogui`
  - `time`
  - `datetime`

## Installation

1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Clone or download the script.
2. Open the script in your preferred code editor.
3. Modify the `time.sleep` interval in the script to suit your needs (default is 60 seconds).
4. Run the script:
   ```bash
   python mouse_mover.py
   ```
5. Optionally, create a CMD file to easily execute the program:
   - If using the system's Python installation:
     ```cmd
     @echo off
     python path\to\mouse_mover.py
     pause
     ```
   - If using a virtual environment:
     ```cmd
     @echo off
     path\to\venv\Scripts\python path\to\mouse_mover.py
     pause
     ```
   Save this as `run_mouse_mover.cmd` and double-click it to run the program.

## Notes

- The script ensures minimal movement to simulate activity and avoid disrupting workflows.
- Ensure you have the necessary permissions to run scripts that control the mouse.
- Adjust the sleep interval to control how frequently the mouse moves.

## Contributing

Feel free to fork the repository, make improvements, and submit a pull request. Contributions are welcome!
