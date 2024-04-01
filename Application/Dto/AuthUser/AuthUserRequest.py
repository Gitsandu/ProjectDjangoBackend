from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class AuthUserRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, username: str,phone_number: str, email: str, password: str):
        super().__init__(id, is_deleted, is_active)
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.password = password