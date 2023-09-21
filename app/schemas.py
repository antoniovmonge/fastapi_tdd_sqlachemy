from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    year: int
    cpu: str | None = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
