from pydantic import BaseModel


class DesafiadosBase(BaseModel):
    name: str
    email: str
    cargo: str


class DesafiadosRequest(DesafiadosBase):
    ...


class DesafiadosResponse(DesafiadosBase):
    id: int

    class Config:
        orm_mode = True
