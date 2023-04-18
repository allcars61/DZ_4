
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base =declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))
    publisher = relationship('Publisher', backref='books')

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)
    book = relationship('Book', backref='stocks')
    shop = relationship('Shop', backref='stocks')

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer)
    stock = relationship('Stock', backref='sales')

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    stocks = relationship('Stock', backref='shop')

def create_tables(engine):
    Base.metadata.create_all(engine)


DSN = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.commit()





