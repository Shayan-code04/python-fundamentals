# day06_p3.py

def validate_email(email):
    
    email = email.strip()

    if "@" not in email:
        return {"valid": False, "reason": "Missing @ symbol"}

    parts = email.split("@")

    if len(parts) != 2:
        return {"valid": False, "reason": "Multiple @ symbols found"}

    local, domain = parts[0], parts[1]

    if len(local) == 0:
        return {"valid": False, "reason": "Nothing before @"}

    if "." not in domain:
        return {"valid": False, "reason": "Domain missing a dot (e.g. gmail.com)"}

    if domain.startswith(".") or domain.endswith("."):
        return {"valid": False, "reason": "Domain cannot start or end with a dot"}

    if local.startswith(".") or local.startswith("-"):
        return {"valid": False, "reason": "Local part cannot start with dot or hyphen"}

    return {"valid": True, "reason": "Email looks valid"}


def main():
    while True:
        email = input("Enter email to validate (or 'quit' to exit): ").strip()
        if email.lower() == "quit":
            break

        result = validate_email(email)
        status = " Valid" if result["valid"] else " Invalid"
        print(f"{status} — {result['reason']}\n")


if __name__ == "__main__":
    main()