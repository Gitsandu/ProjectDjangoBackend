from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class CarVariantResponse(AuditableResponse):
    def __init__(self, id: int, is_deleted: bool, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_active: bool,
                 Model_Id: int, Variant_Name: str, Fuel_Type: str, Launch_Year: int, Transmission: str):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.Model_Id = Model_Id
        self.Variant_Name = Variant_Name
        self.Fuel_Type = Fuel_Type
        self.Launch_Year = Launch_Year
        self.Transmission = Transmission
