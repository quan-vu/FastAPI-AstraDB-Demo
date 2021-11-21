from .models import Product


def create_entry(data:dict):
    if not isinstance(data, dict):
        raise Exception('Input data must a dict')
    return Product.create(**data)
