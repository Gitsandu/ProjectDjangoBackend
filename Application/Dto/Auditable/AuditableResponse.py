from datetime import date
import uuid

class AuditableResponse:
    def __init__(self, id: int, is_deleted: bool, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_active:bool):
        self.id = id
        self.is_deleted = is_deleted
        self.created_by = created_by
        self.updated_by = updated_by
        self.created_date = created_date
        self.updated_date = updated_date
        self.is_active = is_active
