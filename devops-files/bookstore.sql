-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: bookstore
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(25) COLLATE utf8_danish_ci NOT NULL,
  `lastname` varchar(25) COLLATE utf8_danish_ci NOT NULL,
  `mail` varchar(25) COLLATE utf8_danish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Adrian','Kingsley Hughes','KingsleyHughes@mail.com'),(2,'Alex','Federov','Federov@mail.com'),(3,'Alex','Homer','Homer@mail.com'),(4,'Alex','Stockton','Stockton@mail.com'),(5,'Alexander','Nakhimovsky','Nakhimovsky@mail.com'),(6,'Andrea','Chiarelli','Chiarelli@mail.com'),(7,'Andrew','Enfield','Enfield@mail.com'),(8,'Brian','Francis','Francis@mail.com'),(9,'Brian','Matsik','Matsik@mail.com'),(10,'Bruce','Hartwell','Hartwell@mail.com'),(11,'Chris','Ullman','Ullman@mail.com'),(12,'Christian','Gross','Gross@mail.com'),(13,'Craig','McQueen','McQueen@mail.com'),(14,'Dan','Denault','Denault@mail.com'),(15,'Darren','Gill','Gill@mail.com'),(16,'Dave','Jewell','Jewell@mail.com'),(17,'David','Busar','Busar@mail.com'),(18,'David','Sussman','Sussman@mail.com'),(19,'Dino','Esposito','Esposito@mail.com'),(20,'Duncan','Mackenzie','Mackenzie@mail.com'),(21,'Dwayne','Gifford','Gifford@mail.com'),(22,'Felipe','Martins','Martins@mail.com'),(23,'Frank','Boumphrey','Boumphrey@mail.com'),(24,'George','Reilly','Reilly@mail.com'),(25,'Ian','Blackburn','Blackburn@mail.com'),(26,'Ivor','Horton','Horton@mail.com'),(27,'Jake','Sturm','Sturm@mail.com'),(28,'James','Conard','Conard@mail.com'),(29,'Jesse','Liberty','Liberty@mail.com');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookorders`
--

DROP TABLE IF EXISTS `bookorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookorders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `orderdate` date NOT NULL,
  `shipdate` date DEFAULT NULL,
  `invoice` int(11) DEFAULT NULL,
  `shipby` varchar(10) COLLATE utf8_danish_ci DEFAULT NULL,
  `paydate` date DEFAULT NULL,
  `paymethod` varchar(20) COLLATE utf8_danish_ci DEFAULT NULL,
  `invoicedate` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer` (`customer_id`),
  CONSTRAINT `customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookorders`
--

LOCK TABLES `bookorders` WRITE;
/*!40000 ALTER TABLE `bookorders` DISABLE KEYS */;
INSERT INTO `bookorders` VALUES (1,8,'2012-04-18','2012-04-22',23,'','0000-00-00','AMEX','0000-00-00'),(2,11,'2012-02-25','2012-03-03',24,'','0000-00-00','Visa','0000-00-00'),(3,4,'2012-05-01','2012-05-05',25,'','0000-00-00','Mastercard','0000-00-00'),(4,6,'2012-05-01','2012-05-06',26,'','0000-00-00','Visa','0000-00-00'),(5,18,'2012-06-14','2012-06-25',27,'','0000-00-00','Paypal','0000-00-00'),(6,23,'2012-06-24','2012-06-25',28,'','0000-00-00','Paypal','0000-00-00'),(7,4,'2012-06-24','2012-06-25',29,'','0000-00-00','Visa','0000-00-00'),(8,18,'2012-07-01','2012-07-08',30,'','0000-00-00','AMEX','0000-00-00'),(9,23,'2012-07-07','2012-07-09',31,'','0000-00-00','AMEX','0000-00-00'),(10,8,'2012-07-10','2012-07-14',55,'','0000-00-00','Visa','0000-00-00'),(11,27,'2014-07-10','2014-07-14',55,'','0000-00-00','Visa','0000-00-00');
/*!40000 ALTER TABLE `bookorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) DEFAULT NULL,
  `title` varchar(70) COLLATE utf8_danish_ci NOT NULL,
  `published` date NOT NULL,
  `bookprice` decimal(8,2) NOT NULL,
  `isbn` varchar(10) COLLATE utf8_danish_ci DEFAULT NULL,
  `onhand` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `authors` (`author_id`),
  CONSTRAINT `authors` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,2,'ASP 2.0 Programmers Reference','2009-12-01',19.99,'1861002459',12),(2,2,'Professional Active Server Pages 2.0','2009-03-01',55.49,'1861001266',55),(3,3,'XML In IE5 Programmers Reference','2009-03-01',44.95,'1861001576',61),(4,4,'ADO 2.0 Programmers Reference','2009-09-06',27.99,'1861001835',62),(5,5,'Beginners Guide To Access 97','2009-12-01',32.99,'1874416826',26),(6,7,'Beginning WordBasic Programming','2009-07-01',39.95,'1874416869',23),(7,3,'Instant IE4 Dynamic Html Programmers Reference','1997-09-01',22.99,'1861000685',58),(8,7,'Instant Activex Web Database','2009-01-01',41.95,'1861000464',76),(9,3,'IE5 Dynamic HTML Programmers Reference','1999-05-01',22.99,'1861001746',54),(10,3,'Alex Homers Professional ASP Web Techniques','2000-02-01',35.99,'1861003218',54),(11,3,'ASP Programmers Resource Kit','1999-02-01',110.99,'1861002368',54),(12,3,'Professional ASP Techniques For Webmasters','1998-08-06',49.99,'1861001797',74),(13,3,'Professional ASP.NET','2001-04-01',78.08,'1861004885',15),(14,5,'Javascript Objects','2009-11-20',59.95,'1861001894',15),(15,5,'Professional Java Xml Programming With Servlets An','1999-12-01',49.99,'1861002858',54),(16,8,'Professional Active Server Pages','1997-05-01',41.49,'1861000723',45),(17,11,'Instant Netscape4 Dynamic Html Programmers Refere','1997-08-01',22.99,'1861001193',45),(18,11,'Beginning Active Server Pages 3.0','1999-12-01',28.99,'1861003382',54),(19,12,'Professional SQL Server 6.5 Administration','1996-09-01',62.95,'1874416494',58),(20,14,'ASP 3.0 Programmers Reference','2000-03-01',34.99,'1861003234',12),(21,15,'Instant VB Script','1996-11-01',35.00,'1861000448',56),(22,16,'Instant Delphi Programming','1995-03-01',24.95,'1874416575',61),(23,16,'Instant Visual Basic 5 Activex Control Programming','1997-01-01',27.99,'1861000235',62),(24,18,'Beginning Access 97 VBA Programming','1997-09-01',55.95,'1861000863',26),(25,18,'Beginning Access 2000 VBA Programming','1999-05-01',39.99,'1861001762',23),(26,18,'Professional MTS & MSMQ Programming With VB And AS','1998-05-01',46.99,'1861001460',58),(27,18,'A Preview of Active Server Pages+','2000-07-01',52.95,'1861004753',76),(28,18,'ADO 2.1 Programmers Reference','1999-06-01',29.99,'1861002688',54),(29,19,'Visual C++ Windows Shell Programming','1998-12-01',39.99,'1861001843',54),(30,19,'Instant DHTML Scriplets','1998-03-01',29.95,'1861001843',54),(31,19,'Windows Script Host Programmers Reference','1999-06-01',21.99,'1861002653',74),(32,19,'Professional IE4 Programming','1997-10-29',49.95,'1861000707',15),(33,21,'Outlook 2000 VBA Programmers Reference','1999-05-01',17.99,'1861000707',15),(34,21,'Office 2000 Programmers Resource Kit','1999-06-01',89.95,'1861003005',54),(35,22,'Word 2000 VBA Programmers Reference','1999-05-01',37.95,'1861002556',45),(36,22,'Excel 2000 VBA Programmers Reference','1999-05-01',37.95,'1861002548',45),(37,23,'Professional Style Sheets For HTML And XML','1998-06-01',36.99,'1861001657',54),(38,25,'Professional ADO 2.5 Programming','2000-02-01',89.95,'1861002750',58),(39,26,'Beginners Guide To C','1994-09-01',27.95,'1861002750',12),(40,26,'Beginning Visual C++ 6','1998-08-20',49.99,'186100088X',56),(41,26,'Beginners Guide To Win Prog. With Turbo C++ Visual','1995-03-01',41.95,'1874416532',61),(42,26,'Beginning Java 2 - JDK 1.3 Version','2000-03-01',35.99,'1861003668',62),(43,26,'Beginning Visual C++ 6.0 Compiler Edition','1999-01-01',57.49,'1861001967',26),(44,26,'Beginning Java 2.0','1999-02-01',49.99,'1861002238',23),(45,26,'Beginning Visual C++ 5 Programming','1997-03-01',39.95,'1861000081',58),(46,26,'Instant C Programming','1995-08-01',24.95,'1874416249',76),(47,26,'Beginning Java 1.1','1997-06-01',36.99,'1861000278',54),(48,26,'Beginning Visual C++ 4.0','1996-03-01',36.95,'1874416591',54),(49,26,'Beginning C 2nd Ed.','1997-08-01',29.95,'1861001142',54);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_danish_ci NOT NULL,
  `city` varchar(25) COLLATE utf8_danish_ci NOT NULL,
  `state` varchar(25) COLLATE utf8_danish_ci DEFAULT NULL,
  `country` varchar(25) COLLATE utf8_danish_ci DEFAULT NULL,
  `mail` varchar(25) COLLATE utf8_danish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Colin Forbes','Denver','Colorado','USA','forbes@anymail.com'),(2,'Robert Duncan','Redmond','Washington','USA','duncan@anymail.com'),(3,'Alfred Coppel','Malibu','California','USA','coppel@anymail.com'),(4,'Irwin Shaw','Stormond','South Dakota','USA','shaw@anymail.com'),(5,'Sidney Sheldon','Miami','Florida','USA','sheldon@anymail.com'),(6,'Jeffrey Archer','Las Vegas','Nevada','USA','archer@anymail.com'),(7,'Frederich Forsyth','Hollywood','California','USA','forsyth@anymail.com'),(8,'Brian Garfield','Redmond','Washington','USA','garfield@anymail.com'),(9,'Leon Uris','Solvang','California','USA','uris@anymail.com'),(10,'John Kruse','Indianapolis','Indiana','USA','kruse@anymail.com'),(11,'Gerorge Markstein','Maersk City','North Carolina','USA','markstein@anymail.com'),(12,'Nicolas Fawcett','Jones Town','Illinois','USA','fawcett@anymail.com'),(13,'Donald Seamann','Culver City','Colorado','USA','seamann@anymail.com'),(14,'Vivek Chopra','Redmond','Washington','USA','chopra@anymail.com'),(15,'Jeff Genender','Indianapolis','Indiana','USA','genender@anymail.com'),(16,'Anna Pihl Johnsen','Jones Town','Illinois','USA','johnsen@anymail.com'),(17,'Ingrid Dahl','Malibu','California','USA','dahl@anymail.com'),(18,'Jeremy McPeak','Indianapolis','Indiana','USA','jeremy@anymail.com'),(19,'Anthony Cage','Metropolis','Ohio','USA','anthony@anymail.com'),(20,'Brian McEnroe','Bourgainville','Indiana','USA','brianenroe@anymail.com'),(21,'Paul W. Jones','Providence','California','USA','pwjones@anymail.com'),(22,'Monique Bolton','Paris','Provance','France','monique@anymail.com'),(23,'amalie tristan','Bourgainville','Provance','France','amalie@mail.fr'),(24,'pieter tristan','Bourgainville','Provance','France','pieter@mail.fr'),(25,'anthony willis','demolition city','North Carolina','USA','anthony@anymail.nu'),(26,'bolette poulsen','animal farm','Anatolien','Turkey','bolette@poulsen.nu'),(27,'jeanette poulsen','animal farm','Anatolien','Turkey','jeanette@poulsen.nu'),(28,'Marc poulsen','animal farm','Anatolien','Turkey','marc@poulsen.nu'),(29,'christina masterson','petersbourgh','pensylvania','USA','christina@masterson.nu');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderlines`
--

DROP TABLE IF EXISTS `orderlines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderlines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookorder_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `numbooks` int(11) NOT NULL,
  `title` varchar(70) COLLATE utf8_danish_ci NOT NULL,
  `salesprice` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bookorder` (`bookorder_id`),
  KEY `book` (`book_id`),
  CONSTRAINT `book` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `bookorder` FOREIGN KEY (`bookorder_id`) REFERENCES `bookorders` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderlines`
--

LOCK TABLES `orderlines` WRITE;
/*!40000 ALTER TABLE `orderlines` DISABLE KEYS */;
INSERT INTO `orderlines` VALUES (1,1,3,1,'XML In IE5 Programmers Reference',44.95),(2,1,8,1,'Instant Activex Web Database',41.95),(3,1,49,1,'Beginning C 2nd Ed.',48.95),(4,1,16,1,'Professional Active Server Pages',41.99),(5,1,22,2,'Instant Delphi Programming',24.95),(6,2,8,3,'Instant Activex Web Database',41.95),(7,2,9,4,'IE5 Dynamic HTML Programmers Reference',22.99),(8,2,39,8,'Beginners Guide To C',112.95),(9,2,7,4,'Instant IE4 Dynamic Html Programmers Reference',22.99),(10,2,47,7,'Beginning Java 1.1',32.49),(11,3,9,4,'IE5 Dynamic HTML Programmers Reference',22.99),(12,3,17,4,'Instant Netscape4 Dynamic Html Programmers Refere',22.99),(13,3,32,7,'Professional IE4 Programming',49.99),(14,3,7,1,'Instant IE4 Dynamic Html Programmers Reference',22.99),(15,3,39,1,'Beginners Guide To C',27.95),(16,4,17,1,'Instant Netscape4 Dynamic Html Programmers Refere',22.99),(17,4,32,1,'Professional IE4 Programming',49.99),(18,4,7,1,'Instant IE4 Dynamic Html Programmers Reference',22.99),(19,4,39,4,'Beginners Guide To C',27.95),(20,5,18,2,'Beginning Active Server Pages 3.0',28.99),(21,5,32,3,'Professional IE4 Programming',49.99),(22,5,7,4,'Instant IE4 Dynamic Html Programmers Reference',22.99),(23,5,39,3,'Beginners Guide To C',27.95),(24,6,18,5,'Beginning Active Server Pages 3.0',28.99),(25,6,39,7,'Beginners Guide To C',27.95),(26,6,32,4,'Professional IE4 Programming',49.99),(27,6,22,2,'Instant Delphi Programming',24.95),(28,6,47,4,'Beginning Java 1.1',32.49),(29,7,45,1,'Beginning Visual C++ 5 Programming',39.95),(30,7,16,4,'Professional Active Server Pages',41.99),(31,7,22,2,'Instant Delphi Programming',24.95),(32,7,28,7,'ADO 2.1 Programmers Reference',29.95),(33,8,45,9,'Beginning Visual C++ 5 Programming',39.95),(34,8,16,3,'Professional Active Server Pages',41.99),(35,8,22,3,'Instant Delphi Programming',24.95),(36,8,28,6,'ADO 2.1 Programmers Reference',29.95),(37,9,39,2,'Beginners Guide To C',48.95),(38,9,16,1,'Professional Active Server Pages',41.99),(39,9,47,1,'Beginning Java 1.1',32.49),(40,10,21,3,'Instant VB Script',35.99),(41,11,14,4,'Javascript Objects',59.99);
/*!40000 ALTER TABLE `orderlines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-17 18:06:05
