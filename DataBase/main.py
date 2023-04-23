from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
session = Session()
session.add(user)
session.commit()

user.age = 26
session.commit()