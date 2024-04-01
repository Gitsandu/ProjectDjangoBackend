from Application.Dto.APIResponse.APIResponse import APIResponse

class EntityResponseModel:
    def __init__(self, EntityResponse:object, APIResponse: APIResponse):
        self.EntityResponse = EntityResponse
        self.APIResponse = APIResponse
        