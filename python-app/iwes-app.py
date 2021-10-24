from psycopg2 import connect  # published under GNU Lesser General Public License
import pandas

# init postgres stuff
table_name = "NMEA"

conn = connect(
    dbname="iwes_challenge",
    user="iwes",
    host="iwes-postgres-db",
    port="5432",
    password="iwes"
)

cursor = conn.cursor()

cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, a TEXT, b TEXT, c TEXT, status1 TEXT, d TEXT, e TEXT, status2 TEXT, f TEXT, status3 TEXT, g TEXT, status4 TEXT, HeaveRaw TEXT, status5 TEXT, HeaveLever TEXT, SurgeLever TEXT, SwayLever TEXT, HeaveSpeed TEXT, SurgeSpeed TEXT, SwaySpeed TEXT, HeadingROT TEXT, Checksum TEXT);")
# get column names
data_frame = pandas.read_sql_query('SELECT * FROM {} LIMIT 0'.format(table_name), conn)
table_columns = list(pandas.DataFrame.head(data_frame))

# pop sequential primary key id since it is automatically filled
table_columns.pop(0)

while True:
    # store the given input
    data = input('\n Enter sensor information beginning with \'$PHOCT\' or quit with \'Exit\': \n')
    if data.lower() == 'exit':
        break

    # build string for sql INSERT
    data_list = data.replace('*',',').split(',')
    if data_list[0] != '$PHOCT':
        print(f'wrong signal information')
    else:
        value = ''
        for column in data_list[:-1]:
            value += '\'{}\''.format(column)
            value += ','
        value += '\'*' + data_list[-1] + '\''
        # insert sensor information into table
        try:
            cursor.execute(f"INSERT INTO {table_name}({','.join(table_columns)}) VALUES ({value});")
        except:
            print('An exception occured - maybe the sentence was to short. Try again.')

# get latest table content
cursor.execute(f'SELECT * FROM {table_name}')

# print table
for i, record in enumerate(cursor):
    print('\n', record)


# commit db changes
conn.commit()
print('changes committed')

# close the cursor
cursor.close()
print('cursor closed')

# close the connection
conn.close()
print('connection closed')

print('END')
