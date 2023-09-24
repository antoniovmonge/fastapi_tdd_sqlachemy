import asyncio
import csv
from datetime import datetime
from sqlalchemy import select, delete
from src.database import SessionLocal
from src.models import Product, Customer, ProductReview


async def main():
    async with SessionLocal() as session:
        async with session.begin():
            await session.execute(delete(ProductReview))

    async with SessionLocal() as session:
        async with session.begin():
            with open("data/reviews.csv") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    c = await session.scalar(
                        select(Customer).where(Customer.name == row["customer"])
                    )
                    p = await session.scalar(
                        select(Product).where(Product.name == row["product"])
                    )
                    r = ProductReview(
                        customer=c,
                        product=p,
                        timestamp=datetime.strptime(
                            row["timestamp"], "%Y-%m-%d %H:%M:%S"
                        ),
                        rating=int(row["rating"]),
                        comment=row["comment"] or None,
                    )
                    session.add(r)


if __name__ == "__main__":
    asyncio.run(main())
