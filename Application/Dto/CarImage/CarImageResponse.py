from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class CarImageResponse(AuditableResponse):
    def __init__(self , id: int, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_deleted: bool, is_active: bool, Image: str, OverView: int):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.Image = Image
        self.OverView = OverView
