# Defending Against Password Attacks

Defending against password attacks isn’t about a single feature. It’s the result of combining good password practices with proper system-level protections.

## Strong Passwords
Strong passwords are long, unique, and hard to guess. Using random combinations of letters, numbers, and symbols is far more effective than relying on real words or personal information.

## Password Hashing
Passwords should never be stored in plain text. Secure systems use hashing algorithms designed specifically for passwords, making it much harder for attackers to recover the original values even if a database is leaked.

## Salting
Salts add random data to each password before hashing. This prevents attackers from using precomputed tables, such as rainbow tables, and forces them to attack each password individually.

## Rate Limiting
Rate limiting reduces the impact of brute force attacks by restricting how many login attempts are allowed in a given time window. In many cases, it can stop automated attacks entirely.

## Multi-Factor Authentication
Multi-factor authentication adds an extra layer of protection. Even if a password is compromised, a second factor like a one-time code or hardware key can prevent unauthorized access.

## User Awareness
User behavior is often the weakest link. Teaching users about phishing, password reuse, and basic security hygiene can significantly reduce real-world attack success.

Effective security comes from multiple defenses working together, not from relying on passwords alone.
