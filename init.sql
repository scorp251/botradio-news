-- MySQL dump 10.14  Distrib 5.5.60-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: botradio_news
-- ------------------------------------------------------
-- Server version	5.5.60-MariaDB

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
-- Table structure for table `article_tags`
--

DROP TABLE IF EXISTS `article_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_tags` (
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  KEY `tagid_idx` (`tag_id`),
  KEY `articleid_idx` (`article_id`),
  CONSTRAINT `tagid` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `articleid` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_tags`
--

LOCK TABLES `article_tags` WRITE;
/*!40000 ALTER TABLE `article_tags` DISABLE KEYS */;
INSERT INTO `article_tags` VALUES (2,1),(2,3);
/*!40000 ALTER TABLE `article_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `body` text NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

#LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
#INSERT INTO `articles` VALUES (1,'Small title for 1','This is the body of news article. \nTry something to print.','google.com',NULL,NULL,NULL),(2,'Cisco исправила 32 уязвимости в своих продуктах','В среду, 5 сентября, компания Cisco выпустила обновления безопасности, исправляющие 32 уязвимости в ее продуктах. Три из них обозначены как критические, в том числе нашумевшая уязвимость CVE-2018-11776 в Apache Struts, активно эксплуатируемая в реальных кибератаках. Остальные две затрагивают Cisco Umbrella API, а также интерфейс управления маршрутизаторами Cisco RV110W, RV130W и RV215W.\n\nИз оставшихся 29 уязвимостей 14 обозначены как высоко опасные и 15 – как средней опасности. Проблемы были исправлены в Cisco Routers, Cisco Webex, Cisco Umbrella, Cisco SD-WAN Solution, Cisco Cloud Services Platform, Cisco Data Center Network и других продуктах компании.\n\nОбнаруженная в прошлом месяце уязвимость CVE-2018-11776 затрагивает ядро Apache Struts и позволяет удаленно выполнить код. Проблема существует из-за отсутствия надлежащей проверки ядром вводимых пользователями данных при определенных конфигурациях фреймворка. Уязвимость была исправлена производителем в версиях Apache Struts 2.3.35 и 2.5.17, и теперь она также устранена в продуктах Cisco (с полным списком продуктов можно ознакомиться здесь ).\n\nВторая исправленная Cisco критическая уязвимость (CVE-2018-0435) затрагивает Cisco Umbrella API. Cisco Umbrella представляет собой облачную платформу для обеспечения безопасности, выполняющую функции первой линии защиты портов и протоколов путем блокировки вредоносных доменов, URL, IP-адресов и файлов до установления подключения или загрузки. Проблема существует из-за неэффективных настроек аутентификации в интерфейсе Cisco Umbrella API.\n\nТретья уязвимость (CVE-2018-0423) затрагивает web-интерфейс управления маршрутизаторами Cisco RV110W Wireless-N VPN Firewall, Cisco RV130W Wireless-N Multifunction VPN Router и Cisco RV215W Wireless-N VPN Router. С ее помощью злоумышленник может выполнить произвольный код или вызвать отказ в обслуживании.\n','https://www.securitylab.ru/news/495509.php',NULL,NULL,NULL);
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
#UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

#LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
#INSERT INTO `tags` VALUES (1,'Seclab'),(2,'Opennet'),(3,'Безопасность'),(4,'Статьи'),(5,'Всяко-Разно');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
#UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 16:42:27
