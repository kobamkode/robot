import os
import time
import curses

# Set the directory to save screenshots
screenshot_folder = "./screenshots"

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)


def take_screenshot(index):
    screenshot_filename = f"{screenshot_folder}/screenshot_{index}.jpg"
    os.system(f"scrot -M 0 {screenshot_filename}")
    return screenshot_filename


def main(stdscr):
    index = 1

    # Set curses to not wait for input when calling getch()
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit.")

    while True:
        # Take screenshot and get the filename
        screenshot_filename = take_screenshot(index)

        # Update the screen output, clearing previous lines
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")
        stdscr.addstr(1, 0, f"Screenshot {index} saved as: {screenshot_filename}")
        stdscr.refresh()

        index += 1
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
