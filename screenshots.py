import os
import time
import subprocess
from datetime import datetime

# Create the screenshots folder if it doesn't exist
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def take_screenshot():
    # Generate a filename based on the current time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshots/screenshot_{timestamp}.png'
    
    # Call the GNOME screenshot service using dbus-send to take a screenshot
    result = subprocess.run([
        'gnome-screenshot',
        '-w',
        '-f',
        filename
    ], capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        print(f"Screenshot saved: {filename}")
    else:
        print(f"Failed to take screenshot: {result.stderr}")

def main():
    print("Program start!.")
    
    while True:
        # Take a screenshot
        take_screenshot()
        
        # Wait for 1 second
        time.sleep(1)

if __name__ == '__main__':
    main()

