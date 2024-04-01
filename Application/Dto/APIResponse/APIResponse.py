class APIResponse:
    def __init__(self, status_code:int, data:object, message:str = '', total_pages:int = 0, total_count:int = 0):
        self.status_code = status_code
        self.data = data
        self.message =  message
        self.totalPages = total_pages
        self.totalCount = total_count

    def to_dict(self):
        return {
            'status_code': self.status_code,
            'data': self.data,
            'message': self.message,
            'total_pages': self.totalPages,
            'total_count': self.totalCount
        }                
