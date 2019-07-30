import os
import platform
from datetime import datetime
import views


class Selector:
    def __init__(self, info):
        self.chance = info['chance'] if info.get('chance') else 3
        self.options = info['options']
        self.flag = info.get('flag')
        self.mes = info.get('mes')

    def run(self):
        chance = self.chance
        while True:
            if self.mes:
                print(self.mes)
            else:
                print('\n输入提示的指令进行选择：')
            for i in self.options:
                if '_line' == i['sign']:
                    print('----------------')
                else:
                    print('%s: %s' % (i['sign'], i['label']))

            cmd = input(self.flag if self.flag else '\n>')
            for i in self.options:
                if i['sign'] == cmd:
                    return i['return']

            chance -= 1
            if not chance:
                print('给你的机会已经够多了！告辞...')
                quit_it('force')
                return 'quit'
            print('非法输入！\n.')
            continue


def initialize():
    global config
    config = dict()
    config['system'] = platform.system()


def run():
    state = 'home'
    while True:
        if 'home' == state:
            clear_screen()
            state = home()
        elif 'flights' == state:
            clear_screen()
            state = flights()
        elif 'hotels' == state:
            clear_screen()
            state = hotels()
        elif 'bus' == state:
            clear_screen()
            state = bus()
        elif 'cust' == state:
            clear_screen()
            state = cust()
        elif 'resv' == state:
            clear_screen()
            state = resv()
        elif 'genesis' == state:
            clear_screen()
            state = genesis()
        elif 'quit' == state:
            quit_it()
            break
        elif 'flights_view' == state:
            clear_screen()
            state = flights_view()
        elif 'hotels_view' == state:
            clear_screen()
            state = hotels_view()
        elif 'bus_view' == state:
            clear_screen()
            state = bus_view()
        elif 'cust_view' == state:
            clear_screen()
            state = cust_view()
        elif 'resv_view' == state:
            clear_screen()
            state = resv_view()
        elif 'flights_change' == state:
            clear_screen()
            state = flights_change()
        elif 'hotels_change' == state:
            clear_screen()
            state = hotels_change()
        elif 'bus_change' == state:
            clear_screen()
            state = bus_change()
        elif 'cust_change' == state:
            clear_screen()
            state = cust_change()
        elif 'resv_change' == state:
            clear_screen()
            state = resv_change()
        elif 'cust_route' == state:
            clear_screen()
            state = cust_route()
        else:
            print('十分抱歉，我们在人生的路口迷失了方向！')
            print('不能为您继续提供服务...')
            quit_it('force')
            state = 'quit'
            continue


def home():
    print('------------主菜单------------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nHome>',
        'options': [
            {'sign': 'flights', 'label': '航班管理；', 'return': 'flights'},
            {'sign': 'hotels', 'label': '酒店管理；', 'return': 'hotels'},
            {'sign': 'bus', 'label': '巴士管理；', 'return': 'bus'},
            {'sign': 'cust', 'label': '客户管理；', 'return': 'cust'},
            {'sign': 'resv', 'label': '预约管理；', 'return': 'resv'},
            {'sign': '_line'},
            {'sign': 'Genesis', 'label': '创世纪！（恢复默认数据）', 'return': 'genesis'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def flights():
    print('-----------航班管理-----------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nFlights>',
        'options': [
            {'sign': 'view', 'label': '查看航班信息；', 'return': 'flights_view'},
            {'sign': 'change', 'label': '修改航班信息；', 'return': 'flights_change'},
            {'sign': '_line'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def hotels():
    print('-----------酒店管理-----------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nHotels>',
        'options': [
            {'sign': 'view', 'label': '查看酒店信息；', 'return': 'hotels_view'},
            {'sign': 'change', 'label': '修改酒店信息；', 'return': 'hotels_change'},
            {'sign': '_line'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def bus():
    print('-----------巴士管理-----------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nBus>',
        'options': [
            {'sign': 'view', 'label': '查看巴士信息；', 'return': 'bus_view'},
            {'sign': 'change', 'label': '修改巴士信息；', 'return': 'bus_change'},
            {'sign': '_line'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def cust():
    print('-----------客户管理-----------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nCustomers>',
        'options': [
            {'sign': 'view', 'label': '查看客户信息；', 'return': 'cust_view'},
            {'sign': 'change', 'label': '修改客户信息；', 'return': 'cust_change'},
            {'sign': 'route', 'label': '查看客户行程信息；', 'return': 'cust_route'},
            {'sign': '_line'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def resv():
    print('-----------预约管理-----------\n.')
    print('请问您需要执行以下何种操作？')
    selector = Selector({
        'flag': '\nReservations>',
        'options': [
            {'sign': 'view', 'label': '查看预约信息；', 'return': 'resv_view'},
            {'sign': 'change', 'label': '修改预约信息；', 'return': 'resv_change'},
            {'sign': '_line'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
            {'sign': 'quit', 'label': '退出！', 'return': 'quit'},
        ],
    })
    return selector.run()


def genesis():
    selector = Selector({
        'flag': '\nGenesis>',
        'options': [
            {'sign': 'retry', 'label': '再次创世！', 'return': 'genesis'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })

    def is_err():
        if 204 != response.status:
            print('创世失败！')
            print('错误信息：' + response.state_mes)
            print('\n您还可以继续操作...')
            return True

    response = views.genesis()
    if is_err():
        return selector.run()

    response = views.flight_insert([
        {
            'flight_num': 'CZ3217',
            'price': 1450,
            'num_seats': 208,
            'from_city': '广州',
            'ariv_city': '西安',
            'departure_datetime': datetime(2018, 6, 6, 19, 25),
            'landing_datetime': datetime(2018, 6, 6, 22, 0)
        }, {
            'flight_num': 'MU2119',
            'price': 920,
            'num_seats': 257,
            'from_city': '西安',
            'ariv_city': '北京',
            'departure_datetime': datetime(2018, 6, 6, 22, 30),
            'landing_datetime': datetime(2018, 6, 7, 0, 30)
        }, {
            'flight_num': 'CZ5116',
            'price': 670,
            'num_seats': 300,
            'from_city': '北京',
            'ariv_city': '上海',
            'departure_datetime': datetime(2018, 6, 7, 6, 50),
            'landing_datetime': datetime(2018, 6, 7, 9, 15)
        }, {
            'flight_num': 'FM725',
            'price': 804,
            'num_seats': 208,
            'from_city': '上海',
            'ariv_city': '香港',
            'departure_datetime': datetime(2018, 6, 7, 21, 20),
            'landing_datetime': datetime(2018, 6, 7, 23, 35)
        }, {
            'flight_num': 'SQ002',
            'price': 3753,
            'num_seats': 350,
            'from_city': '香港',
            'ariv_city': '旧金山',
            'departure_datetime': datetime(2018, 6, 8, 23, 30),
            'landing_datetime': datetime(2018, 6, 9, 12, 15)
        }, {
            'flight_num': 'UA857',
            'price': 6280,
            'num_seats': 352,
            'from_city': '旧金山',
            'ariv_city': '上海',
            'departure_datetime': datetime(2018, 6, 10, 13, 20),
            'landing_datetime': datetime(2018, 6, 11, 2, 25)
        }, {
            'flight_num': 'CZ3527',
            'price': 3700,
            'num_seats': 208,
            'from_city': '上海',
            'ariv_city': '广州',
            'departure_datetime': datetime(2018, 6, 11, 18, 50),
            'landing_datetime': datetime(2018, 6, 11, 21, 15)
        },
    ])
    if is_err():
        return selector.run()

    response = views.hotels_insert([
        {
            'hotel_name': '西北饭店',
            'location': '西安',
            'price': 700,
            'num_rooms': 543
        }, {
            'hotel_name': '佛山宾馆',
            'location': '佛山',
            'price': 2000,
            'num_rooms': 387
        }, {
            'hotel_name': '白宫',
            'location': '华盛顿特区',
            'price': 2333,
            'num_rooms': 1
        }, {
            'hotel_name': 'Ritz-Carlton',
            'location': '亚特兰大',
            'price': 10000,
            'num_rooms': 200
        }, {
            'hotel_name': '建国饭店',
            'location': '西安',
            'price': 500,
            'num_rooms': 200
        }, {
            'hotel_name': '希尔顿花园酒店',
            'location': '西安',
            'price': 300,
            'num_rooms': 230
        }, {
            'hotel_name': '西安电子科技大学',
            'location': '西安',
            'price': 20,
            'num_rooms': 30000
        }, {
            'hotel_name': '志诚丽柏',
            'location': '西安',
            'price': 356,
            'num_rooms': 150
        },
    ])
    if is_err():
        return selector.run()

    response = views.bus_insert([
        {
            'bus_num': '916路',
            'location': '西安',
            'price': 2,
            'num_seats': 20
        }, {
            'bus_num': '广275',
            'location': '广州',
            'price': 4,
            'num_seats': 25
        }, {
            'bus_num': '佛232B',
            'location': '广州、佛山',
            'price': 2,
            'num_seats': 25
        }, {
            'bus_num': '桂04',
            'location': '南海、佛山',
            'price': 2,
            'num_seats': 20
        }, {
            'bus_num': '桂10',
            'location': '南海',
            'price': 2,
            'num_seats': 20
        }
    ])
    if is_err():
        return selector.run()

    response = views.customers_insert([
        {'cust_name': '罗阳豪'},
        {'cust_name': 'Keyboard'},
        {'cust_name': 'KeybrL'},
        {'cust_name': 'Maozu'},
        {'cust_name': '猫组'},
        {'cust_name': '王可馨'},
        {'cust_name': '方学习'},
        {'cust_name': 'Study FANG'},
        {'cust_name': 'LUO Y.-H.'},
        {'cust_name': 'WANG Ke-xin'},
    ])
    if is_err():
        return selector.run()

    resv_list = [
        {'cust_id': '1', 'resv_type': 'flight', 'resv_key': 'CZ3217'},
        {'cust_id': '1', 'resv_type': 'flight', 'resv_key': 'CZ5116'},
        {'cust_id': '1', 'resv_type': 'flight', 'resv_key': 'FM725'},
        {'cust_id': '1', 'resv_type': 'flight', 'resv_key': 'UA857'},
        {'cust_id': '1', 'resv_type': 'hotel', 'resv_key': '白宫'},
        {'cust_id': '1', 'resv_type': 'bus', 'resv_key': '916路'},
    ]
    for i in resv_list:
        response = views.reservations_insert(i)
        if is_err():
            print(i)
            return selector.run()
    return selector.run()


def quit_it(mod='default'):
    if 'default' == mod:
        print('\n很荣幸为您提供服务，再会！')
        exit(1)
    elif 'force' == mod:
        print('\n服务已被强制终止...')
        exit(0)


# view
def flights_view(mod='default'):
    if 'default' == mod:
        print('===== 航班信息 =====\n')
    response = views.flight_list()
    if 200 != response.status:
        print('十分抱歉未能获取航班信息！')
        print('错误信息：' + response.state_mes)
        print('您可以继续操作...')
    else:
        data = response.data
        for i in range(len(data)):
            data[i] = (
                data[i]['flight_num'],
                str(data[i]['price']),
                str(data[i]['num_seats']),
                str(data[i]['num_avail']),
                data[i]['from_city'],
                data[i]['ariv_city'],
                data[i]['departure_datetime'].strftime('%Y-%m-%d %H:%M'),
                data[i]['landing_datetime'].strftime('%Y-%m-%d %H:%M'),
            )
        data.insert(0, (
            '航班号',
            '价格',
            '座位数',
            '余座',
            '起飞城市',
            '降落城市',
            '起飞时间',
            '降落时间',
        ))
        print_table({
            'float_type': ['left', 'right', 'right', 'right', 'left', 'left', 'left', 'left'],
            'data': data,
        })
    if 'default' == mod:
        selector = Selector({
            'flag': '\nFlights/View>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'flights_view'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'flights'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'flights'


def hotels_view(mod='default'):
    if 'default' == mod:
        print('===== 酒店信息 =====\n')
    response = views.hotels_list()
    if 200 != response.status:
        print('十分抱歉未能获取酒店信息！')
        print('错误信息：' + response.state_mes)
        print('您可以继续操作...')
    else:
        data = response.data
        for i in range(len(data)):
            data[i] = (
                data[i]['hotel_name'],
                data[i]['location'],
                str(data[i]['price']),
                str(data[i]['num_rooms']),
                str(data[i]['num_avail']),
            )
        data.insert(0, (
            '酒店名',
            '地点',
            '价格',
            '房间数',
            '房间余量',
        ))
        print_table({
            'float_type': ['left', 'left', 'right', 'right', 'right'],
            'data': data,
        })
    if 'default' == mod:
        selector = Selector({
            'flag': '\nHotels/View>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'hotels_view'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'hotels'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'home'


def bus_view(mod='default'):
    if 'default' == mod:
        print('===== 巴士信息 =====\n')
    response = views.bus_list()
    if 200 != response.status:
        print('十分抱歉未能获取巴士信息！')
        print('错误信息：' + response.state_mes)
        print('您可以继续操作...')
    else:
        data = response.data
        for i in range(len(data)):
            data[i] = (
                data[i]['bus_num'],
                data[i]['location'],
                str(data[i]['price']),
                str(data[i]['num_seats']),
                str(data[i]['num_avail']),
            )
        data.insert(0, (
            '巴士编号',
            '地点',
            '价格',
            '座位数',
            '余座',
        ))
        print_table({
            'float_type': ['left', 'left', 'right', 'right', 'right'],
            'data': data,
        })
    if 'default' == mod:
        selector = Selector({
            'flag': '\nBus/View>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'bus_view'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'bus'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'home'


def cust_view(mod='default'):
    if 'default' == mod:
        print('===== 客户信息 =====\n')
    response = views.customers_list()
    if 200 != response.status:
        print('十分抱歉未能获取客户信息！')
        print('错误信息：' + response.state_mes)
        print('您可以继续操作...')
    else:
        data = response.data
        for i in range(len(data)):
            data[i] = (
                str(data[i]['cust_id']),
                data[i]['cust_name'],
            )
        data.insert(0, (
            '客户编号',
            '客户姓名',
        ))
        print_table({
            'float_type': ['right', 'left'],
            'data': data,
        })
    if 'default' == mod:
        selector = Selector({
            'flag': '\nCustomers/View>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'cust_view'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'cust'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'home'


def cust_route(mod='default'):
    if 'default' == mod:
        print('===== 客户行程 =====\n')
        print('已有的客户信息：')
        cust_view('simple')
    cust_id = input('需要打印行程的客户的客户编号:')
    response = views.check_route(cust_id)
    if 200 != response.status:
        print('获取行程失败！')
        print('错误信息：' + response.state_mes)
        print('您还可以继续操作...')
    else:
        data = response.data
        print('该客户行程路线：')
        for i in range(len(data)):
            if i != 0 and i % 2 == 0:
                if data[i] != data[i-1]:
                    print(data[i], end=' -> ')
            elif i == 0:
                print(data[i], end=' -> ')
            else:
                print(data[i], end='')
                if i == len(data) - 1:
                    print()
                elif data[i] == data[i+1]:
                    print(' -> ', end='')
                else:
                    print(' --- ', end='')
    if 'default' == mod:
        selector = Selector({
            'flag': '\nCustomers/Route>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'cust_route'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'cust'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'home'


def resv_view(mod='default'):
    if 'default' == mod:
        print('===== 预约信息 =====\n')
    selector = Selector({
        'mes': '选择预约种类：',
        'flag': '\nReservations/View>',
        'options': [
            {'sign': 'all', 'label': '全部预约；', 'return': 'all'},
            {'sign': 'flights', 'label': '航班预约；', 'return': 'flight'},
            {'sign': 'hotels', 'label': '酒店预约；', 'return': 'hotel'},
            {'sign': 'bus', 'label': '巴士预约；', 'return': 'bus'},
        ],
    })
    response = views.reservations_list(selector.run() if 'default' == mod else 'all')
    if 200 != response.status:
        print('十分抱歉未能获取预约信息！')
        print('错误信息：' + response.state_mes)
        print('您可以继续操作...')
    else:
        data = response.data
        for i in range(len(data)):
            data[i] = (
                str(data[i]['resv_id']),
                str(data[i]['cust_id']),
                data[i]['cust_name'],
                data[i]['resv_type'][0].upper() + data[i]['resv_type'][1:],
                data[i]['resv_key'],
            )
        data.insert(0, (
            '预约编号',
            '客户编号',
            '客户名',
            '预约类型',
            '预约内容',
        ))
        print_table({
            'float_type': ['right', 'right', 'left', 'left', 'left'],
            'data': data,
        })
    if 'default' == mod:
        selector = Selector({
            'flag': '\nReservations/View>',
            'options': [
                {'sign': 'reload', 'label': '刷新数据；', 'return': 'resv_view'},
                {'sign': '_line'},
                {'sign': 'back', 'label': '返回上级目录；', 'return': 'resv'},
                {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'}
            ]
        })
        return selector.run()
    return 'home'


# change
def flights_change():
    print('===== 修改航班信息 =====\n')
    selector = Selector({
        'mes': '对航班信息作何种修改？',
        'flag': '\nFlights/Change>',
        'options': [
            {'sign': 'add', 'label': '增加', 'return': 'add'},
            {'sign': 'del', 'label': '删除', 'return': 'del'},
            {'sign': 'update', 'label': '更新', 'return': 'update'},
            {'sign': '_line'},
            {'sign': 'cancel', 'label': '取消修改！', 'return': 'cancel'},
        ]
    })
    cmd = selector.run()
    if 'add' == cmd:
        flag = '/Add'
        print('增加的航班的信息：')
        flight_num = input('航班号: ')
        chance = 2
        while chance:
            try:
                price = int(input('票价: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            price = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')
        chance = 2
        while chance:
            try:
                num_seats = int(input('座位数: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            num_seats = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')
        from_city = input('起飞城市: ')
        ariv_city = input('降落城市: ')
        chance = 2
        while chance:
            try:
                departure_datetime = datetime.strptime(input('起飞时间(格式: "YYYY-mm-dd HH:MM"): '), '%Y-%m-%d %H:%M')
                landing_datetime = datetime.strptime(input('降落时间(格式同上): '), '%Y-%m-%d %H:%M')
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            departure_datetime = landing_datetime = datetime(1949, 10, 1, 0, 0)
            print('给你的机会已经够多了！告辞...')
            quit_it('force')

        response = views.flight_insert([{
            'flight_num': flight_num,
            'price': price,
            'num_seats': num_seats,
            'from_city': from_city,
            'ariv_city': ariv_city,
            'departure_datetime': departure_datetime,
            'landing_datetime': landing_datetime
        }])
        if 204 != response.status:
            print('数据插入失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('插入成功！')
    elif 'del' == cmd:
        flag = '/Delete'
        print('已有航班信息：')
        flights_view('simple')
        flight_num = input('\n所需删除的航班的航班号: ')
        response = views.flight_delete(flight_num)
        if 204 != response.status:
            print('删除失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('删除成功！')
    elif 'update' == cmd:
        flag = '/Update'
        print('已有航班信息：')
        flights_view('simple')
        flight_num = input('\n所需更新的航班的航班号： ')
        print('以下条目如需更新则输入新的信息，如不需要则留空')
        try:
            price = int(input('票价: '))
        except:
            price = None
        try:
            num_seats = int(input('座位数: '))
        except:
            num_seats = None
        from_city = input('起飞城市: ')
        ariv_city = input('降落城市: ')
        try:
            departure_datetime = datetime.strptime(input('起飞时间(格式: "YYYY-mm-dd HH:MM"): '), '%Y-%m-%d %H:%M')
        except:
            departure_datetime = None
        try:
            landing_datetime = datetime.strptime(input('降落时间(格式同上): '), '%Y-%m-%d %H:%M')
        except:
            landing_datetime = None

        response = views.flight_update({
            'flight_num': flight_num if flight_num else None,
            'price': price if price else None,
            'num_seats': num_seats if num_seats else None,
            'from_city': from_city if from_city else None,
            'ariv_city': ariv_city if ariv_city else None,
            'departure_datetime': departure_datetime if departure_datetime else None,
            'landing_datetime': landing_datetime if landing_datetime else None
        })
        if 204 != response.status:
            print('数据更新失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('更新成功！')
    else:
        flag = ''

    print('您还可以继续操作...')
    selector = Selector({
        'flag': '\nFlights/Change' + flag + '>',
        'options': [
            {'sign': 'continue', 'label': '继续修改；', 'return': 'flights_change'},
            {'sign': 'back', 'label': '返回上级目录；', 'return': 'flights'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })
    return selector.run()


def hotels_change():
    print('===== 修改酒店信息 =====\n')
    selector = Selector({
        'mes': '对酒店信息作何种修改？',
        'flag': '\nHotels/Change>',
        'options': [
            {'sign': 'add', 'label': '增加', 'return': 'add'},
            {'sign': 'del', 'label': '删除', 'return': 'del'},
            {'sign': 'update', 'label': '更新', 'return': 'update'},
            {'sign': '_line'},
            {'sign': 'cancel', 'label': '取消修改！', 'return': 'cancel'},
        ]
    })
    cmd = selector.run()
    if 'add' == cmd:
        flag = '/Add'
        print('增加的酒店的信息：')
        hotel_name = input('酒店名: ')
        location = input('地点: ')
        chance = 2
        while chance:
            try:
                price = int(input('价格: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            price = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')
        chance = 2
        while chance:
            try:
                num_rooms = int(input('房间数: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            num_rooms = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')

        response = views.hotels_insert([{
            'hotel_name': hotel_name,
            'location': location,
            'price': price,
            'num_rooms': num_rooms
        }])
        if 204 != response.status:
            print('数据插入失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('插入成功！')
    elif 'del' == cmd:
        flag = '/Delete'
        print('已有酒店信息：')
        hotels_view('simple')
        hotel_name = input('\n所需删除的酒店的酒店名: ')
        response = views.hotels_delete(hotel_name)
        if 204 != response.status:
            print('删除失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('删除成功！')
    elif 'update' == cmd:
        flag = '/Update'
        print('已有酒店信息：')
        hotels_view('simple')
        hotel_name = input('\n所需更新的酒店的酒店名: ')
        print('以下条目如需更新则输入新的信息，如不需要则留空')
        location = input('地点：')
        try:
            price = int(input('票价: '))
        except:
            price = None
        try:
            num_rooms = int(input('房间数: '))
        except:
            num_rooms = None

        response = views.hotels_update({
            'hotel_name': hotel_name,
            'location': location if location else None,
            'price': price if price else None,
            'num_rooms': num_rooms if num_rooms else None,
        })
        if 204 != response.status:
            print('数据更新失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('更新成功！')
    else:
        flag = ''

    print('您还可以继续操作...')
    selector = Selector({
        'flag': '\nFlights/Change' + flag + '>',
        'options': [
            {'sign': 'continue', 'label': '继续修改；', 'return': 'hotels_change'},
            {'sign': 'back', 'label': '返回上级目录；', 'return': 'hotels'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })
    return selector.run()


def bus_change():
    print('===== 修改巴士信息 =====\n')
    selector = Selector({
        'mes': '对巴士信息作何种修改？',
        'flag': '\nBus/Change>',
        'options': [
            {'sign': 'add', 'label': '增加', 'return': 'add'},
            {'sign': 'del', 'label': '删除', 'return': 'del'},
            {'sign': 'update', 'label': '更新', 'return': 'update'},
            {'sign': '_line'},
            {'sign': 'cancel', 'label': '取消修改！', 'return': 'cancel'},
        ]
    })
    cmd = selector.run()
    if 'add' == cmd:
        flag = '/Add'
        print('增加的巴士的信息：')
        bus_num = input('巴士编号: ')
        location = input('地点: ')
        chance = 2
        while chance:
            try:
                price = int(input('价格: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            price = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')
        chance = 2
        while chance:
            try:
                num_seats = int(input('座位数: '))
                break
            except:
                chance -= 1
                print('非法输入！请重新输入')
        else:
            num_seats = 0
            print('给你的机会已经够多了！告辞...')
            quit_it('force')

        response = views.bus_insert([{
            'bus_num': bus_num,
            'location': location,
            'price': price,
            'num_seats': num_seats
        }])
        if 204 != response.status:
            print('数据插入失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('插入成功！')
    elif 'del' == cmd:
        flag = '/Delete'
        print('已有酒店信息：')
        bus_view('simple')
        bus_num = input('\n所需删除的巴士的巴士编号: ')
        response = views.bus_delete(bus_num)
        if 204 != response.status:
            print('删除失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('删除成功！')
    elif 'update' == cmd:
        flag = '/Update'
        print('已有巴士信息：')
        bus_view('simple')
        bus_num = input('\n所需更新的巴士的巴士编号: ')
        print('以下条目如需更新则输入新的信息，如不需要则留空')
        location = input('地点: ')
        try:
            price = int(input('票价: '))
        except:
            price = None
        try:
            num_seats = int(input('座位数: '))
        except:
            num_seats = None

        response = views.bus_update({
            'bus_num': bus_num,
            'location': location if location else None,
            'price': price if price else None,
            'num_seats': num_seats if num_seats else None,
        })
        if 204 != response.status:
            print('数据更新失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('更新成功！')
    else:
        flag = ''

    print('您还可以继续操作...')
    selector = Selector({
        'flag': '\nBus/Change' + flag + '>',
        'options': [
            {'sign': 'continue', 'label': '继续修改；', 'return': 'bus_change'},
            {'sign': 'back', 'label': '返回上级目录；', 'return': 'bus'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })
    return selector.run()


def cust_change():
    print('===== 修改客户信息 =====\n')
    selector = Selector({
        'mes': '对客户信息作何种修改？',
        'flag': '\nCustomers/Change>',
        'options': [
            {'sign': 'add', 'label': '增加', 'return': 'add'},
            {'sign': 'del', 'label': '删除', 'return': 'del'},
            {'sign': 'update', 'label': '更新', 'return': 'update'},
            {'sign': '_line'},
            {'sign': 'cancel', 'label': '取消修改！', 'return': 'cancel'},
        ]
    })
    cmd = selector.run()
    if 'add' == cmd:
        flag = '/Add'
        print('增加的客户的信息：')
        cust_name = input('客户名: ')

        response = views.customers_insert([{
            'cust_name': cust_name,
        }])
        if 204 != response.status:
            print('数据插入失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('插入成功！')
    elif 'del' == cmd:
        flag = '/Delete'
        print('已有客户信息：')
        cust_view('simple')
        cust_id = input('\n所需删除的客户的客户编号: ')
        response = views.customers_delete(cust_id)
        if 204 != response.status:
            print('删除失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('删除成功！')
    elif 'update' == cmd:
        flag = '/Update'
        print('已有客户信息：')
        cust_view('simple')
        cust_id = input('\n所需更新的客户的客户编号： ')
        cust_name = input('客户姓名: ')

        response = views.customers_update({
            'cust_id': cust_id,
            'cust_name': cust_name,
        })
        if 204 != response.status:
            print('数据更新失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('更新成功！')
    else:
        flag = ''

    print('您还可以继续操作...')
    selector = Selector({
        'flag': '\nCustomers/Change' + flag + '>',
        'options': [
            {'sign': 'continue', 'label': '继续修改；', 'return': 'cust_change'},
            {'sign': 'back', 'label': '返回上级目录；', 'return': 'cust'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })
    return selector.run()


def resv_change():
    print('===== 修改预约信息 =====\n')
    selector = Selector({
        'mes': '对预约信息作何种修改？',
        'flag': '\nReservation/Change>',
        'options': [
            {'sign': 'add', 'label': '增加', 'return': 'add'},
            {'sign': 'del', 'label': '删除', 'return': 'del'},
            {'sign': '_line'},
            {'sign': 'cancel', 'label': '取消修改！', 'return': 'cancel'},
        ]
    })
    cmd = selector.run()
    if 'add' == cmd:
        flag = '/Add'
        print('增加的预约的信息：')
        print('已有客户信息：')
        cust_view('simple')
        cust_id = input('客户编号: ')
        selector = Selector({
            'mes': '预约类型：',
            'flag': 'Reservation/Change/Add>',
            'options': [
                {'sign': 'flights', 'label': '航班', 'return': 'flight'},
                {'sign': 'hotels', 'label': '酒店', 'return': 'hotel'},
                {'sign': 'bus', 'label': '巴士', 'return': 'bus'},
            ]
        })
        resv_type = selector.run()
        if 'flight' == resv_type:
            print('已有航班信息：')
            flights_view('simple')
            resv_key = input('预约的航班号: ')
        elif 'hotel' == resv_type:
            print('已有酒店信息：')
            hotels_view('simple')
            resv_key = input('预约的酒店名: ')
        elif 'bus' == resv_type:
            print('已有巴士信息：')
            bus_view('simple')
            resv_key = input('预约的巴士编号: ')
        else:
            print('见鬼了！')
            resv_key = ''

        response = views.reservations_insert({
            'cust_id': cust_id,
            'resv_type': resv_type,
            'resv_key': resv_key,
        })
        if 204 != response.status:
            print('数据插入失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('插入成功！')
    elif 'del' == cmd:
        flag = '/Delete'
        print('已有预约信息：')
        resv_view('simple')
        resv_id = input('\n所需删除的预约的预约编号: ')
        response = views.reservations_delete(resv_id)
        if 204 != response.status:
            print('删除失败！')
            print('错误信息：' + response.state_mes)
        else:
            print('删除成功！')
    else:
        flag = ''

    print('您还可以继续操作...')
    selector = Selector({
        'flag': '\nReservations/Change' + flag + '>',
        'options': [
            {'sign': 'continue', 'label': '继续修改；', 'return': 'resv_change'},
            {'sign': 'back', 'label': '返回上级目录；', 'return': 'resv'},
            {'sign': 'home', 'label': '返回主菜单！', 'return': 'home'},
        ]
    })
    return selector.run()


# Print Tools
def print_table(info):
    data = info['data']
    float_type = info['float_type']
    max_len = [0 for _ in data[0]]
    for item in data:
        for i in range(len(item)):
            max_len[i] = len(item[i].encode('gbk')) \
                if len(item[i].encode('gbk')) > max_len[i] \
                else max_len[i]

    print_table_line(max_len)
    print_table_data(data[0], max_len, ['center' for _ in data[0]])
    print_table_line(max_len)
    for item in data[1:]:
        print_table_data(item, max_len, float_type)
    print_table_line(max_len)


def print_table_repeat(source, times):
    for _ in range(times):
        print(source, end='')


def print_table_line(max_len):
    for i in max_len:
        print('+', end='')
        print_table_repeat('-', i + 2)
    else:
        print('+')


def print_table_data(item, max_len, float_type):
    for i in range(len(item)):
        print('|', end='')
        all_space = max_len[i] - len(item[i].encode('gbk')) + 2
        if 'right' == float_type[i]:
            print_table_repeat(' ', all_space - 1)
            print(item[i], end='')
            print(' ', end='')
        elif 'left' == float_type[i]:
            print(' ', end='')
            print(item[i], end='')
            print_table_repeat(' ', all_space - 1)
        else:  # center
            print_table_repeat(' ', all_space // 2)
            print(item[i], end='')
            print_table_repeat(' ', all_space - (all_space // 2))
    else:
        print('|')


# Useful Tools
def clear_screen():
    if 'Linux' == config['system']:
        os.system('clear')
    elif 'Windows' == config['system']:
        os.system('cls')
    elif 'Darwin' == config['system']:
        os.system('clear')
    else:
        print('清屏操作被未知力量所阻止！')
        print('----------------------\n.\n.\n.\n.\n')


if '__main__' == __name__:
    initialize()
    run()
