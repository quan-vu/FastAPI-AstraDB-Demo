from typing import List
from fastapi import FastAPI

from cassandra.cqlengine.management import sync_table
from . import (
    db,
    config,
    crud,
    models,
    schema,
)

settings = config.get_settings()
Product = models.Product

app = FastAPI()

session = None

@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(Product)


@app.get("/")
def read_index():
    return {"hello": "world", "name": settings.name}


@app.get("/products", response_model=List[schema.ProductListSchema])
def products_list_view():
    return list(Product.objects.all())


@app.post("/products")
def products_create_view(data: schema.ProductSchema):
    product = crud.create_entry(data.dict())
    return product
