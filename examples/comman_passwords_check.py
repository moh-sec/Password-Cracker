import re
import os
import math
import requests

# Most common passwords list 
URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
OUTPUT_PATH = "data/common_passwords.txt"


def download_password_list(url=URL, output_path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)


def load_common_passwords(file_path=OUTPUT_PATH):
    if not os.path.exists(file_path):
        print("Common passwords file not found. Downloading now...")
        download_password_list()

    with open(file_path, "r", encoding="utf-8") as file:
        passwords = {line.strip().lower() for line in file if line.strip()}

    return passwords


def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1

    return score


def strength_label(score):
    if score <= 2:
        return "Very Weak"
    elif score <= 4:
        return "Weak"
    elif score == 5:
        return "Moderate"
    else:
        return "Strong"


def calculate_entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"[0-9]", password):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)


def entropy_label(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 35:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    else:
        return "Strong"


def has_repetition(password):
    # Reject if 3 same chars in a row
    return re.search(r"(.)\1\1", password) is not None


def has_sequence(password):
    # Reject if sequence of 4 increasing chars (1234, abcd)
    password_lower = password.lower()

    for i in range(len(password_lower) - 3):
        segment = password_lower[i:i+4]
        if segment.isalpha() or segment.isdigit():
            if all(ord(segment[j]) + 1 == ord(segment[j+1]) for j in range(3)):
                return True
    return False


def composition_check(password):
    groups = 0
    if re.search(r"[a-z]", password): groups += 1
    if re.search(r"[A-Z]", password): groups += 1
    if re.search(r"[0-9]", password): groups += 1
    if re.search(r"[^a-zA-Z0-9]", password): groups += 1
    return groups


if __name__ == "__main__":
    common_passwords = load_common_passwords()

    while True:
        password = input("Enter a password: ")

        # 1) common password check
        if password.lower() in common_passwords:
            print("Password rejected: This password is too common.")
            continue

        # 2) Basic checks
        if len(password) < 12:
            print("Password rejected: Password must be at least 12 characters.")
            continue

        if composition_check(password) < 3:
            print("Password rejected: Password must include at least 3 of the following: lowercase, uppercase, numbers, symbols.")
            continue

        if has_repetition(password):
            print("Password rejected: Password contains repeated characters.")
            continue

        if has_sequence(password):
            print("Password rejected: Password contains a sequential pattern.")
            continue

        # 3) score + entropy
        score = check_password_strength(password)
        entropy = calculate_entropy(password)

        if score < 5 or entropy < 50:
            print("Password rejected.")
            print(f"- Score: {score} ({strength_label(score)})")
            print(f"- Entropy: {round(entropy, 2)} ({entropy_label(entropy)})")
            continue

        print("Password accepted.")
        print(f"- Score: {score} ({strength_label(score)})")
        print(f"- Entropy: {round(entropy, 2)} ({entropy_label(entropy)})")

        print("You can enter another password if you want.\n")
