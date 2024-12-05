from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Beneficiary(Base):
    __tablename__ = 'beneficiaries'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)
    state = Column(String)
    address = Column(String)
    photo = Column(String)

class AidRecord(Base):
    __tablename__ = 'aid_records'
    id = Column(Integer, primary_key=True)
    beneficiary_id = Column(Integer, ForeignKey('beneficiaries.id'))
    aid_type = Column(String)
    distribution_date = Column(Date)
    status = Column(String)

class FaceEmbedding(Base):
    __tablename__ = 'face_embeddings'
    id = Column(Integer, primary_key=True)
    beneficiary_id = Column(Integer, ForeignKey('beneficiaries.id'))
    embedding_data = Column(String)
