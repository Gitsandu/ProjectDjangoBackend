from Application.Dto.APIResponse.APIResponse import APIResponse
from typing import Any

class APIResponseHelper:
    _api_response_helper = None

    @staticmethod
    def get_instance():
        if APIResponseHelper._api_response_helper is None:
            APIResponseHelper._api_response_helper = APIResponseHelper()
        return APIResponseHelper._api_response_helper

    def convert_to_api_response(self, response: Any, message: str = None, total_pages: int = 0, total_count: int = 0) -> APIResponse:
        return APIResponse(
            data=response,
            message= 'Success',
            total_pages=total_pages,
            total_count=total_count,
            status_code= 200 if message != "Success" else 404
        )