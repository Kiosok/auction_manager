"""Извлекает данные из базы данных"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint

# Временно БД достаю из этой же папки, а парсинг на данный момент создает БД у себя в папке
engine = create_engine('sqlite:///lots.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class MyTable(Base):
    __tablename__ = 'lots'
    # id = Column(Integer)
    lot_number = Column(String, primary_key=True)
    trade_type = Column(String)
    e_platform = Column(String)
    subject_property_location = Column(String)
    start_date = Column(String)
    closing_date = Column(String)
    date_of_bidding = Column(String)
    subject_of_bidding = Column(String)
    lot_description = Column(String)
    property_location = Column(String)
    object_category = Column(String)
    form_of_ownership = Column(String)
    term_of_agreement = Column(String)
    type_of_contract = Column(String)
    lease_term = Column(String)
    initial_price = Column(String)
    auction_step = Column(String)
    deposit_amount = Column(String)
    recipient = Column(String)
    purpose_of_payment = Column(String)
    cadastral_number = Column(String)
    land_area = Column(String)
    type_of_use = Column(String)
    application_form = Column(String)
    status = Column(String)

    condition = Column(String)
    link_lot = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

metadata = MetaData()
metadata.create_all(engine)

rows = session.query(MyTable).all()
result = [row.as_dict() for row in rows]

# Сохраняем список словарей
import json

path = 'G:/Documents/Python/game/auction_manager/UI/'

with open(f'{path}dict_lot.json', 'w') as f:
    json.dump(result, f)