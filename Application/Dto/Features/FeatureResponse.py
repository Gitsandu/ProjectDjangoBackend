from Application.Dto.Auditable.AuditableResponse import AuditableResponse
import uuid
from datetime import date

class FeatureResponse(AuditableResponse):
    def __init__(self, id: int, created_by: uuid.UUID, updated_by: uuid.UUID, created_date: date, updated_date: date, is_deleted: bool, is_active: bool, POWER_STEERING: bool, POWER_WINDOWS_FRONT: bool, AIR_CONDITIONER: bool, HEATER: bool, ADJUSTABLE_HEAD_LIGHTS: bool, FOG_LIGHTS_FRONT: bool, ANTI_LOCK_BRAKING_SYSTEM: bool, CENTRAL_LOCKING: bool, RADIO: bool, Entertainment_communication: dict, Safety: dict, Exterior:dict, Interior: dict, Comfort_convenience: dict, OverView: int):
        super().__init__(id, is_deleted, created_by, updated_by, created_date, updated_date, is_active)
        self.POWER_STEERING = POWER_STEERING
        self.POWER_WINDOWS_FRONT = POWER_WINDOWS_FRONT
        self.AIR_CONDITIONER = AIR_CONDITIONER
        self.HEATER = HEATER
        self.ADJUSTABLE_HEAD_LIGHTS = ADJUSTABLE_HEAD_LIGHTS
        self.FOG_LIGHTS_FRONT = FOG_LIGHTS_FRONT
        self.ANTI_LOCK_BRAKING_SYSTEM = ANTI_LOCK_BRAKING_SYSTEM
        self.CENTRAL_LOCKING = CENTRAL_LOCKING
        self.RADIO = RADIO
        self.Entertainment_communication = Entertainment_communication
        self.Safety = Safety 
        self.Exterior = Exterior
        self.Interior = Interior
        self.Comfort_convenience = Comfort_convenience
        self.OverView = OverView


    
        
        
    