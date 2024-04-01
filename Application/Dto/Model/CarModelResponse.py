from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class CarModelResponse(AuditableResponse):
    def __init__(self, id: int, is_deleted: bool, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_active: bool,
                 Brand: int, Model_name: str):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.Model_name = Model_name
        self.Brand = Brand
