import hashlib
import secrets
import sqlite3
from pathlib import Path
from typing import Optional, Tuple

class SecureLoginSystem:
    def __init__(self, db_path: str = "users.db"):
        """Initialize login system with SQLite database"""
        self.db_path = Path(db_path)
        self._init_database()

    def _init_database(self) -> None:
        """Create users table with hashed passwords and salts"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def _hash_password(self, password: str, salt: Optional[str] = None) -> Tuple[str, str]:
        """
        Hash password using SHA-256 with random salt
        Returns (hash, salt) tuple
        """
        if not salt:
            salt = secrets.token_hex(16)  # Generate random salt
        
        # Combine password and salt, then hash
        hash_input = (password + salt).encode('utf-8')
        password_hash = hashlib.sha256(hash_input).hexdigest()
        
        return password_hash, salt

    def register(self, username: str, password: str) -> bool:
        """Register new user with hashed password"""
        if not username or not password:
            return False

        try:
            password_hash, salt = self._hash_password(password)
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                    (username, password_hash, salt)
                )
            return True
        except sqlite3.IntegrityError:
            return False  # Username already exists

    def login(self, username: str, password: str) -> bool:
        """Verify login credentials using secure comparison"""
        if not username or not password:
            return False

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "SELECT password_hash, salt FROM users WHERE username = ?",
                    (username,)
                )
                result = cursor.fetchone()
                
                if not result:
                    return False
                
                stored_hash, salt = result
                test_hash, _ = self._hash_password(password, salt)
                
                # Use constant-time comparison
                return secrets.compare_digest(test_hash, stored_hash)
                
        except Exception:
            return False

# Example usage
def main():
    login_system = SecureLoginSystem()
    
    # Registration
    print("Register new user:")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if login_system.register(username, password):
        print("Registration successful!")
    else:
        print("Registration failed!")

    # Login
    print("\nLogin:")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if login_system.login(username, password):
        print("Login successful!")
    else:
        print("Invalid credentials!")

if __name__ == "__main__":
    main()