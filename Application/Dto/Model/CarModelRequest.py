from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class CarModelRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, Brand: int, Model_name: str):
        super().__init__(id, is_deleted, is_active)
        self.Model_name = Model_name
        self.Brand = Brand