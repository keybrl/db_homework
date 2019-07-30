import pymysql
import random

# database connection info
HOST = '127.0.0.1'
PORT = 3306  # The default value is 3306
USER = 'root'
PASSWORD = ''
DATABASE = 'BANK191'
TABLE = 'account191'

# 'M-00000000', 'M-00000001', ...
ACCOUNT_NUMBER_PREFIX = 'M-'  # Any value you like
ACCOUNT_NUMBER_RANGE = (0, 5000000)
# To torture the database, it is best to have more than 5,000,000 data.
# Insert approximately 10,000 data per second.
# It is slow but still faster than you.

BRANCH_NAMES = (
    'Downtown',
    'Perryridge',
    'Brighton',
    'Mianus',
    'Redwood',
    'Round Hill'
)

BALANCE_RANGE = (0, 10000000)  # Even distribution(, which is ridiculous.)


# You can run it now, and just ignore the following contents.
try:
    conn = pymysql.connect(host=HOST, port=PORT, db=DATABASE, user=USER, passwd=PASSWORD)
except pymysql.err.OperationalError as e:
    print('Error: ' + str(e))
    exit(-1)

cur = conn.cursor()

for i in range(ACCOUNT_NUMBER_RANGE[0], ACCOUNT_NUMBER_RANGE[1]):
    account_number = '%s%08d' % (ACCOUNT_NUMBER_PREFIX, i)
    if 0 == i % 10000:
        conn.commit()
        print('%s, has commit' % account_number)
    branch_name = random.choice(BRANCH_NAMES)
    balance = '%d.%d' % (random.randrange(BALANCE_RANGE[0], BALANCE_RANGE[1]), random.randrange(0, 99))
    balance = 0.01 if '0.0' == balance else float(balance)
    cur.execute('INSERT INTO ' + TABLE + ' VALUE (%s, %s, %s)', (account_number, branch_name, balance))
conn.commit()
conn.close()
