from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class UserRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, first_name: str, last_name: str, age: int, phone_number: str, email: str, address: str):
        super().__init__(id, is_deleted, is_active)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.phone_number = phone_number
        self.email = email
        self.address = address