from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

def error_responses(message: str, code: int):
    return{
        "success": False,
        "error": message,
        "code": code
    }

def register_exception_handlers(app):


    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=error_responses(exc.detail, exc.status_code)
        )
    
    @app.excetion_handler(Exception)
    async def global_exception_handler(request: Request,exc: Exception):
        return JSONResponse(
            status_code=500,
            content=error_responses("Internal server Error", 500)
        )