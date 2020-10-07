CREATE SCHEMA `jw` ;
use jw;
CREATE TABLE `jw`.`empleado` (
  `codempleado` VARCHAR(15) NOT NULL,
  `nombres_empleado` VARCHAR(35) NULL,
  `apellidos_empleado` VARCHAR(35) NULL,
  `telefono_empleado` VARCHAR(15) NULL,
  `edad_empleado` VARCHAR(3) NULL,
  `salario_empleado` VARCHAR(10) NULL,
  `genero` VARCHAR(12) NULL,
  `cargo` VARCHAR(20) NULL,
  `civil` VARCHAR(15) NULL,
  `estado` VARCHAR(15) NULL,
  PRIMARY KEY (`codempleado`));
