import random
import time
import os
from fastapi import APIRouter, FastAPI, Body
from ..api_helpers.common import add_welcome_endpoint
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Votes Generator API")

class VoteRequest(BaseModel):
    candidate_ids: List[str]
    interval: int = 5

load_dotenv()
HIDE_ADMIN_ENDPOINTS = os.getenv("DEBUG", "0") == "1"

router = APIRouter()

add_welcome_endpoint(router,
                     summary="IIC Simulation endpoints",
                     description="This route lists the available admin endpoints.",
                     tags=["iic"])

@router.post(
    "/votes",
    summary="Votes generator",
    description="Generates random votes for each candidate every `interval` seconds",
    responses={
        200: {
            "description": "Random generation of votes between candidates",
            "content": {
                "application/json": {
                    "example": {
                        "votes": {"candidate_1": 3, "candidate_2": 7}
                    }
                }
            }
        },
    },
)
def generate_votes(data: VoteRequest = Body(...)):
    candidate_ids = data.candidate_ids
    interval = data.interval

    # Simulate waiting for "interval" seconds
    time.sleep(interval)

    # Generate random votes for each candidate
    votes = {cid: random.randint(0, 10) for cid in candidate_ids}

    return JSONResponse(content={"votes": votes})