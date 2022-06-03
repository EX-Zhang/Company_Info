/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80028
Source Host           : localhost:3306
Source Database       : company

Target Server Type    : MYSQL
Target Server Version : 80028
File Encoding         : 65001

Date: 2022-06-01 10:39:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for company_stock
-- ----------------------------
DROP TABLE IF EXISTS `company_stock`;
CREATE TABLE `company_stock` (
  `Symbol` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Date` date NOT NULL,
  `Open` double DEFAULT NULL,
  `Close` double DEFAULT NULL,
  `High` double DEFAULT NULL,
  `Low` double DEFAULT NULL,
  PRIMARY KEY (`Symbol`,`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
