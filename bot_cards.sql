# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.31)
# Database: bot_cards
# Generation Time: 2023-02-27 15:27:09 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table cards
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cards`;

CREATE TABLE `cards` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `type_card` tinyint unsigned NOT NULL,
  `get_point` smallint unsigned NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;

INSERT INTO `cards` (`id`, `type_card`, `get_point`, `url`)
VALUES
	(1,2,500,'cards/Civil/0012.png'),
	(2,2,500,'cards/Civil/0013.png'),
	(3,2,500,'cards/Civil/0011.png'),
	(4,2,500,'cards/Civil/0039.png'),
	(5,2,500,'cards/Civil/0038.png'),
	(6,2,500,'cards/Civil/0010.png'),
	(7,2,500,'cards/Civil/0028.png'),
	(8,2,500,'cards/Civil/0014.png'),
	(9,2,500,'cards/Civil/0015.png'),
	(10,2,500,'cards/Civil/0029.png'),
	(11,2,500,'cards/Civil/0017.png'),
	(12,2,500,'cards/Civil/0016.png'),
	(13,2,500,'cards/Civil/0027.png'),
	(14,2,500,'cards/Civil/0033.png'),
	(15,2,500,'cards/Civil/0032.png'),
	(16,2,500,'cards/Civil/0026.png'),
	(17,2,500,'cards/Civil/0030.png'),
	(18,2,500,'cards/Civil/0024.png'),
	(19,2,500,'cards/Civil/0018.png'),
	(20,2,500,'cards/Civil/0019.png'),
	(21,2,500,'cards/Civil/0025.png'),
	(22,2,500,'cards/Civil/0031.png'),
	(23,2,500,'cards/Civil/0009.png'),
	(24,2,500,'cards/Civil/0035.png'),
	(25,2,500,'cards/Civil/0021.png'),
	(26,2,500,'cards/Civil/0020.png'),
	(27,2,500,'cards/Civil/0034.png'),
	(28,2,500,'cards/Civil/0008.png'),
	(29,2,500,'cards/Civil/0022.png'),
	(30,2,500,'cards/Civil/0036.png'),
	(31,2,500,'cards/Civil/0037.png'),
	(32,2,500,'cards/Civil/0023.png'),
	(33,1,250,'cards/Basic/0065.png'),
	(34,1,250,'cards/Basic/0059.png'),
	(35,1,250,'cards/Basic/0058.png'),
	(36,1,250,'cards/Basic/0064.png'),
	(37,1,250,'cards/Basic/0063.png'),
	(38,1,250,'cards/Basic/0062.png'),
	(39,1,250,'cards/Basic/0048.png'),
	(40,1,250,'cards/Basic/0060.png'),
	(41,1,250,'cards/Basic/0061.png'),
	(42,1,250,'cards/Basic/0049.png'),
	(43,1,250,'cards/Basic/0044.png'),
	(44,1,250,'cards/Basic/0050.png'),
	(45,1,250,'cards/Basic/0051.png'),
	(46,1,250,'cards/Basic/0045.png'),
	(47,1,250,'cards/Basic/0053.png'),
	(48,1,250,'cards/Basic/0047.png'),
	(49,1,250,'cards/Basic/0046.png'),
	(50,1,250,'cards/Basic/0052.png'),
	(51,1,250,'cards/Basic/0056.png'),
	(52,1,250,'cards/Basic/0042.png'),
	(53,1,250,'cards/Basic/0043.png'),
	(54,1,250,'cards/Basic/0057.png'),
	(55,1,250,'cards/Basic/0041.png'),
	(56,1,250,'cards/Basic/0055.png'),
	(57,1,250,'cards/Basic/0054.png'),
	(58,1,250,'cards/Basic/0040.png'),
	(59,3,1000,'cards/Rare/0071.png'),
	(60,3,1000,'cards/Rare/0070.png'),
	(61,3,1000,'cards/Rare/0099.png'),
	(62,3,1000,'cards/Rare/0072.png'),
	(63,3,1000,'cards/Rare/0066.png'),
	(64,3,1000,'cards/Rare/0067.png'),
	(65,3,1000,'cards/Rare/0073.png'),
	(66,3,1000,'cards/Rare/0098.png'),
	(67,3,1000,'cards/Rare/0088.png'),
	(68,3,1000,'cards/Rare/0077.png'),
	(69,3,1000,'cards/Rare/0076.png'),
	(70,3,1000,'cards/Rare/0089.png'),
	(71,3,1000,'cards/Rare/0074.png'),
	(72,3,1000,'cards/Rare/0100.png'),
	(73,3,1000,'cards/Rare/0101.png'),
	(74,3,1000,'cards/Rare/0075.png'),
	(75,3,1000,'cards/Rare/0087.png'),
	(76,3,1000,'cards/Rare/0093.png'),
	(77,3,1000,'cards/Rare/0078.png'),
	(78,3,1000,'cards/Rare/0079.png'),
	(79,3,1000,'cards/Rare/0092.png'),
	(80,3,1000,'cards/Rare/0086.png'),
	(81,3,1000,'cards/Rare/0090.png'),
	(82,3,1000,'cards/Rare/0084.png'),
	(83,3,1000,'cards/Rare/0085.png'),
	(84,3,1000,'cards/Rare/0091.png'),
	(85,3,1000,'cards/Rare/0095.png'),
	(86,3,1000,'cards/Rare/0081.png'),
	(87,3,1000,'cards/Rare/0080.png'),
	(88,3,1000,'cards/Rare/0094.png'),
	(89,3,1000,'cards/Rare/0082.png'),
	(90,3,1000,'cards/Rare/0096.png'),
	(91,3,1000,'cards/Rare/0069.png'),
	(92,3,1000,'cards/Rare/0068.png'),
	(93,3,1000,'cards/Rare/0097.png'),
	(94,3,1000,'cards/Rare/0083.png'),
	(95,4,2500,'cards/Extra/0111.png'),
	(96,4,2500,'cards/Extra/0105.png'),
	(97,4,2500,'cards/Extra/0104.png'),
	(98,4,2500,'cards/Extra/0110.png'),
	(99,4,2500,'cards/Extra/0106.png'),
	(100,4,2500,'cards/Extra/0112.png'),
	(101,4,2500,'cards/Extra/0113.png'),
	(102,4,2500,'cards/Extra/0107.png'),
	(103,4,2500,'cards/Extra/0103.png'),
	(104,4,2500,'cards/Extra/0117.png'),
	(105,4,2500,'cards/Extra/0116.png'),
	(106,4,2500,'cards/Extra/0102.png'),
	(107,4,2500,'cards/Extra/0128.png'),
	(108,4,2500,'cards/Extra/0114.png'),
	(109,4,2500,'cards/Extra/0115.png'),
	(110,4,2500,'cards/Extra/0124.png'),
	(111,4,2500,'cards/Extra/0118.png'),
	(112,4,2500,'cards/Extra/0119.png'),
	(113,4,2500,'cards/Extra/0125.png'),
	(114,4,2500,'cards/Extra/0127.png'),
	(115,4,2500,'cards/Extra/0126.png'),
	(116,4,2500,'cards/Extra/0122.png'),
	(117,4,2500,'cards/Extra/0123.png'),
	(118,4,2500,'cards/Extra/0109.png'),
	(119,4,2500,'cards/Extra/0121.png'),
	(120,4,2500,'cards/Extra/0120.png'),
	(121,4,2500,'cards/Extra/0108.png'),
	(122,5,5000,'cards/Exclusive/0139.png'),
	(123,5,5000,'cards/Exclusive/0138.png'),
	(124,5,5000,'cards/Exclusive/0129.png'),
	(125,5,5000,'cards/Exclusive/0144.png'),
	(126,5,5000,'cards/Exclusive/0145.png'),
	(127,5,5000,'cards/Exclusive/0141.png'),
	(128,5,5000,'cards/Exclusive/0140.png'),
	(129,5,5000,'cards/Exclusive/0142.png'),
	(130,5,5000,'cards/Exclusive/0143.png'),
	(131,5,5000,'cards/Exclusive/0130.png'),
	(132,5,5000,'cards/Exclusive/0131.png'),
	(133,5,5000,'cards/Exclusive/0133.png'),
	(134,5,5000,'cards/Exclusive/0132.png'),
	(135,5,5000,'cards/Exclusive/0136.png'),
	(136,5,5000,'cards/Exclusive/0137.png'),
	(137,5,5000,'cards/Exclusive/0135.png'),
	(138,5,5000,'cards/Exclusive/0134.png');

/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` varchar(20) NOT NULL,
  `points` int NOT NULL DEFAULT '0',
  `attemp` tinyint unsigned DEFAULT '1',
  `balance` smallint unsigned NOT NULL DEFAULT '0',
  `spot_pass` tinyint(1) NOT NULL DEFAULT '0',
  `date_attemp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_cube` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_name` varchar(25) DEFAULT NULL,
  `date_bouling` datetime DEFAULT CURRENT_TIMESTAMP,
  `date_basketball` datetime DEFAULT CURRENT_TIMESTAMP,
  `date_darts` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`user_id`, `points`, `attemp`, `balance`, `spot_pass`, `date_attemp`, `date_cube`, `user_name`, `date_bouling`, `date_basketball`, `date_darts`)
VALUES
	('1265361945',0,0,100,0,'2023-02-27 00:10:40','2023-03-05 16:20:16','anienovak','2023-02-26 16:24:09','2023-02-26 16:24:09','2023-02-26 16:24:09'),
	('346831387',0,0,100,0,'2023-02-26 20:05:30','2023-03-05 16:05:55','LiShox','2023-02-26 16:24:09','2023-02-26 16:24:09','2023-02-26 16:24:09'),
	('408853689',0,0,0,0,'2023-02-27 00:19:38','2023-03-05 15:46:11','zhekagracia','2023-02-27 17:04:13','2023-02-27 17:04:46','2023-02-27 17:05:33'),
	('456406814',0,1,0,0,'2023-02-26 20:35:31','2023-02-26 20:35:31','buckold','2023-02-26 20:35:31','2023-02-26 20:35:31','2023-02-26 20:35:31'),
	('6189180632',0,64,0,0,'2023-02-26 18:58:27','2023-03-05 14:58:36','vladfree1','2023-02-27 16:57:09','2023-02-27 16:47:08','2023-02-27 16:45:45'),
	('633118670',0,4,0,0,'2023-02-27 00:27:09','2023-03-05 20:27:28','Glebaty220','2023-02-26 19:42:18','2023-02-26 19:42:18','2023-02-26 19:42:18'),
	('806106337',0,1,0,0,'2023-02-26 17:56:00','2023-02-26 17:56:00','DariaLagunova','2023-02-26 17:56:00','2023-02-26 17:56:00','2023-02-26 17:56:00'),
	('889316779',0,0,0,0,'2023-02-26 19:48:11','2023-03-05 15:48:21','LubitelGG','2023-02-26 16:24:09','2023-02-26 16:24:09','2023-02-27 17:22:59'),
	('947218494',0,0,0,0,'2023-02-27 00:46:12','2023-03-05 15:56:54','toxan4ik','2023-02-26 16:24:09','2023-02-26 16:24:09','2023-02-26 16:24:09');

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users_cards
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_cards`;

CREATE TABLE `users_cards` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_card` int unsigned NOT NULL,
  `id_user_id` varchar(20) NOT NULL,
  `date_get` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_card` (`id_card`),
  KEY `id_user_id` (`id_user_id`),
  CONSTRAINT `users_cards_ibfk_1` FOREIGN KEY (`id_card`) REFERENCES `cards` (`id`) ON DELETE CASCADE,
  CONSTRAINT `users_cards_ibfk_2` FOREIGN KEY (`id_user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `users_cards` WRITE;
/*!40000 ALTER TABLE `users_cards` DISABLE KEYS */;

INSERT INTO `users_cards` (`id`, `id_card`, `id_user_id`, `date_get`)
VALUES
	(59,116,'6189180632','2023-02-26 14:49:02'),
	(60,15,'6189180632','2023-02-26 14:58:27'),
	(61,122,'6189180632','2023-02-26 14:58:45'),
	(62,11,'6189180632','2023-02-26 14:58:46'),
	(63,65,'6189180632','2023-02-26 14:58:47'),
	(64,79,'6189180632','2023-02-26 14:58:48'),
	(65,58,'408853689','2023-02-26 15:45:55'),
	(66,29,'408853689','2023-02-26 15:45:58'),
	(67,121,'408853689','2023-02-26 15:46:15'),
	(68,10,'408853689','2023-02-26 15:46:17'),
	(69,123,'408853689','2023-02-26 15:46:18'),
	(70,2,'1265361945','2023-02-26 15:48:06'),
	(71,1,'889316779','2023-02-26 15:48:07'),
	(72,77,'889316779','2023-02-26 15:48:11'),
	(73,127,'1265361945','2023-02-26 15:48:15'),
	(74,121,'889316779','2023-02-26 15:48:26'),
	(75,87,'947218494','2023-02-26 15:56:41'),
	(76,23,'947218494','2023-02-26 15:56:45'),
	(77,50,'947218494','2023-02-26 15:56:56'),
	(78,104,'947218494','2023-02-26 15:56:57'),
	(79,97,'947218494','2023-02-26 15:56:59'),
	(80,31,'947218494','2023-02-26 15:57:01'),
	(81,19,'947218494','2023-02-26 15:57:02'),
	(82,59,'947218494','2023-02-26 15:57:07'),
	(83,43,'346831387','2023-02-26 16:05:05'),
	(84,46,'346831387','2023-02-26 16:05:30'),
	(85,17,'346831387','2023-02-26 16:06:02'),
	(86,53,'346831387','2023-02-26 16:06:06'),
	(87,25,'346831387','2023-02-26 16:08:01'),
	(88,2,'1265361945','2023-02-26 16:20:21'),
	(89,84,'1265361945','2023-02-26 16:20:23'),
	(90,42,'1265361945','2023-02-26 16:20:26'),
	(91,74,'6189180632','2023-02-26 16:58:19'),
	(92,45,'6189180632','2023-02-26 16:58:21'),
	(93,21,'6189180632','2023-02-26 16:58:22'),
	(94,40,'6189180632','2023-02-26 16:58:23'),
	(95,138,'6189180632','2023-02-26 16:58:24'),
	(96,121,'6189180632','2023-02-26 16:58:24'),
	(97,16,'408853689','2023-02-26 17:04:16'),
	(98,3,'408853689','2023-02-26 17:05:03'),
	(99,5,'408853689','2023-02-26 17:05:05'),
	(100,138,'408853689','2023-02-26 17:05:06'),
	(101,99,'408853689','2023-02-26 17:05:10'),
	(102,30,'408853689','2023-02-26 17:05:14'),
	(103,84,'408853689','2023-02-26 17:05:42'),
	(104,99,'6189180632','2023-02-26 17:58:01'),
	(105,30,'6189180632','2023-02-26 17:58:02'),
	(106,7,'6189180632','2023-02-26 17:58:03'),
	(107,28,'6189180632','2023-02-26 17:58:04'),
	(108,132,'6189180632','2023-02-26 17:58:05'),
	(109,63,'6189180632','2023-02-26 17:58:06'),
	(110,62,'6189180632','2023-02-26 17:58:07'),
	(111,118,'6189180632','2023-02-26 17:58:07'),
	(112,98,'6189180632','2023-02-26 17:58:09'),
	(113,93,'6189180632','2023-02-26 17:58:10'),
	(114,36,'6189180632','2023-02-26 17:58:11'),
	(115,107,'6189180632','2023-02-26 17:58:11'),
	(116,28,'6189180632','2023-02-26 17:58:12'),
	(117,46,'6189180632','2023-02-26 17:58:13'),
	(118,63,'6189180632','2023-02-26 17:58:14'),
	(119,44,'6189180632','2023-02-26 17:58:15'),
	(120,4,'6189180632','2023-02-26 17:58:15'),
	(121,28,'6189180632','2023-02-26 17:58:16'),
	(122,119,'6189180632','2023-02-26 17:58:17'),
	(123,125,'6189180632','2023-02-26 17:58:18'),
	(124,101,'6189180632','2023-02-26 17:58:18'),
	(125,32,'6189180632','2023-02-26 17:58:19'),
	(126,39,'6189180632','2023-02-26 17:58:20'),
	(127,33,'6189180632','2023-02-26 17:58:20'),
	(128,33,'6189180632','2023-02-26 17:58:21'),
	(129,6,'6189180632','2023-02-26 17:58:22'),
	(130,54,'6189180632','2023-02-26 17:58:22'),
	(131,45,'6189180632','2023-02-26 17:58:23'),
	(132,6,'6189180632','2023-02-26 17:58:23'),
	(133,31,'6189180632','2023-02-26 17:58:24'),
	(134,54,'6189180632','2023-02-26 17:58:25'),
	(135,138,'6189180632','2023-02-26 17:58:25'),
	(136,86,'6189180632','2023-02-26 17:58:26'),
	(137,12,'6189180632','2023-02-26 19:39:09'),
	(138,123,'6189180632','2023-02-26 19:42:13'),
	(139,112,'633118670','2023-02-26 19:42:49'),
	(140,92,'6189180632','2023-02-26 19:42:49'),
	(141,42,'6189180632','2023-02-26 20:07:45'),
	(142,21,'6189180632','2023-02-26 20:08:05'),
	(143,8,'6189180632','2023-02-26 20:08:14'),
	(144,3,'6189180632','2023-02-26 20:08:16'),
	(145,34,'6189180632','2023-02-26 20:08:17'),
	(146,120,'6189180632','2023-02-26 20:08:19'),
	(147,33,'6189180632','2023-02-26 20:08:24'),
	(148,85,'6189180632','2023-02-26 20:10:06'),
	(149,26,'6189180632','2023-02-26 20:10:10'),
	(150,27,'1265361945','2023-02-26 20:10:40'),
	(151,58,'6189180632','2023-02-26 20:11:45'),
	(152,57,'6189180632','2023-02-26 20:11:47'),
	(153,19,'6189180632','2023-02-26 20:11:49'),
	(154,129,'6189180632','2023-02-26 20:11:49'),
	(155,100,'6189180632','2023-02-26 20:11:50'),
	(156,109,'6189180632','2023-02-26 20:11:51'),
	(157,51,'6189180632','2023-02-26 20:11:52'),
	(158,81,'408853689','2023-02-26 20:19:38'),
	(159,43,'633118670','2023-02-26 20:26:57'),
	(160,10,'633118670','2023-02-26 20:27:09'),
	(161,41,'633118670','2023-02-26 20:27:39'),
	(162,45,'456406814','2023-02-26 20:35:49'),
	(163,32,'947218494','2023-02-26 20:46:12'),
	(164,82,'456406814','2023-02-26 21:00:20'),
	(165,117,'456406814','2023-02-26 21:00:36'),
	(166,17,'456406814','2023-02-26 21:00:40'),
	(167,33,'6189180632','2023-02-26 21:01:05'),
	(168,50,'6189180632','2023-02-26 21:01:09');

/*!40000 ALTER TABLE `users_cards` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
