import os
import subprocess
import curses
import time

# Set the directory to save screenshots
screenshot_folder = "./screenshots"

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)


def list_open_windows():
    # Use `wmctrl -lG` to list all open windows with details
    result = subprocess.run(["wmctrl", "-lG"], stdout=subprocess.PIPE)
    windows = result.stdout.decode("utf-8").splitlines()

    # Print all available windows
    print("Available windows:")
    for i, window in enumerate(windows):
        print(f"{i}: {window}")

    return windows


def take_screenshot(window_id, screenshot_index):
    screenshot_filename = f"{
        screenshot_folder}/screenshot_{screenshot_index}.jpg"
    os.system(f"scrot -M 0 -w {window_id} {screenshot_filename}")
    return screenshot_filename


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # List all open windows
    windows = list_open_windows()

    # Display the list of windows to the user
    stdscr.addstr(0, 0, "Available windows:\n")
    for idx, window in enumerate(windows):
        stdscr.addstr(idx + 1, 0, f"{idx}: {window}\n")

    stdscr.addstr(len(windows) + 2, 0,
                  "Enter the index of the window: ")
    stdscr.refresh()

    curses.echo()  # Allow user to see their input

    user_input = stdscr.getstr(
        len(windows) + 2, len("Enter the index of the window: ")).decode()
    # curses.noecho()

    try:
        i = int(user_input)
        if 0 <= i < len(windows):
            # Extract window ID from the selected window
            window_info = windows[i]
            # The window ID is the first item
            window_id = window_info.split()[0]
        else:
            stdscr.addstr(len(windows) + 3, 0,
                          "Invalid index. Press any key to exit.")
            stdscr.refresh()
            stdscr.getch()
            return
    except ValueError:
        stdscr.addstr(len(windows) + 3, 0,
                      "Invalid input. Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Set curses to not wait for input when calling getch()
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit.")

    screenshot_index = 1
    # Take screenshot by window ID
    print(f"Take screenshot by window ID: {window_id}")
    while True:
        screenshot_filename = take_screenshot(window_id, screenshot_index)

        # Update the screen output, clearing previous lines
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")
        stdscr.addstr(
            1, 0, f"Screenshot {screenshot_index} saved as: {
                screenshot_filename}"
        )
        stdscr.refresh()

        screenshot_index += 1
        time.sleep(1)

        # Check for keypresses
        key = stdscr.getch()
        if key == ord("q"):  # Quit if 'q' is pressed
            stdscr.addstr(2, 0, "Quitting the program.")
            stdscr.refresh()
            time.sleep(1)
            break


if __name__ == "__main__":
    # Initialize curses
    curses.wrapper(main)
