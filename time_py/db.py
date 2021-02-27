import psycopg2 as pg

conn_db = pg.connect(
    user = "postgres",
    password = "shuvo56761676",
    host = "127.0.0.1", # or localhost
    port = "5432",
    database = "vms_postgreSQL"
)
print("Connected (PostgreSQL) database! \nThank you! \n")

cur_db = conn_db.cursor() # here is cur one kind fo class type variable
#print(type(cur))
cur_db.execute("insert into check_in(id,name,purpose) values(202,'nurnobi hossain','kaje')")
conn_db.commit()
cur_db.execute("SELECT * from check_in")
rows = cur_db.fetchall()

for row in rows:
    print("ID : ",row[0])
    print("Name : ", row[1])
    print("Purpose : ",row[2])
    print('\n')

print("INSERT Query successful executed!")
conn_db.close()
