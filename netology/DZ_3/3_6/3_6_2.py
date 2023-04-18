import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, aliased

from models import Publisher, Book, Stock, Sale, Shop

DSN = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

publisher_id = input("Введите идентификатор издателя: ")

publisher = session.query(Publisher).filter(Publisher.id==publisher_id).one()

alias_stock = aliased(Stock)
alias_sale = aliased(Sale)
sales = session.query(Book.title, Shop.name, alias_sale.price, alias_sale.date_sale).\
    join(alias_stock).\
    join(Shop).\
    join(alias_sale).\
    filter(Book.id_publisher==publisher.id)

for sale in sales:
    print(sale[0], sale[1], sale[2], sale[3])