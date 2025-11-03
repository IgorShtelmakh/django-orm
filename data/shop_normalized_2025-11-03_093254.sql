-- MySQL dump 10.13  Distrib 8.0.41, for macos15.2 (arm64)
--
-- Host: 127.0.0.1    Database: shop_normalized
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `parent_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_categories_name` (`name`),
  KEY `fk_categories_parent` (`parent_id`),
  CONSTRAINT `fk_categories_parent` FOREIGN KEY (`parent_id`) REFERENCES `categories` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Ноутбуки',NULL),(2,'Смартфони',NULL),(3,'Телевізори',NULL),(4,'Побутова техніка',NULL),(5,'Аудіотехніка',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;

--
-- Table structure for table `customer_addresses`
--

DROP TABLE IF EXISTS `customer_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_addresses` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` int unsigned NOT NULL,
  `label` varchar(30) NOT NULL,
  `address_line` varchar(200) NOT NULL,
  `city` varchar(100) NOT NULL,
  `postal_code` varchar(20) DEFAULT NULL,
  `country` varchar(80) NOT NULL DEFAULT 'Україна',
  PRIMARY KEY (`id`),
  KEY `idx_caddr_customer` (`customer_id`),
  CONSTRAINT `fk_caddr_customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_addresses`
--

/*!40000 ALTER TABLE `customer_addresses` DISABLE KEYS */;
INSERT INTO `customer_addresses` VALUES (1,1,'shipping','вул. Хрещатик, 10','Київ','01001','Україна'),(2,2,'shipping','пл. Ринок, 5','Львів','79000','Україна'),(3,3,'shipping','вул. Дерибасівська, 3','Одеса','65000','Україна'),(4,4,'shipping','пр. Науки, 45','Харків','61000','Україна'),(5,5,'shipping','пр. Д. Яворницького, 50','Дніпро','49000','Україна'),(6,6,'shipping','вул. Соборна, 18','Вінниця','21000','Україна'),(7,7,'shipping','вул. Шевченка, 55','Полтава','36000','Україна'),(8,8,'shipping','вул. Головна, 22','Чернівці','58000','Україна'),(9,9,'shipping','пр. Соборний, 99','Запоріжжя','69000','Україна'),(10,10,'shipping','пр. Бандери, 14','Тернопіль','46000','Україна');
/*!40000 ALTER TABLE `customer_addresses` ENABLE KEYS */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_customers_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Іван Петренко','ivan.petrenko@example.com','+380501234567'),(2,'Оксана Коваленко','oksana.kovalenko@example.com','+380631112233'),(3,'Петро Іванов','petro.ivanov@example.com','+380971234567'),(4,'Марія Шевченко','maria.shevchenko@example.com','+380931112233'),(5,'Андрій Кравчук','andriy.kravchuk@example.com','+380671234567'),(6,'Наталія Ткаченко','nataliya.tkachenko@example.com','+380681112233'),(7,'Сергій Бондар','sergiy.bondar@example.com','+380931234567'),(8,'Юлія Лисенко','yuliya.lysenko@example.com','+380501112233'),(9,'Михайло Гордієнко','mykhailo.hordiienko@example.com','+380931567890'),(10,'Катерина Дорошенко','kateryna.doroshenko@example.com','+380671112233');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  `supplier_id` int unsigned DEFAULT NULL,
  `unit_price` decimal(12,2) NOT NULL,
  `quantity` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_oitems_product` (`product_id`),
  KEY `fk_oitems_supplier` (`supplier_id`),
  KEY `idx_oitems_order` (`order_id`),
  CONSTRAINT `fk_oitems_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_oitems_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_oitems_supplier` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
INSERT INTO `order_items` VALUES (1,1,4,1,44500.00,1),(2,2,6,5,37900.00,1),(3,3,11,3,41500.00,1),(4,4,1,1,24900.00,1),(5,5,7,2,35500.00,1),(6,6,14,4,26800.00,1),(7,7,17,5,15900.00,1),(8,8,18,1,11800.00,2),(9,9,12,2,51800.00,1),(11,11,3,3,34500.00,1),(12,12,16,3,8800.00,1),(13,13,2,2,27800.00,1),(14,14,13,4,40500.00,1),(15,15,15,2,22800.00,1),(16,16,19,3,6900.00,1),(17,17,9,5,27500.00,1),(18,18,5,2,31800.00,1);
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `order_number` varchar(40) NOT NULL,
  `customer_id` int unsigned NOT NULL,
  `order_date` date NOT NULL,
  `status` enum('pending','paid','shipped','cancelled') NOT NULL DEFAULT 'pending',
  `billing_address_id` int unsigned DEFAULT NULL,
  `shipping_address_id` int unsigned DEFAULT NULL,
  `notes` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_orders_number` (`order_number`),
  KEY `idx_orders_customer` (`customer_id`),
  KEY `fk_orders_baddr` (`billing_address_id`),
  KEY `fk_orders_saddr` (`shipping_address_id`),
  CONSTRAINT `fk_orders_baddr` FOREIGN KEY (`billing_address_id`) REFERENCES `customer_addresses` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_saddr` FOREIGN KEY (`shipping_address_id`) REFERENCES `customer_addresses` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'3001',1,'2025-08-01','paid',1,1,'Швидка доставка'),(2,'3002',2,'2025-08-02','paid',2,2,NULL),(3,'3003',3,'2025-08-02','pending',3,3,'Очікує підтвердження'),(4,'3004',4,'2025-08-03','paid',4,4,NULL),(5,'3005',5,'2025-08-04','paid',5,5,NULL),(6,'3006',6,'2025-08-05','pending',6,6,NULL),(7,'3007',7,'2025-08-06','paid',7,7,NULL),(8,'3008',8,'2025-08-07','paid',8,8,'Оплата частинами'),(9,'3009',9,'2025-08-08','pending',9,9,NULL),(11,'3011',1,'2025-08-10','paid',1,1,NULL),(12,'3012',2,'2025-08-11','pending',2,2,NULL),(13,'3013',3,'2025-08-12','paid',3,3,NULL),(14,'3014',4,'2025-08-13','paid',4,4,NULL),(15,'3015',5,'2025-08-14','pending',5,5,NULL),(16,'3016',6,'2025-08-15','paid',6,6,NULL),(17,'3017',7,'2025-08-16','paid',7,7,NULL),(18,'3018',8,'2025-08-17','pending',8,8,NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int unsigned NOT NULL,
  `method` enum('card','bank','cash','paypal') NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `paid_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_payments_order` (`order_id`),
  CONSTRAINT `fk_payments_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,1,'card',44500.00,'2025-08-03 10:15:00'),(2,2,'card',37900.00,'2025-08-03 12:00:00'),(3,4,'paypal',24900.00,'2025-08-04 09:10:00'),(4,5,'card',35500.00,'2025-08-05 15:20:00'),(5,7,'card',15900.00,'2025-08-07 11:45:00'),(6,8,'card',23600.00,'2025-08-08 14:00:00'),(8,11,'card',34500.00,'2025-08-11 10:05:00'),(9,13,'card',27800.00,'2025-08-12 12:40:00'),(10,14,'bank',40500.00,'2025-08-13 13:15:00'),(11,16,'card',6900.00,'2025-08-15 09:35:00'),(12,17,'card',27500.00,'2025-08-16 17:05:00');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku` varchar(64) NOT NULL,
  `name` varchar(160) NOT NULL,
  `category_id` int unsigned NOT NULL,
  `default_supplier_id` int unsigned DEFAULT NULL,
  `list_price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_products_sku` (`sku`),
  KEY `fk_products_category` (`category_id`),
  KEY `fk_products_supplier` (`default_supplier_id`),
  CONSTRAINT `fk_products_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_products_supplier` FOREIGN KEY (`default_supplier_id`) REFERENCES `suppliers` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'SKU001','Lenovo IdeaPad 3',1,1,25000.00),(2,'SKU002','HP Pavilion 15',1,2,28000.00),(3,'SKU003','Asus ZenBook 14',1,3,35000.00),(4,'SKU004','Apple MacBook Air',1,1,45000.00),(5,'SKU005','Dell Inspiron 16',1,2,32000.00),(6,'SKU006','iPhone 14',2,5,38000.00),(7,'SKU007','Samsung Galaxy S23',2,2,36000.00),(8,'SKU008','Xiaomi Redmi Note 12',2,3,15000.00),(9,'SKU009','OnePlus 11',2,5,28000.00),(10,'SKU010','Google Pixel 7',2,1,30000.00),(11,'SKU011','LG OLED 55',3,3,42000.00),(12,'SKU012','Samsung QLED 65',3,2,52000.00),(13,'SKU013','Sony Bravia 50',3,4,41000.00),(14,'SKU014','Bosch Холодильник',4,4,27000.00),(15,'SKU015','Samsung Пральна машина',4,2,23000.00),(16,'SKU016','Philips Пилосос',4,3,9000.00),(17,'SKU017','Sony WH-1000XM5',5,5,16000.00),(18,'SKU018','Apple AirPods Pro',5,1,12000.00),(19,'SKU019','JBL Charge 5',5,3,7000.00),(20,'12345678902','Product 3',5,5,21000.00),(21,'1234567890','Product 1',1,1,100000.00),(29,'12345678901','Product 1',1,1,100000.00);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;

--
-- Table structure for table `products_copy`
--

DROP TABLE IF EXISTS `products_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_copy` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku` varchar(64) NOT NULL,
  `name` varchar(160) NOT NULL,
  `category_id` int unsigned NOT NULL,
  `default_supplier_id` int unsigned DEFAULT NULL,
  `list_price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_products_sku` (`sku`),
  KEY `fk_products_category` (`category_id`),
  KEY `fk_products_supplier` (`default_supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_copy`
--

/*!40000 ALTER TABLE `products_copy` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_copy` ENABLE KEYS */;

--
-- Table structure for table `shipments`
--

DROP TABLE IF EXISTS `shipments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipments` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int unsigned NOT NULL,
  `carrier_name` varchar(80) DEFAULT NULL,
  `tracking_number` varchar(80) DEFAULT NULL,
  `shipped_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_shipments_tracking` (`tracking_number`),
  KEY `idx_shipments_order` (`order_id`),
  CONSTRAINT `fk_shipments_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipments`
--

/*!40000 ALTER TABLE `shipments` DISABLE KEYS */;
INSERT INTO `shipments` VALUES (1,1,'Нова Пошта','TRK30001','2025-08-03 18:00:00'),(2,2,'Укрпошта','TRK30002','2025-08-04 10:00:00'),(3,4,'Нова Пошта','TRK30004','2025-08-05 09:30:00'),(4,5,'Нова Пошта','TRK30005','2025-08-06 16:45:00'),(5,7,'Нова Пошта','TRK30007','2025-08-08 12:10:00'),(6,8,'Укрпошта','TRK30008','2025-08-09 08:20:00'),(8,11,'Нова Пошта','TRK3011','2025-08-12 15:10:00'),(9,13,'Нова Пошта','TRK3013','2025-08-13 16:00:00'),(10,14,'Укрпошта','TRK3014','2025-08-14 09:00:00'),(11,16,'Нова Пошта','TRK3016','2025-08-16 10:40:00'),(12,17,'Нова Пошта','TRK3017','2025-08-17 12:55:00');
/*!40000 ALTER TABLE `shipments` ENABLE KEYS */;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `phone` varchar(32) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_suppliers_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Rozetka',NULL,NULL),(2,'Comfy',NULL,NULL),(3,'Foxtrot',NULL,NULL),(4,'Epicentr',NULL,NULL),(5,'Allo',NULL,NULL);
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;

--
-- Dumping routines for database 'shop_normalized'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-03  9:33:07
