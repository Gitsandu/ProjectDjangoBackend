class AuditableRequest:
    def __init__(self, id:int, is_deleted:bool, is_active:bool):
        self.id = id
        self.is_deleted = is_deleted
        self.is_active = is_active
