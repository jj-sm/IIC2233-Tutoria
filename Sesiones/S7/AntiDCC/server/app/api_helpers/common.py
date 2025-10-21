from fastapi import APIRouter, Depends
from typing import List, Dict, Any

def add_welcome_endpoint(
        router: APIRouter, *, summary: str, description: str,
        tags: List[str], skip_paths: List[str] = None) -> None:
    """Attach a '/' welcome endpoint to the router that lists its routes."""
    skip_paths = set(skip_paths or ["/"])

    @router.get(
        "/",
        summary=summary,
        description=description,
        tags=tags,
        responses={
            200: {
                "description": "List of available endpoints",
                "content": {
                    "application/json": {
                        "example": {
                            "endpoints": [
                                "/search/endpoint1 [GET]",
                                "/search/endpoint2 [GET]"
                            ]
                        }
                    }
                }
            }
        },
    )
    def welcome() -> Dict[str, Any]:
        endpoints = []
        for r in router.routes:
            if r.path in skip_paths:
                continue
            methods = ",".join(r.methods) if r.methods else "GET"
            endpoints.append(f"{r.path} [{methods}]")
        return {"endpoints": endpoints}
