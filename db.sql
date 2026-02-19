-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: opti_db
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mangosihana`
--

DROP TABLE IF EXISTS `mangosihana`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mangosihana` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `kncskjhewjhC` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mangosihana`
--

LOCK TABLES `mangosihana` WRITE;
/*!40000 ALTER TABLE `mangosihana` DISABLE KEYS */;
/*!40000 ALTER TABLE `mangosihana` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opti`
--

DROP TABLE IF EXISTS `opti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opti` (
  `id_employee` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `number` varchar(50) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `rfid` varchar(45) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_employee`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opti`
--

LOCK TABLES `opti` WRITE;
/*!40000 ALTER TABLE `opti` DISABLE KEYS */;
INSERT INTO `opti` VALUES (1,'Paolo',20,'m','paolo@gmail.com','321','123','D1 95 1A 1C',NULL),(2,'rutz',19,'m','jeriel@gmail.com','093','123','00 8D BB 1C',NULL),(3,'banner',20,NULL,NULL,NULL,NULL,NULL,NULL),(5,'paolo',56,'f','asdf','099',NULL,'kjsdi',NULL),(22,'paolo',20,'m','asdf','099',NULL,'kjsdi',NULL),(23,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `opti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opti_admin_db`
--

DROP TABLE IF EXISTS `opti_admin_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opti_admin_db` (
  `id_admin` int NOT NULL AUTO_INCREMENT,
  `admin_name` varchar(45) DEFAULT NULL,
  `admin_password` varchar(45) DEFAULT NULL,
  `admin_rfid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opti_admin_db`
--

LOCK TABLES `opti_admin_db` WRITE;
/*!40000 ALTER TABLE `opti_admin_db` DISABLE KEYS */;
INSERT INTO `opti_admin_db` VALUES (1,'Paolo','123',NULL);
/*!40000 ALTER TABLE `opti_admin_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opti_rec`
--

DROP TABLE IF EXISTS `opti_rec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opti_rec` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_employee` varchar(45) DEFAULT NULL,
  `time_in` datetime DEFAULT NULL,
  `time_out` datetime DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `total_present` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opti_rec`
--

LOCK TABLES `opti_rec` WRITE;
/*!40000 ALTER TABLE `opti_rec` DISABLE KEYS */;
INSERT INTO `opti_rec` VALUES (1,'',NULL,NULL,NULL,NULL,NULL),(2,NULL,NULL,NULL,NULL,NULL,NULL),(3,NULL,NULL,NULL,NULL,NULL,NULL),(4,NULL,NULL,NULL,NULL,NULL,NULL),(5,'1','2026-02-18 08:15:13','2026-02-18 08:16:48',1,5,NULL),(6,'2','2026-02-18 14:00:19','2026-02-18 14:04:07',3,15,NULL),(7,'1',NULL,NULL,NULL,NULL,NULL),(8,'2',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `opti_rec` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-19 23:00:39
