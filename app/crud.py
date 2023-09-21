from sqlalchemy.orm import Session


from app import models, schemas


async def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
