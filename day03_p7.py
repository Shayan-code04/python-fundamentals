def palindrome_checker(*args):
    """Check multiple strings at once and return a dict of results."""
    results = {}
    for text in args:
        normalized = ''.join(ch.lower() for ch in str(text) if ch.isalnum())
        results[text] = normalized == normalized[::-1]
    return results


if __name__ == '__main__':
    samples = [
        'Level',
        'hello',
        'A man, a plan, a canal, Panama',
        '12321',
        'Not a palindrome'
    ]
    for text, is_palindrome in palindrome_checker(*samples).items():
        print(f'{text!r}: {is_palindrome}')
