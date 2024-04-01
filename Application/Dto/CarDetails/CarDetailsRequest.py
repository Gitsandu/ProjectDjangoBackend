from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class CarDetailsRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, Location: str, Brand_Name: str,Model_Name: str, Variant_Name: str, MFD_Year: int, KiloMeter: str, Ownership: str, When_ToSell: str, User: int, FuelType: str, Transmission: str):
        super().__init__(id, is_deleted, is_active)
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
        
        
        
    