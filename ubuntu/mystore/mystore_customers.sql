-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: mystore
-- ------------------------------------------------------
-- Server version	8.0.19-0ubuntu0.19.10.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES UTF8MB4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--
use mystore;

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `CustomerID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) COLLATE utf8mb4_danish_ci NOT NULL,
  `Address` varchar(45) COLLATE utf8mb4_danish_ci NOT NULL,
  `City` varchar(45) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `State` varchar(45) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `Zip` varchar(45) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `Phone` varchar(45) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `Email` varchar(45) COLLATE utf8mb4_danish_ci NOT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;
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

-- Dump completed on 2020-04-21 10:59:35
