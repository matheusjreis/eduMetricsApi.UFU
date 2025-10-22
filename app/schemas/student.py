from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    full_name: str = Field(..., max_length=255)
    email: EmailStr | None = None


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int

    model_config = {"from_attributes": True}
