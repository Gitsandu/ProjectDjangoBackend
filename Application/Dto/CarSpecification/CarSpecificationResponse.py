from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class CarSpecificationResponse(AuditableResponse):
    def __init__(self, id: int, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_deleted: bool, is_active: bool, engine: str, max_power: str, torque: str, mileage:str, seats: str, wheel: str, engine_and_transmission:dict, dimensions_and_capacity: dict, miscellaneous: dict, OverView: int):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.mileage =  mileage
        self.engine = engine
        self.max_power = max_power
        self.torque = torque
        self.seats = seats
        self.wheel = wheel
        self.engine_and_transmission = engine_and_transmission
        self.dimensions_and_capacity = dimensions_and_capacity
        self.miscellaneous = miscellaneous
        self.OverView = OverView
        
    