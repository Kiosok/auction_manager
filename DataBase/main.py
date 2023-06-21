from sqlite3 import IntegrityError

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///lots.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Lot(Base):
    __tablename__ = 'lots'
    #id = Column(Integer)
    lot_number = Column(String, primary_key=True)
    trade_type = Column(String)
    e_platform = Column(String)
    subject_property_location = Column(String)
    start_date = Column(String)
    closing_date = Column(String)
    status = Column(String, primary_key=True)

    def __init__(self, dict_lot):
        self.lot_number = dict_lot.get('Извещение, лот', None)
        self.trade_type = dict_lot.get('Вид торгов', None)
        self.e_platform = dict_lot.get('Электроннаяплощадка', None)
        self.subject_property_location = dict_lot.get('Субъект местонахождения имущества', None)
        self.start_date = dict_lot.get('Дата и время начала подачи заявок', None)
        self.closing_date = dict_lot.get('Дата и время окончания подачи заявок', None)
        self.status = dict_lot['Статус']

    def edit(self, new_name):
        self.lot_number = new_name

Base.metadata.create_all(engine)  # create tables
session = Session()

# create a new lot and add it to the database
dict_lot = {'Извещение, лот': '455', 'Вид торгов': 'Электронные', 'Электроннаяплощадка': 'Киров НЕТ',
            'Субъект местонахождения имущества': 'Кузня', 'Дата и время начала подачи заявок': '01.05.2022',
            'Дата и время окончания подачи заявок': '07.05.2022', 'Статус': 'Новые'}

lot_Vasya = Lot(dict_lot)
lot_Petya = Lot(dict_lot)

lot_Vasya.edit('Вася')

lot_Petya.edit('Петя')
session.merge(lot_Vasya)
lot_Petya.trade_type = 'РЫНОК'
lot_Petya.start_date = 'Everyday'
session.merge(lot_Petya)
session.commit()

#lot = session.query(Lot).get('Вася')
lots = session.query(Lot).filter(Lot.status == 'Новые').all()


# query the database for all lots
lots = session.query(Lot).all()
for lot in lots:
    print(lot.lot_number, lot.trade_type, lot.e_platform, lot.subject_property_location, lot.start_date, lot.closing_date, lot.start_date)