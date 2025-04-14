import hashlib
import os


def hash_password(password: str) -> str:
    """
    Hashes a password using PBKDF2 with SHA-256 and returns a string that includes both
    the salt and the hash. The salt and hash are separated by a colon.
    """
    salt = os.urandom(16)  # Create a 16-byte salt (yes this is necessary just leave it)
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256",  # Using sha256 as the algorithm
        password.encode("utf-8"),  # Password -> bytes
        salt,  # Provide the salt
        100000,  # This is the recommended number of iterations, crazy!
    )
    return salt.hex() + ":" + hashed_password.hex()


def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verifies a provided password against the stored hash.

    Args:
        stored_password: A string containing the salt and hash separated by a colon.
        provided_password: The password string to verify.

    Returns:
        True if the `provided_password` matches the `stored_password`, otherwise False.
    """
    salt_hex, hash_hex = stored_password.split(":")
    salt = bytes.fromhex(salt_hex)
    new_hash = hashlib.pbkdf2_hmac("sha256", provided_password.encode("utf-8"), salt, 100000)
    return new_hash.hex() == hash_hex


# HERES AN EXAMPLE
if __name__ == "__main__":
    plain_password = "my_secure_password"
    hashed = hash_password(plain_password)
    print("Stored hash:", hashed)
    print("Verification:", verify_password(hashed, "my_secure_password"))  # Should output True
