from fastapi import HTTPException

class APIError(HTTPException):
    def __init__(self, status_code, detail = str):
        super().__init__(status_code, detail)