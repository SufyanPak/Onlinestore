from typing import Optional
from fastapi import FastAPI, Depends, HTTPException

from sqlmodel import Fields, Session, SQLModel, create_engine

class site_user(SQLModel, table=True):
    id: Optional[int] = Fields(default=None, primary_key=True)
    name: str
    email: str
    phone_no: int
    