# ai_tutor_project/auth_manager.py
import bcrypt
from database import SessionLocal, User

class AuthManager:
    @staticmethod
    def login(email: str, password: str) -> bool:
        db = SessionLocal()
        user = db.query(User).filter(User.email == email).first()
        if user and bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
            return True
        return False

    @staticmethod
    def invite_only_signup(email: str, invite_code: str) -> bool:
        # implement invite code validation
        pass
