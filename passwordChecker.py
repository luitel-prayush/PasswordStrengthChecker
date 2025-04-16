import re

def check_password_strength(password):
    length_err = len(password) < 12
    num_err = re.search(r"\d", password) is None
    uppercase_err = re.search(r"[A-Z]", password) is None
    lowercase_err = re.search(r"[a-z]", password) is None
    symbol_err = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Password length is less than 12': length_err,
        'Missing a number': num_err,
        'Missing uppercase': uppercase_err,
        'Missing lowercase': lowercase_err,
        'Missing symbol !@#$%^&*(),.?\":{}|<>': symbol_err
    }

    validPassword = not any(errors.values())

    return validPassword, errors

pwd = input("Enter your password: ")
valid, errors = check_password_strength(pwd)

if valid:
    print("✅ Your password is strong!")
else:
    print("❌ Weak password:")
    for err, failed in errors.items():
        if failed:
            print(f" - {err}")