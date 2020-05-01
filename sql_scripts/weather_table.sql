DROP TABLE IF EXISTS weather;

CREATE TABLE `weather` (
  `date` DATE NOT NULL,
  `temperature` FLOAT,
  `humidity` FLOAT,
  `wind` FLOAT,
  `rain` FLOAT,
  PRIMARY KEY (`date`)
);

SHOW TABLES;

INSERT INTO weather (date, temperature, humidity, wind, rain) VALUES ("2018-09-13", 0, 0, 0, 0);

SELECT * FROM weather;

