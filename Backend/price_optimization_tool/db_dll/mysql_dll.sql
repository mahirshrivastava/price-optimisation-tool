-- Creating Product Table
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(40) NOT NULL,
  `description` varchar(255) NOT NULL,
  `cost_price` float NOT NULL,
  `selling_price` float NOT NULL,
  `category` varchar(40) NOT NULL,
  `stock_available` int NOT NULL,
  `units_sold` int NOT NULL,
  `customer_rating` float NOT NULL,
  `demand_forecast` int DEFAULT NULL,
  `optimized_price` float DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_name` (`product_name`)
)

-- Create Users Table
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(120) NOT NULL,
  `role_id` int NOT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
)

-- Create Roles Table
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(30) NOT NULL,
  `demand_forecast` tinyint(1) DEFAULT NULL,
  `add_products` tinyint(1) DEFAULT NULL,
  `view_products` tinyint(1) DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `modified_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_name` (`role_name`)
)