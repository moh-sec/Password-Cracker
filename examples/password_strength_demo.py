import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
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


if __name__ == "__main__":
    password = input("Enter a password to test: ")
    score = check_password_strength(password)
    print("Password strength:", strength_label(score))
