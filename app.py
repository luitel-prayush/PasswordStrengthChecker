from flask import Flask, render_template, request

import re
import math
import hashlib
import requests
import secrets
import string

app = Flask(__name__)

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

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_knownBreaches(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def generate_strong_password(length=16):
    if length < 12:
        raise ValueError("Password length should be at least 12 for security.")

    # Character sets
    lowercase = 'abcdefghjkmnpqrstuvwxyz'  # removed: i, l
    uppercase = 'ABCDEFGHJKMNPQRSTUVWXYZ'  # removed: I, O
    digits = '23456789'                   # removed: 0, 1
    symbols = '!@#$%^&*()-_=+[]{};:,.<>?'

    # Make sure we have at least one of each
    required = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Combined allowed characters (excluding similar ones)
    all_allowed = lowercase + uppercase + digits + symbols

    # Fill the rest of the password
    remaining = [secrets.choice(all_allowed) for _ in range(length - len(required))]

    # Mix it all up
    full_password = required + remaining
    secrets.SystemRandom().shuffle(full_password)

    return ''.join(full_password)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    suggested_password = None

    if request.method == "POST":
        if "generate" in request.form:
            try:
                length = int(request.form.get("length", 16))
                suggested_password = generate_strong_password(length)
            except Exception as e:
                suggested_password = f"Error: {str(e)}"
        else:
            password = request.form.get("password")
            strong, issues = check_password_strength(password)
            entropy = calculate_entropy(password)
            pwned_count = check_knownBreaches(password)
            result = {
                "password": password,
                "strong": strong,
                "issues": issues,
                "entropy": entropy,
                "pwned_count": pwned_count
            }

    return render_template("index.html", result=result, suggested_password=suggested_password)

if __name__ == "__main__":
    app.run(debug=True)