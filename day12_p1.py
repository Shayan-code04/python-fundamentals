"""
Day 12 - Log Generator

Topics:
- os
- datetime
- random
- File Handling
- Functions
"""

import os
import random
from datetime import datetime


def create_log_entry():
    """Creates a log file with timestamp, random status, and log count."""

    # Folder where logs will be stored
    log_folder = "logs"

    # Create the folder if it doesn't exist
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    # Current date and time
    current_time = datetime.now()

    # Timestamp for inside the file
    readable_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Filename-safe timestamp
    filename_timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Random status
    status_tags = [
        "SUCCESS",
        "FAILED",
        "WARNING",
        "INFO"
    ]

    status = random.choice(status_tags)

    # Count existing log files
    existing_logs = len(os.listdir(log_folder))

    # Create filename
    filename = f"{filename_timestamp}.txt"

    # Full path to the file
    file_path = os.path.join(log_folder, filename)

    # Write log information
    with open(file_path, "w") as file:
        file.write("===== LOG ENTRY =====\n")
        file.write(f"Timestamp     : {readable_timestamp}\n")
        file.write(f"Status        : {status}\n")
        file.write(f"Existing Logs : {existing_logs}\n")

    print(f"Log created successfully!")
    print(f"Location : {file_path}")


if __name__ == "__main__":
    create_log_entry()