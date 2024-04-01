from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class CarDetailsResponse(AuditableResponse):
    def __init__(self, id: int, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_deleted: bool, is_active: bool, Location: str, Brand_Name: str,Model_Name: str, Variant_Name: str, MFD_Year: int, KiloMeter: str, Ownership: str, When_ToSell: str, User: int, FuelType: str, Transmission: str):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.Location = Location
        self.Brand_Name = Brand_Name
        self.Model_Name = Model_Name
        self.Variant_Name = Variant_Name
        self.MFD_Year = MFD_Year 
        self.KiloMeter = KiloMeter
        self.Ownership = Ownership
        self.When_ToSell = When_ToSell
        self.User = User
        self.FuelType = FuelType
        self.Transmission = Transmission
        
        
        
    