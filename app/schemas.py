from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50,
                      description="Nombre del producto")
    description: str | None = Field(
        None, max_length=200, description="Descripción opcional")
    price: float = Field(..., ge=0,
                         description="El precio debe ser mayor o igual a cero")


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    model_config = {"from_attributes": True}  # reemplaza class Config
