from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class IndexCreate(BaseModel):
    name: str

INDEXES = []

@router.post("/")
async def create_index(payload: IndexCreate):
    idx = {"id": len(INDEXES)+1, "name": payload.name}
    INDEXES.append(idx)
    return idx

@router.get("/", response_model=List[dict])
async def list_indexes():
    return INDEXES
