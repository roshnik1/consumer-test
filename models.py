from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric

from app import db

class Households(db.Model):
    __tablename__ = '400_households'
    HSHD_NUM = Column(Integer, primary_key=True)
    L = Column(Boolean)
    AGE_RANGE = Column(String(5))
    MARITAL = Column(String(10))
    INCOME_RANGE = Column(String(10))
    HOMEOWNER = Column(String(10))
    HSHD_COMPOSITION = Column(String(25))
    HH_SIZE = Column(String(5))
    CHILDREN = Column(String(5))
    def __str__(self):
        return self.HSHD_NUM

class Products(db.Model):
    __tablename__ = '400_products'
    PRODUCT_NUM = Column(Integer, primary_key=True)
    DEPARTMENT = Column(String(10))
    COMMODITY = Column(String(25))
    BRAND_TY = Column(String(10))
    NATURAL_ORGANIC_FLAG = Column(String(1))

class Transactions(db.Model):
    __tablename__ = '400_transactions'
    BASKET_NUM = Column(Integer)
    HSHD_NUM = Column(Integer, primary_key=True)
    PURCHASE = Column(Date)
    PRODUCT_NUM = Column(Integer, primary_key=True)
    SPEND = Column(Numeric)
    UNITS = Column(Integer)
    STORE_R = Column(String(10))
    WEEK_NUM = Column(Integer)
    YEAR = Column(Integer)