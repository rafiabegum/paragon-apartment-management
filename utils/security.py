# Rafia Begum
# 24043914

import hashlib


class Security:

    @staticmethod
    def hash_password(password):
        """
        Converts a plain-text password into a SHA-256 hash.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        """
        Verifies whether the entered password matches the stored hash.
        """
        return hashlib.sha256(password.encode()).hexdigest() == hashed_password


if __name__ == "__main__":

    password = "admin123"

    hashed = Security.hash_password(password)

    print("Original Password :", password)
    print("Hashed Password   :", hashed)

    if Security.verify_password(password, hashed):
        print("Password Verified Successfully")
    else:
        print("Password Verification Failed")