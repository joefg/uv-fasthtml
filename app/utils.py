from email.utils import parseaddr
import hashlib


def hash_password(password: str, salt: str):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
    ).hex()


def is_valid_email(email_address: str):
    parsed = parseaddr(email_address)
    if "@" in parsed[1]:
        return True
    return False
