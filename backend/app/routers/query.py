from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class QueryResp(BaseModel):
    answer: str
    sources: List[dict]

@router.get("/")
async def query(q: str):
    # PoC: return canned response
    return QueryResp(
        answer=f"This is a stubbed answer to: {q}",
        sources=[{"doc": "example.pdf", "page": 1}]
    )
