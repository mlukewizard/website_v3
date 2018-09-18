import os

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = os.path.join('database', 'website_db')

Base = declarative_base()

class Product(Base):
    __tablename__ = 'user'
    productID = Column(String(250), primary_key=True)
    brand = Column(String(250), nullable=False)
    details = Column(String(250), nullable=False)
    img1Path = Column(String(250), nullable=False)
    img2Path = Column(String(250), nullable=False)
    price = Column(String(250), nullable=False)

    def __repr__(self):
        return self.productID

def delete_and_create_database():
    if os.path.exists(DATABASE_NAME + '.db'):
        os.remove(DATABASE_NAME + '.db')
    create_database()

def create_database():
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

def add_item(item):

    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    # Adds some stuff to the database
    DBSession = sessionmaker(bind=engine)

    session = DBSession()
    session.add(item)
    session.commit()


def get_entry_from_field_value(entryType, field, value):

    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    # Make a query to find all Persons in the database
    try:
        return session.query(entryType).filter(getattr(entryType, field) == value).one()
    except:
        return None

def get_all_entry_type(entryType):

    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    return session.query(entryType).all()

if __name__ == "__main__":
    delete_and_create_database()
    add_item(Product(productID = "1", brand="Fix-My-Road-Rash", details="Bandage", img1Path="path", img2Path="path", price="£10"))
    x = get_all_entry_type(Product)
    print('hi')