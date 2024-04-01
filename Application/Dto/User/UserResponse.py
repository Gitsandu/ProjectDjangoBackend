from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class UserResponse(AuditableResponse):
    def __init__(self, id: int, is_deleted: bool, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_active: bool,
                 first_name: str, last_name: str, age: int, phone_number: str, email: str, address: str):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.phone_number = phone_number
        self.email = email
        self.address = address
