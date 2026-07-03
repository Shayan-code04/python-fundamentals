from datetime import datetime


def write_log_entry(filepath, message):
    """
    Append a timestamped log entry to a log file.

    Parameters:
        filepath (str): path to the log file.
        message (str): the log message to record.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def read_log(filepath):
    """
    Read and return all log entries from a log file.

    Parameters:
        filepath (str): path to the log file.

    Returns:
        list of str: each log line, without trailing newline.
    """
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]


def print_log(entries):
    """
    Print log entries one per line.

    Parameters:
        entries (list of str): log entries to print.
    """
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    filepath = "activity.log"

    write_log_entry(filepath, "Program started")
    write_log_entry(filepath, "Student records processed")
    write_log_entry(filepath, "Program finished")

    entries = read_log(filepath)
    print_log(entries)