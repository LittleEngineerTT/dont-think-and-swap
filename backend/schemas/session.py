from schemas.user import User
from uuid import uuid4

class SessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.session_ids = []
        self.users = {}

    def create_session(self):
        session_id = uuid4().hex
        self.session_ids.append(session_id)
        self.users[session_id] = {}
        self.users[session_id]["users"] = []
        self.users[session_id]["total_users"] = 0
        return True
    
    def remove_session(self, session_id):
        self.session_ids.remove(session_id)
        self.users.pop(session_id)
        return True

    def add_participant(self, session_id, user: User):
        if session_id not in self.session_ids:
            return False
        self.users[session_id]["users"].append(user)
        self.users[session_id]["total_users"] += 1
        return True

    def remove_participant(self, session_id: str, user: User):
        self.users[session_id]["users"].remove(user)
        return True

# Global instance of the session manager
session_manager = SessionManager()
