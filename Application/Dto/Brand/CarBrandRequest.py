from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class CarBrandRequest(AuditableRequest):
    def __init__(self, id: int, is_deleted: bool, is_active: bool, Brandname: str):
        super().__init__(id, is_deleted, is_active)
        self.Brandname = Brandname