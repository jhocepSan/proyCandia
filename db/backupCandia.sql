-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:        9.3.0 - MySQL Community Server - GPL
-- SO del servidor:              Linux
-- HeidiSQL Versión:            12.10.1.133
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para candiacar
CREATE DATABASE IF NOT EXISTS `candiacar` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `candiacar`;

-- Volcando estructura para tabla candiacar.persona
DROP TABLE IF EXISTS `persona`;
CREATE TABLE IF NOT EXISTS `persona` (
  `idpersona` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `direccion` text,
  `telefono` varchar(10) DEFAULT NULL,
  `foto` text,
  `idusuario` int NOT NULL DEFAULT '-1',
  `estado` varchar(1) DEFAULT 'A' COMMENT 'A = ACTIVO\\nE = ELIMINADO\\nI = INACTIVO',
  `tipo` varchar(1) DEFAULT 'U',
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  `codigo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idpersona`),
  CONSTRAINT codigo UNIQUE (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla candiacar.segusuario
DROP TABLE IF EXISTS `segusuario`;
CREATE TABLE IF NOT EXISTS `segusuario` (
  `idusuario` int unsigned NOT NULL,
  `usoapp` varchar(1) DEFAULT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  `ubicacion` point DEFAULT NULL,
  `detalles` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla candiacar.servicio
DROP TABLE IF EXISTS `servicio`;
CREATE TABLE IF NOT EXISTS `servicio` (
  `idservicio` int unsigned NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  `tipo` varchar(1) DEFAULT NULL COMMENT 'P= MANTENIMIENTO PREVENTIVO\nC=MANTENIMIETNO CORRECTIVO\nI=INSPECCION VEHICULAR\n',
  `estado` varchar(1) DEFAULT NULL COMMENT 'A=activo\nF=teminado\nS=en espera\n',
  `descripcion` text,
  `hingreso` datetime DEFAULT NULL,
  `hsalida` datetime DEFAULT NULL,
  `idpersona` int NOT NULL,
  `idvehiculo`  int unsigned not null,
  PRIMARY KEY (`idservicio`),
  constraint servicio_persona_idpersona_fk
      foreign key (idpersona) references candiacar.persona (idpersona),
  constraint servicio_vehiculo_idvehiculo_fk
      foreign key (idvehiculo) references candiacar.vehiculo (idvehiculo)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla candiacar.tipovehiculo
DROP TABLE IF EXISTS `tipovehiculo`;
CREATE TABLE IF NOT EXISTS `tipovehiculo` (
  `idtipovehiculo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `estado` varchar(1) DEFAULT 'A',
  PRIMARY KEY (`idtipovehiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla candiacar.usuario
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `idusuario` int unsigned NOT NULL AUTO_INCREMENT,
  `nameusuario` varchar(15) DEFAULT NULL,
  `correo` varchar(45) NOT NULL,
  `estado` varchar(1) DEFAULT 'A',
  `tipo` varchar(1) DEFAULT NULL,
  `usoapp` varchar(1) DEFAULT NULL,
  `contrasenia` varchar(200) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla candiacar.vehiculo
DROP TABLE IF EXISTS `vehiculo`;
CREATE TABLE IF NOT EXISTS `vehiculo` (
  `idvehiculo` int unsigned NOT NULL AUTO_INCREMENT,
  `modelo` varchar(10) DEFAULT NULL,
  `placa` varchar(10) DEFAULT NULL,
  `color` varchar(10) DEFAULT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
  `idtipo` int DEFAULT NULL,
  `motor` varchar(45) DEFAULT NULL,
  `km` varchar(45) DEFAULT NULL,
  `fotoplaca` text,
  `foto` text,
  PRIMARY KEY (`idvehiculo`),
  CONSTRAINT placa UNIQUE (placa),
  CONSTRAINT vehiculo_tipovehiculo_idtipovehiculo_fk foreign key (idtipo) references candiacar.tipovehiculo (idtipovehiculo)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
