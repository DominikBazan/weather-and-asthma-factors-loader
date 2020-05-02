DROP TABLE IF EXISTS asthmaFactors;

CREATE TABLE `asthmaFactors` (
  `name` VARCHAR(15) NOT NULL,
  `january1` TINYINT,
  `january2` TINYINT,
  `january3` TINYINT,
  `february1` TINYINT,
  `february2` TINYINT,
  `february3` TINYINT,
  `march1` TINYINT,
  `march2` TINYINT,
  `march3` TINYINT,
  `april1` TINYINT,
  `april2` TINYINT,
  `april3` TINYINT,
  `may1` TINYINT,
  `may2` TINYINT,
  `may3` TINYINT,
  `june1` TINYINT,
  `june2` TINYINT,
  `june3` TINYINT,
  `july1` TINYINT,
  `july2` TINYINT,
  `july3` TINYINT,
  `august1` TINYINT,
  `august2` TINYINT,
  `august3` TINYINT,
  `september1` TINYINT,
  `september2` TINYINT,
  `september3` TINYINT,
  `october1` TINYINT,
  `october2` TINYINT,
  `october3` TINYINT,
  `november1` TINYINT,
  `november2` TINYINT,
  `november3` TINYINT,
  `december1` TINYINT,
  `december2` TINYINT,
  `december3` TINYINT,
  PRIMARY KEY (`name`)
);

SHOW TABLES;

INSERT INTO asthmaFactors VALUES ("plant",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);

SELECT * FROM asthmaFactors;

