from xmlrpc.client import DateTime
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer, DateTime, BIGINT, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship


Pharmacy = mysql.connector.connect(
  host="localhost",
  user="root",
  database='chemistry',
  auth_plugin='mysql_native_password',
  password="Ueg8)ae-:!Nl",
)


engine = create_engine('mysql+mysqlconnector://root:Ueg8)ae-:!Nl@localhost:3306/chemistry', pool_pre_ping=True)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()

class User(Base):
  __tablename__ = 'User'

  idUser = Column(Integer, primary_key=True)
  UserName = Column(String(45), unique=True)
  FirstName = Column(String(45), nullable=False)
  LastName = Column(String(45), nullable=False)
  Email = Column(String(45), unique=True)
  Password = Column(String(45), nullable=False)
  Phone = Column(String(45), nullable=False)

class Status(Base):
    __tablename__ = 'Status'

    idStatus = Column(Integer, primary_key=True)
    Name = Column(String(45), nullable=False)

class Drug(Base):
    __tablename__ = 'Drug'

    idDrug = Column(Integer, primary_key=True)
    Name = Column(String(45), nullable=False)
    Price =  Column(Integer, nullable=False)
    idStatus = Column(Integer, ForeignKey(Status.idStatus))
    # Status = relationship('Status', backref='Drug', lazy=True)

class Order(Base):
    __tablename__ = 'Order'

    idOrder = Column(Integer, primary_key=True)
    idDrug = Column(Integer, ForeignKey(Drug.idDrug))
    Quantity = Column(Integer, nullable=False)
    idUser = Column(Integer, ForeignKey(User.idUser))
    idStatus = Column(Integer, ForeignKey(Status.idStatus))

    Drug = relationship(Drug, backref='Order', lazy="joined")
    User = relationship(User, backref='Order', lazy="joined")
    Status = relationship(Status, backref='Order', lazy="joined")

# Base.metadata.create_all(engine)

