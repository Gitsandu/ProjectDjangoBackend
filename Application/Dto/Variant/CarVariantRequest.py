from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class CarVariantRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, Model_Id: int, Variant_Name: str, Fuel_Type: str, Launch_Year: int, Transmission: str):
        super().__init__(id, is_deleted, is_active)
        self.Model_Id = Model_Id
        self.Variant_Name = Variant_Name
        self.Fuel_Type = Fuel_Type
        self.Launch_Year = Launch_Year
        self.Transmission = Transmission
