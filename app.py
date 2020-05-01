from database import dbConnection
from database import truncateTableNamed
from database import printTableNamed

db = dbConnection()

# DROP weather table
query = "DROP TABLE IF EXISTS weather;"
cursor = db.cursor()
cursor.execute(query)
db.commit()
cursor.close()

# CREATE weather table
query =\
"CREATE TABLE `weather` (\
  `date` DATE NOT NULL,\
  `temperature` FLOAT,\
  `humidity` FLOAT,\
  `wind` FLOAT,\
  `rain` FLOAT,\
  PRIMARY KEY (`date`)\
);"
cursor = db.cursor()
cursor.execute(query)
db.commit()
cursor.close()

# INSERT values from file
weatherFilePath = "./weather_history.txt"
cursor = db.cursor()
f = open(weatherFilePath, "r")
header = f.readline()
for line in f: 
    record = line.split()
    query = 'INSERT INTO weather (date, temperature, humidity, wind, rain)\
        VALUES ("{0}", {1}, {2}, {3}, {4});'.format(record[0], record[2], record[5], record[8], record[13])
    cursor.execute(query)
db.commit()
cursor.close()

