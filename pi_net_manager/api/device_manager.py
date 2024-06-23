from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_address = Column(String)
    mac_address = Column(String)

engine = create_engine("sqlite:///devices.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_devices():
    return session.query(Device).all()

def create_device(name, ip_address, mac_address):
    device = Device(name=name, ip_address=ip_address, mac_address=mac_address)
    session.add(device)
    session.commit()
    return device

def get_device(device_id):
    return session.query(Device).filter_by(id=device_id).first()

def update_device(device_id, name, ip_address, mac_address):
    device = session.query(Device).filter_by(id=device_id).first()
    if device:
        device.name = name
        device.ip_address = ip_address
        device.mac_address = mac_address
        session.commit()
    return device

def delete_device(device_id):
    device = session.query(Device).filter_by(id=device_id).first()
    if device:
        session.delete(device)
        session.commit()
    return {"message": "Device deleted successfully"}
