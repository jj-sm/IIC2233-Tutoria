from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from starlette.requests import Request
from .routers import (iic)
# from .logging_middleware import RequestLoggerMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

URL_PREFIX = os.getenv("URL_PREFIX", "").rstrip("/")
app = FastAPI(title="IIC API", version="1.0.0")
app.root_path = URL_PREFIX
# app.add_middleware(RequestLoggerMiddleware)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid request data"},
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="API Helper for asynchronous tasks",
        routes=app.routes,
    )

    # Add custom 403 response and remove 422
    for path in openapi_schema["paths"].values():
        for method in path.values():
            responses = method.get("responses", {})

            # Remove 422 if exists
            responses.pop("422", None)

            # Add custom 403
            responses["403"] = {
                "description": "Not authorized - missing or invalid API key",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid or inactive API Key"}
                    }
                },
            }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Routers
app.include_router(iic.router, prefix="/iic", tags=["iic"], include_in_schema=True)
# app.include_router(navaids.router, prefix="/navaids", tags=["Navaids"], include_in_schema=True)
# app.include_router(procedures.router, prefix="/procedures", tags=["Procedures"],
#                    include_in_schema=True)
# app.include_router(airports.router, prefix="/airports", tags=["Airports"], include_in_schema=True)
# app.include_router(airspace.router, prefix="/airspace", tags=["Airspace"], include_in_schema=True)
# app.include_router(maps.router, prefix="/html/maps", tags=["Maps"], include_in_schema=True)
# app.include_router(maps_view.router, prefix="/viewer/maps", tags=["Maps Viewer"],
#                    include_in_schema=True)
# app.include_router(enroute.router, prefix="/enroute", tags=["Enroute"], include_in_schema=True)
# app.include_router(poly_search.router, prefix="/poly_search", tags=["Polygon Search"],
#                    include_in_schema=True)
# app.include_router(sectorfile.router, prefix="/sectorfile", tags=["Sectorfile"],
#                    include_in_schema=True)
