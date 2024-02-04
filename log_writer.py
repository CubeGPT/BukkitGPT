import os
import datetime

def logger(text):
    # Get the current timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%b-%d-%Y-%H-%M-%S")  # Format: SS-MinuteMinute-HH-DD-MonthMonth-YYYY

    # Create the logs folder if it doesn't exist
    logs_folder = "logs"
    os.makedirs(logs_folder, exist_ok=True)

    # Create or append to the log file
    log_file_path = os.path.join(logs_folder, f"{timestamp}.log")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"[{now.strftime('%H:%M:%S')}] {text}\n")