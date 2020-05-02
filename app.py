from database import dbConnection

db = dbConnection()

# DROP weather table
query = "DROP TABLE IF EXISTS weather;"
print(query)
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
print(query)
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
    print(query)
    cursor.execute(query)
db.commit()
cursor.close()

# DROP asthmaFactors table
query = "DROP TABLE IF EXISTS asthmaFactors;"
print(query)
cursor = db.cursor()
cursor.execute(query)
db.commit()
cursor.close()

# CREATE asthmaFactors table
query =\
  "CREATE TABLE `asthmaFactors` (\
  `name` VARCHAR(15) NOT NULL,\
  `january1` TINYINT,\
  `january2` TINYINT,\
  `january3` TINYINT,\
  `february1` TINYINT,\
  `february2` TINYINT,\
  `february3` TINYINT,\
  `march1` TINYINT,\
  `march2` TINYINT,\
  `march3` TINYINT,\
  `april1` TINYINT,\
  `april2` TINYINT,\
  `april3` TINYINT,\
  `may1` TINYINT,\
  `may2` TINYINT,\
  `may3` TINYINT,\
  `june1` TINYINT,\
  `june2` TINYINT,\
  `june3` TINYINT,\
  `july1` TINYINT,\
  `july2` TINYINT,\
  `july3` TINYINT,\
  `august1` TINYINT,\
  `august2` TINYINT,\
  `august3` TINYINT,\
  `september1` TINYINT,\
  `september2` TINYINT,\
  `september3` TINYINT,\
  `october1` TINYINT,\
  `october2` TINYINT,\
  `october3` TINYINT,\
  `november1` TINYINT,\
  `november2` TINYINT,\
  `november3` TINYINT,\
  `december1` TINYINT,\
  `december2` TINYINT,\
  `december3` TINYINT,\
  PRIMARY KEY (`name`)\
);"
print(query)
cursor = db.cursor()
cursor.execute(query)
db.commit()
cursor.close()

# INSERT values from file
asthmaFactorsFilePath = "./asthma_factors_history.txt"
cursor = db.cursor()
f = open(asthmaFactorsFilePath, "r")
for line in f: 
    line = line.split()
    data = '\"' + line[0] + '\"'
    for el in range(1,len(line)):
      data += ("," + line[el])
    query = 'INSERT INTO asthmaFactors VALUES (' + data + ');'
    print(query)
    cursor.execute(query)
db.commit()
cursor.close()

