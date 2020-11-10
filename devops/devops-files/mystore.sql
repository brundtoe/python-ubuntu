-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: mystore
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `au_id` varchar(11) NOT NULL DEFAULT '',
  `au_lname` varchar(40) DEFAULT NULL,
  `au_fname` varchar(20) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `zip` varchar(5) DEFAULT NULL,
  `contract` tinyint(1) NOT NULL,
  PRIMARY KEY (`au_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES ('172-32-1176','White','Johnson','408 496-7223','10932 Bigge Rd.','Menlo Park','CA','94025',1),('213-46-8915','Green','Marjorie','415 986-7020','309 63rd St. #411','Oakland','CA','94618',1),('238-95-7766','Carson','Cheryl','415 548-7723','589 Darwin Ln.','Berkeley','CA','94705',1),('267-41-2394','O\'Leary','Michael','408 286-2428','22 Cleveland Av. #14','San Jose','CA','95128',1),('274-80-9391','Straight Jr.','Dean','415 834-3929','5420 College Av.','Oakland','CA','94609',1),('341-22-1782','Smith','Meander','913 843-0462','10 Mississippi Dr.','Lawrence','KS','66044',0),('409-56-7008','Bennet','Abraham','415 658-9932','6223 Bateman St.','Berkeley','CA','94705',1),('427-17-2319','Dull','Ann','415 836-7128','3410 Blonde St.','Palo Alto','CA','94301',1),('472-27-2349','Gringlesby','Burt','707 938-6445','PO Box 792','Covelo','CA','95428',1),('486-29-1786','Locksley Jr.','Charlene','415 585-4620','18 Broadway Av.','San Francisco','CA','94130',1),('527-72-3246','Greene','Morningstar','615 297-2723','22 Graybar House Rd.','Nashville','TN','37215',0),('648-92-1872','Blotchet-Halls','Reginald','503 745-6402','55 Hillsdale Bl.','Corvallis','OR','97330',1),('672-71-3249','Yokomoto','Akiko','415 935-4228','3 Silver Ct.','Walnut Creek','CA','94595',1),('712-45-1867','del Castillo','Innes','615 996-8275','2286 Cram Pl. #86','Ann Arbor','MI','48105',1),('722-51-5454','DeFrance','Michel','219 547-9982','3 Balding Pl.','Gary','IN','46403',1),('724-08-9931','Stringer','Dirk','415 843-2991','5420 Telegraph Av.','Oakland','CA','94609',0),('724-80-9391','MacFeather','Stearns','415 354-7128','44 Upland Hts.','Oakland','CA','94612',1),('756-30-7391','Karsen','Livia','415 534-9219','5720 McAuley St.','Oakland','CA','94609',1),('807-91-6654','Panteley','Sylvia','301 946-8853','1956 Arlington Pl.','Rockville','MD','20853',1),('846-92-7186','Hunter','Sheryl','415 836-7128','3410 Blonde St.','Palo Alto','CA','94301',1),('893-72-1158','McBadden','Heather','707 448-4982','301 Putnam','Vacaville','CA','95688',0),('899-46-2035','Ringer','Anne','801 826-0752','67 Seventh Av.','Salt Lake City','UT','84152',1),('998-72-3567','Ringer','Albert','801 826-0752','67 Seventh Av.','Salt Lake City','UT','84152',1);
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `CustomerID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `City` varchar(45) DEFAULT NULL,
  `State` varchar(45) DEFAULT NULL,
  `Zip` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Colin Forbes','Primary Road 23','Denver','Colorado','34567','(555) 4945 38475','forbes@anymail.com'),(2,'Robert Duncan','Duane Street 45','Redmond','Washington','68790','(555) 3485 04864','duncan@anymail.com'),(3,'Alfred Coppel','Haalson Avenue 66','Malibu','California','87646','(555) 3985 09815','coppel@anymail.com'),(4,'Irwin Shaw','Redwood Street 89','Stormond','South Dakota','74504','(555) 8715 15907','shaw@anymail.com'),(5,'Sidney Sheldon','White Bull Street 98','Miami','Florida','35875','(555) 9754 08753','sheldon@anymail.com'),(6,'Evelyn Anthony','Hollow Road 87','Houston','Texas','89162','(555) 9781 90435','anthony@anymail.com'),(7,'Jeffrey Archer','Forrest Road 76','Las Vegas','Nevada','76557','(555) 4587 90751','archer@anymail.com'),(8,'Frederich Forsyth','Sunset Boulevard 65','Hollywood','California','76452','(555) 3575 87025','forsyth@anymail.com'),(9,'Brian Garfield','Duane Street 54','Redmond','Washington','68790','(555) 3485 04938','garfield@anymail.com'),(10,'Leon Uris','Soldier Street','Solvang','California','89740','(444) 9749 98744','uris@anymail.com'),(11,'John Kruse','Struts Avenue','Indianapolis','Langeland','34756','(444) 5762 83593','kruse@anymail.com'),(12,'Gerorge Markstein','Container Road','Maersk City','North Carolina','34598','(333) 3472 97435','markstein@anymail.com'),(13,'Nicolas Fawcett','McPeak Road','Jones Town','Illinois','34756','(444) 4576 97598','fawcett@anymail.com'),(14,'Donald Seamann','Marking Street','Culver City','Colorado','23763','(333) 4875 97154','seamann@anymail.com'),(15,'Vivek Chopra','Duane Street 88','Redmond','Washington','68790','(333) 3485 97535','chopra@anymail.com'),(16,'Jeff Genender','Apache Road','Indianapolis','Indiana','34756','(444) 5762 98075','genender@anymail.com'),(17,'Anna Pihl Johnsen','Wrox Avenue','Jones Town','Illinois','34756','(444) 4576 98505','johnsen@anymail.com'),(18,'Ingrid Dahl','Provincial Avenue','Malibu','California','92472','(555) 4576 98357','dahl@anymail.com'),(19,'Jeremy McPeak','Crosspoint Boulevard 345','Indianapolis','IN','46256','(555) 3475 58722','jeremy@anymail.com'),(20,'Anthony Cage','Birds Nest 33','Metropolis','ME','34567','456 5867 3743','anthony@anymail.com'),(21,'Brian McEnroe','Center Court 1','Bourgainville','BG','23496','666 6788 3958','brianenroe@anymail.com'),(22,'Paul W. Jones','Pilkington Ave 3','Providence','PR','34986','457 9457 39842','pwjones@anymail.com'),(23,'Monique Bolton','Estelle Lauder Ave 22','Paris','France','37476','234 4975 89723','monique@anymail.com'),(24,'amalie tristan','Birds Nest 33','Bourgainville','France','23496','234 4975 89723','amalie@mail.fr'),(25,'pieter tristan','Birds Nest 33','Bourgainville','France','23496','234 4975 89723','amalie@mail.fr'),(26,'anthony willis','demitec road 34','demolition city','North Carolina','34746','25757 254','anthony@anymail.nu'),(27,'bolette poulsen','pullard road 2','animal farm','turkey','87598','225 577','bolette@poulsen.nu'),(28,'jeanette poulsen','pullard road 2','animal farm','turkey','44342','54657 57745','jeanette@poulsen.nu'),(29,'Marc poulsen','pullard road 2','animal farm','turkey','23422','4572 45747','marc@poulsen.nu'),(30,'christina masterson','bond street 007','petersbourgh','pensylvania','24747','45777 57','christina@masterson.nu'),(31,'cecilie bundgaard','tobaco road 34','toombstone','colorado','45757','6787 57574','cecilie@bundgaard.nu'),(32,'Erwin bundgaard','tobaco road 34','toombstone','colorado','57288','54574 457','erwin@bundgaard.nu'),(33,'martha bundgaard','tobaco road 34','toombstone','colorado','45718','457 9457 39842','martha@bundgaard.nu'),(34,'Cathrine Johnsson','Green Forrest Lane 2','Aidensfield','Nevada','37465','555 68758 3874','cathrine@anymail.com'),(35,'Maria Olsen','Bygaden 33','Helsinge','Ohio','34567','555 8675 84732','maria@olsen.com'),(36,'Mario Brothers','Marvel Street 56','Cartoon Wood','Minnesota','45678','555 8576 38472','mario@brothers.nu'),(37,'Mario Brothers','Marvel Street 56','Cartoon Wood','Minnesota','45678','555 8576 38472','mario@brothers.nu'),(38,'Jakob Olsen','Randersgade 3','Horsens','Midtjylland','2345','555 6875','jacob@olsen.nu'),(39,'Martina Svendsen','Bygaden 56','Holme Olstrup','Sjælland','3456','555 9475 29874','martina@svendsen.nu'),(40,'Julie Bertelsen','Skovbrynet 23','Hareskoven','Nordsjælland','3455','444 8576 38472','julie@bertelsen.nu'),(41,'Karl Stegger','Skovstien','Syvhuse','California','2345','555 687456','karl@stegger.nu'),(42,'Monique Bolton','Estelle Lauder Ave 22','Paris','France','2345','234 4975 89723','monique@anymail.com'),(43,'Asger Hansen','Frydenlundsvej 23','Reno','AZ','34564','555 9876 98765','asger@anymail.com'),(44,'Maria Hansen','Sunset Boulevrd','Beverly Hills','CA','29260','345 5967 35983','maria@hansen.com'),(45,'Smarty Hansson Jr.','Arlington Road 123','Washington DC','District of Columbia','76543','555-5678-34567','smarty@anymail.com'),(46,'Andreas Christoffersen','Grønlandsvej 456','Nuuk','Green Zone','99999','333-4444-55555','andreas@anymail.com');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-17 18:09:36
