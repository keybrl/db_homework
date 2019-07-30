from models import *


class Response:
    def __init__(self, data=None, state_mes=None, status=200):
        self.data = data
        self.state_mes = state_mes
        self.status = status


@auto_session
def check_route(session, cust_id):
    if not session.query(Customers).filter(Customers.cust_id == cust_id).one():
        return Response(None, '客户不存在', 404)

    all_resv = session.\
        query(Reservations, Flights).\
        filter(1 == Reservations.resv_type).\
        filter(Flights.flight_num == Reservations.resv_key).\
        filter(Reservations.cust_id == cust_id).\
        order_by(Flights.departure_datetime).\
        all()

    if not all_resv:
        return Response(None, '该客户无行程', 204)

    data = []
    for i in all_resv:
        data.append(i[1].from_city)
        data.append(i[1].ariv_city)
    return Response(data, 'ok', 200)


def genesis():
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    except:
        return Response(None, '重建表失败', 500)
    return Response(None, 'ok', 204)


# Flights
@auto_session
def flight_insert(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    insert_data = []
    for i in data:
        flight_num = i.get('flight_num')
        price = i.get('price')
        num_seats = i.get('num_seats')
        from_city = i.get('from_city')
        ariv_city = i.get('ariv_city')
        departure_datetime = i.get('departure_datetime')
        landing_datetime = i.get('landing_datetime')
        if not flight_num or not price or not num_seats \
                or not from_city or not ariv_city \
                or not departure_datetime or not landing_datetime:
            return Response(None, '参数不全', 400)
        insert_data.append(Flights(
            flight_num=flight_num,
            price=price,
            num_seats=num_seats,
            num_avail=num_seats,
            from_city=from_city,
            ariv_city=ariv_city,
            departure_datetime=departure_datetime,
            landing_datetime=landing_datetime
        ))
    try:
        session.add_all(insert_data)
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)
    return Response(None, 'ok', 204)


@auto_session
def flight_delete(session, flight_num):
    if not flight_num:
        return Response(None, '参数不全', 400)

    flight = session.query(Flights).filter(Flights.flight_num == flight_num).first()

    if not flight:
        return Response(None, '航班不存在', 404)

    try:
        session.delete(flight)
        session.commit()
    except:
        session.rollback()
        return Response(None, '删除失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def flight_list(session):
    all_data = []
    for i in session.query(Flights).all():
        data = {
            'flight_num': i.flight_num,
            'price': i.price,
            'num_seats': i.num_seats,
            'num_avail': i.num_avail,
            'from_city': i.from_city,
            'ariv_city': i.ariv_city,
            'departure_datetime': i.departure_datetime,
            'landing_datetime': i.landing_datetime
        }
        all_data.append(data)
    return Response(all_data, 'ok', 200)


@auto_session
def flight_update(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    flight_num = data.get('flight_num')
    price = data.get('price')
    num_seats = data.get('num_seats')
    num_avail = None
    from_city = data.get('from_city')
    ariv_city = data.get('ariv_city')
    departure_datetime = data.get('departure_datetime')
    landing_datetime = data.get('landing_datetime')
    if not flight_num or (not price and not num_seats and not from_city and not ariv_city
                          and not departure_datetime and not landing_datetime):
        return Response(None, '未做任何修改')

    flight = session.query(Flights).filter(Flights.flight_num == flight_num).first()

    if not flight:
        return Response(None, '航班不存在', 404)

    if num_seats:
        num_avail = flight.num_avail + num_seats - flight.num_seats
        if num_avail < 0:
            return Response(None, '不允许将座位数调至已预约数量以下', 403)

    try:
        flight.price = price if price else flight.price
        flight.num_seats = num_seats if num_seats else flight.num_seats
        flight.num_avail = num_avail if num_avail else flight.num_avail
        flight.from_city = from_city if from_city else flight.from_city
        flight.ariv_city = ariv_city if ariv_city else flight.ariv_city
        flight.departure_datetime = departure_datetime if departure_datetime else flight.departure_datetime
        flight.landing_datetime = landing_datetime if landing_datetime else flight.landing_datetime
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)

    return Response(None, 'ok', 204)


# Hotels
@auto_session
def hotels_insert(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    insert_data = []
    for i in data:
        hotel_name = i.get('hotel_name')
        location = i.get('location')
        price = i.get('price')
        num_rooms = i.get('num_rooms')
        if not hotel_name or not location or not price or not num_rooms:
            return Response(None, '参数不全', 400)
        insert_data.append(Hotels(
            hotel_name=hotel_name,
            location=location,
            price=price,
            num_rooms=num_rooms,
            num_avail=num_rooms
        ))

    try:
        session.add_all(insert_data)
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def hotels_delete(session, hotel_name):
    if not hotel_name:
        return Response(None, '参数不全', 400)

    hotel = session.query(Hotels).filter(Hotels.hotel_name == hotel_name).first()

    if not hotel:
        return Response(None, '酒店不存在', 404)

    try:
        session.delete(hotel)
        session.commit()
    except:
        session.rollback()
        return Response(None, '删除失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def hotels_list(session):
    all_data = []
    for i in session.query(Hotels).all():
        data = {
            'hotel_name': i.hotel_name,
            'location': i.location,
            'price': i.price,
            'num_rooms': i.num_rooms,
            'num_avail': i.num_avail
        }
        all_data.append(data)
    return Response(all_data, 'ok', 200)


@auto_session
def hotels_update(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    hotel_name = data.get('hotel_name')
    location = data.get('location')
    price = data.get('price')
    num_rooms = data.get('num_rooms')
    num_avail = None

    if not hotel_name or (not location and not price and not num_rooms):
        return Response(None, '未做任何修改')

    hotel = session.query(Hotels).filter(Hotels.hotel_name == hotel_name).first()

    if not hotel:
        return Response(None, '酒店不存在', 404)

    if num_rooms:
        num_avail = hotel.num_avail + num_rooms - hotel.num_rooms
        if num_avail < 0:
            return Response(None, '不允许将房间数调至已预约数量以下', 403)

    try:
        hotel.location = location if location else hotel.location
        hotel.price = price if price else hotel.price
        hotel.num_rooms = num_rooms if num_rooms else hotel.num_rooms
        hotel.num_avail = num_avail if num_avail else hotel.num_avail
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)
    return Response(None, 'ok', 204)


# Bus
@auto_session
def bus_insert(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    insert_data = []
    for i in data:
        bus_num = i.get('bus_num')
        location = i.get('location')
        price = i.get('price')
        num_seats = i.get('num_seats')
        if not bus_num or not location or not price or not num_seats:
            return Response(None, '参数不全', 400)
        insert_data.append(Bus(
            bus_num=bus_num,
            location=location,
            price=price,
            num_seats=num_seats,
            num_avail=num_seats
        ))

    try:
        session.add_all(insert_data)
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def bus_delete(session, bus_num):
    if not bus_num:
        return Response(None, '参数不全', 400)

    bus = session.query(Bus).filter(Bus.bus_num == bus_num).first()

    if not bus:
        return Response(None, '巴士不存在', 404)

    try:
        session.delete(bus)
        session.commit()
    except:
        session.rollback()
        return Response(None, '删除失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def bus_list(session):
    all_data = []
    for i in session.query(Bus).all():
        data = {
            'bus_num': i.bus_num,
            'location': i.location,
            'price': i.price,
            'num_seats': i.num_seats,
            'num_avail': i.num_avail
        }
        all_data.append(data)
    return Response(all_data, 'ok', 200)


@auto_session
def bus_update(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    bus_num = data.get('bus_num')
    location = data.get('location')
    price = data.get('price')
    num_seats = data.get('num_seats')
    num_avail = None

    if not bus_num or (not location and not price and not num_seats):
        return Response(None, '未做任何修改')

    bus = session.query(Bus).filter(Bus.bus_num == bus_num).first()

    if not bus:
        return Response(None, '巴士不存在', 404)

    if num_seats:
        num_avail = bus.num_avail + num_seats - bus.num_seats
        if num_avail < 0:
            return Response(None, '不允许将座位数调至已预约数量以下', 403)

    try:
        bus.location = location if location else bus.location
        bus.price = price if price else bus.price
        bus.num_seats = num_seats if num_seats else num_seats
        bus.num_avail = num_avail if num_avail else num_avail
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)
    return Response(None, 'ok', 204)


# Customers
@auto_session
def customers_insert(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    insert_data = []
    for i in data:
        cust_name = i.get('cust_name')
        if not cust_name:
            return Response(None, '参数不全', 400)
        insert_data.append(Customers(
            cust_name=cust_name
        ))

    try:
        session.add_all(insert_data)
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def customers_delete(session, cust_id):
    if not cust_id:
        return Response(None, '参数不全', 400)

    cust = session.query(Customers).filter(Customers.cust_id == cust_id).first()

    if not cust:
        return Response(None, '航班不存在', 404)

    try:
        session.delete(cust)
        session.commit()
    except:
        session.rollback()
        return Response(None, '删除失败', 500)

    return Response(None, 'ok', 204)


@auto_session
def customers_list(session):
    all_data = []
    for i in session.query(Customers).all():
        data = {
            'cust_id': i.cust_id,
            'cust_name': i.cust_name
        }
        all_data.append(data)
    return Response(all_data, 'ok', 200)


@auto_session
def customers_update(session, data):
    if not data:
        return Response(None, '参数不全', 400)

    cust_id = data.get('cust_id')
    cust_name = data.get('cust_name')

    if not cust_id or not cust_name:
        return Response(None, '未做任何修改')

    cust = session.query(Customers).filter(Customers.cust_id == cust_id).first()

    if not cust:
        return Response(None, '客户不存在', 404)

    try:
        cust.cust_name = cust_name if cust_name else cust.cust_name
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)
    return Response(None, 'ok', 204)


# Reservations
@auto_session
def reservations_insert(session, resv):
    cust_id = resv.get('cust_id')
    resv_type = resv.get('resv_type')
    resv_key = resv.get('resv_key')
    if not cust_id or not resv_type or not resv_key:
        return Response(None, '参数不全', 400)
    if not session.query(Customers).filter(Customers.cust_id == cust_id).one():
        return Response(None, '客户不存在', 404)
    elif resv_type not in ('flight', 'hotel', 'bus'):
        return Response(None, '预约类别不存在', 404)

    resv_table = None
    if 'flight' == resv_type:
        resv_table = session.query(Flights).filter(Flights.flight_num == resv_key).first()
    elif 'hotel' == resv_type:
        resv_table = session.query(Hotels).filter(Hotels.hotel_name == resv_key).first()
    elif 'bus' == resv_type:
        resv_table = session.query(Bus).filter(Bus.bus_num == resv_key).first()

    if not resv_table:
        return Response(None, '预约的内容不存在', 404)
    elif resv_table.num_avail <= 0:
        return Response(None, '预约已满', 403)

    try:
        session.add(Reservations(
            cust_id=cust_id,
            resv_type=data_map['resv_type'][resv_type],
            resv_key=resv_key
        ))
        resv_table.num_avail -= 1
        session.commit()
    except:
        session.rollback()
        return Response(None, '写入失败', 500)
    return Response(None, 'ok', 204)


@auto_session
def reservations_delete(session, resv_id):
    if not resv_id:
        return Response(None, '参数不全', 400)

    resv = session.query(Reservations).filter(Reservations.resv_id == resv_id).first()

    if not resv:
        return Response(None, '预约不存在', 404)

    if 1 == resv.resv_type:
        resv_thing = session.query(Flights).filter(Flights.flight_num == resv.resv_key).first()
    elif 2 == resv.resv_type:
        resv_thing = session.query(Hotels).filter(Hotels.hotel_name == resv.resv_key).first()
    elif 3 == resv.resv_type:
        resv_thing = session.query(Bus).filter(Bus.bus_num == resv.resv_key).first()
    else:
        return Response(None, '见了鬼了', 500)

    try:
        resv_thing.num_avail += 1
        session.delete(resv)
        session.commit()
    except:
        session.rollback()
        return Response(None, '删除失败', 500)
    return Response(None, 'ok', 204)


@auto_session
def reservations_list(session, resv_type='all'):
    if 'flight' == resv_type:
        resv = session \
            .query(Reservations, Customers) \
            .filter(1 == Reservations.resv_type) \
            .filter(Customers.cust_id == Reservations.cust_id) \
            .order_by(Reservations.cust_id, Reservations.resv_type, Reservations.resv_key) \
            .all()
    elif 'hotel' == resv_type:
        resv = session \
            .query(Reservations, Customers) \
            .filter(2 == Reservations.resv_type) \
            .filter(Customers.cust_id == Reservations.cust_id) \
            .order_by(Reservations.cust_id, Reservations.resv_type, Reservations.resv_key) \
            .all()
    elif 'bus' == resv_type:
        resv = session \
            .query(Reservations, Customers) \
            .filter(3 == Reservations.resv_type) \
            .filter(Customers.cust_id == Reservations.cust_id) \
            .order_by(Reservations.cust_id, Reservations.resv_type, Reservations.resv_key) \
            .all()
    else:  # 'all' == resv_type
        resv = session \
            .query(Reservations, Customers) \
            .filter(Customers.cust_id == Reservations.cust_id) \
            .order_by(Reservations.cust_id, Reservations.resv_type, Reservations.resv_key) \
            .all()

    data = []
    resv_type_map = ['', 'flight', 'hotel', 'bus']
    for i in resv:
        data.append({
            'resv_id': i[0].resv_id,
            'cust_id': i[0].cust_id,
            'cust_name': i[1].cust_name,
            'resv_type': resv_type_map[i[0].resv_type],
            'resv_key': i[0].resv_key,
        })

    return Response(data, 'ok', 200)
