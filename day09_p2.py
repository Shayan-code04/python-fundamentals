
"""
Read a file with retry logic and custom exception handling.
"""


class FileRetryExceededError(Exception):
    """Raised when all retry attempts to read a file have been exhausted."""
    pass


def read_file_with_retry(filepath, max_retries=3):
    """
    Attempts to read a file.

    Parameters:
        filepath (str): Initial file path.
        max_retries (int): Maximum number of attempts.

    Returns:
        str: Contents of the file.

    Raises:
        FileRetryExceededError: If all retry attempts fail due to
                                FileNotFoundError.
    """

    current_path = filepath

    for attempt in range(1, max_retries + 1):
        try:
            with open(current_path, "r") as file:
                return file.read()

        except FileNotFoundError:
            print(f"File not found: {current_path}")

            if attempt == max_retries:
                raise FileRetryExceededError(
                    f"Failed to open '{current_path}' after {attempt} attempts."
                )

            current_path = input("Enter a new file path: ")

        except PermissionError:
            print("Permission denied. You don't have access to this file.")
            raise

        except IsADirectoryError:
            print("The given path is a directory, not a file.")
            raise

        finally:
            print(f"Attempt {attempt} finished")


if __name__ == "__main__":
    try:
        path = input("Enter file path: ")
        content = read_file_with_retry(path)

        print("\nFile contents:")
        print(content)

    except FileRetryExceededError as e:
        print(f"\nFailed: {e}")

    except PermissionError:
        print("\nOperation aborted due to insufficient permissions.")

    except IsADirectoryError:
        print("\nOperation aborted because a directory was provided instead of a file.")