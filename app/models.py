from sqlalchemy import Column, Integer, String,Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app import db
from flask_login import  UserMixin
import enum


class UserRoleEnum(enum.Enum):
    USER=1
    ADMIN=2


#UserMixin để nó hiều đây là model dùng để chứng thực-> vì Python da kế thừa
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), default='https://th.bing.com/th/id/OIP.48Pj-NVeziMTgdX6rHGpKAHaI1?w=162&h=194&c=7&r=0&o=5&dpr=1.1&pid=1.7')
    user_role = Column(Enum(UserRoleEnum),default=UserRoleEnum.USER)
    receipts = relationship('Receipt',backref='user',lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False,unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return  self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    Category_ID = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)

class BaseModel (db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime)
    active = Column(Boolean, default=True)


class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)



if __name__=="__main__":
    from app import app 
    with app.app_context():
        db.create_all()

        # import hashlib
        # u = User(name='Admin',
        #          username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN
        #          )
        # db.session.add(u)
        # db.session.commit()
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
        # p4 = Product(name="IPhone16 Pro Max", price=40000000, Category_ID=1,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p5 = Product(name="IPhone19 Pro Max", price=90000000, Category_ID=1,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p6 = Product(name="Samsung", price=10000000, Category_ID=2, image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p7 = Product(name="Oppo Pro Max", price=20000000, Category_ID=2, image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p8 = Product(name="realme Pro Max", price=30000000, Category_ID=2,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p9 = Product(name="Oppo 2", price=40000000, Category_ID=1,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # p10 = Product(name="Samsung2 Pro Max", price=90000000, Category_ID=1,  image= "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg")
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.add_all([p6, p7, p8, p9, p10])
        # db.session.commit()
        #######
