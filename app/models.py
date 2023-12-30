from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False,unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    Category_ID = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__=="__main__":
    from app import app 
    with app.app_context():
        # c1 = Category(name="Iphone")
        # c2 = Category(name="tablet")
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        ##########################
        # p1 = Product(name="IPhone15 Pro Max", price=10000000, Category_ID=2, image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p2 = Product(name="IPhone12 Pro Max", price=20000000, Category_ID=2, image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p3 = Product(name="IPhone13 Pro Max", price=30000000, Category_ID=2,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")

        # db.session.add_all([p1, p2, p3,])
        # db.session.commit()
        #######
        db.create_all()