# 导入:
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

with open('config.json', 'r') as fp:
    config_json = fp.read(1024)
    config = json.loads(config_json)


# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine(
    # 'mysql+pymysql://' + config['db_user'] + ':' + config['db_passwd'] +
    # '@' + config['db_host'] + '/' + config['db_name'] + '?charset=' + config['db_charset'],
    'sqlite:///db.sqlite',
)
# 创建DBSession类型:
Session = sessionmaker(bind=engine)


class Flights(Base):
    __tablename__ = 'flights'

    flight_num = Column(String(32), primary_key=True)
    price = Column(Integer)
    num_seats = Column(Integer)
    num_avail = Column(Integer)
    from_city = Column(String(128))
    ariv_city = Column(String(128))
    departure_datetime = Column(DateTime)
    landing_datetime = Column(DateTime)


class Hotels(Base):
    __tablename__ = 'hotels'

    hotel_name = Column(String(128), primary_key=True)
    location = Column(String(128))
    price = Column(Integer)
    num_rooms = Column(Integer)
    num_avail = Column(Integer)


class Bus(Base):
    __tablename__ = 'bus'

    bus_num = Column(String(32), primary_key=True)
    location = Column(String(128))
    price = Column(Integer)
    num_seats = Column(Integer)
    num_avail = Column(Integer)


class Customers(Base):
    __tablename__ = 'customers'

    cust_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_name = Column(String(128))


class Reservations(Base):
    __tablename__ = 'reservations'

    resv_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_id = Column(Integer)
    resv_type = Column(Integer)
    resv_key = Column(String(128))


def auto_session(func):
    def _func(*args, **kwargs):
        session = Session()
        func_return = func(session, *args, **kwargs)
        session.close()
        return func_return
    return _func


data_map = {
    'resv_type': {
        'flight': 1,
        'hotel': 2,
        'bus': 3
    },
}


if '__main__' == __name__:
    Base.metadata.create_all(engine)


