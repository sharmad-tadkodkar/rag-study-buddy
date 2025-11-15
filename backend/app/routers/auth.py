from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class UserIn(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(u: UserIn):
    # PoC: no DB, return stub
    return {"email": u.email, "msg": "signup stubbed in PoC"}

@router.post("/login")
async def login(u: UserIn):
    # PoC: return fake token
    return {"access_token": "fake-token", "token_type": "bearer"}
