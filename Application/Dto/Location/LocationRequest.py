from Application.Dto.Auditable.AuditableRequest import AuditableRequest

class LocationRequest(AuditableRequest):
    def __init__(self, id: int, city_name:str, pin_code: str, state:str):
        super().__init__(id)
        self.city_name = city_name
        self.pin_code = pin_code
        self.state = state 