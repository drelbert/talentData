# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:13:34 2017

@author: DElbert
"""

from sqlalchemy import create_engine

dbconn = create_engine('mysql+mysqlconnector://root@localhost/talentdataone')



-- MySQL Workbench Forward Engineering code from 11.20.17


SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`person` ;

CREATE TABLE IF NOT EXISTS `mydb`.`person` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lastName` VARCHAR(32) NULL,
  `firstName` VARCHAR(32) NULL,
  `personType` VARCHAR(32) NULL,
  `personStatus` VARCHAR(20) NULL,
  `orgId` VARCHAR(20) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Evaluations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Evaluations` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Evaluations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `questionOne` INT NULL,
  `questionTwo` INT NULL,
  `questionThree` INT NULL,
  `questionFour` INT NULL,
  `courseId` VARCHAR(15) NULL,
  `transcriptId` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Mandatory Courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Mandatory Courses` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Mandatory Courses` (
  `id` INT NOT NULL,
  `courseName` VARCHAR(45) NULL,
  `closeDate` DATE NULL,
  `duration` INT NULL,
  `transcript_id` INT NOT NULL,
  `Evaluations_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`transcript`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`transcript` ;

CREATE TABLE IF NOT EXISTS `mydb`.`transcript` (
  `hhsId` FLOAT NULL,
  `courseTitle` VARCHAR(50) NULL,
  `dateMarkedComplete` DATE NULL,
  `courseId` VARCHAR(15) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Courses` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Courses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `courseTitle` VARCHAR(50) NULL,
  `courseId` VARCHAR(15) NULL,
  `offeringStartDate` DATE NULL,
  `offeringEndDate` DATE NULL,
  `offeringDomain` VARCHAR(20) NULL,
  `deliveryType` VARCHAR(30) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Program Course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Program Course` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Program Course` (
  `id` INT NOT NULL,
  `courseName` VARCHAR(45) NULL,
  `programId` DATE NULL,
  `duration` INT NULL,
  `transcript_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Program`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Program` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Program` (
  `id` INT NOT NULL,
  `supervisor` VARCHAR(20) NULL,
  `projectOfficer` VARCHAR(20) NULL,
  `grantsManager` VARCHAR(20) NULL,
  `midLevelLeader` VARCHAR(20) NULL,
  `seniorLevelLeader` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL DEFAULT 'initial, current, out of compliance',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`transcripts_has_Open Enrollment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`transcripts_has_Open Enrollment` ;

CREATE TABLE IF NOT EXISTS `mydb`.`transcripts_has_Open Enrollment` (
  `transcripts_id` INT NOT NULL,
  `Open Enrollment_id` INT NOT NULL,
  PRIMARY KEY (`transcripts_id`, `Open Enrollment_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Program Course_has_Program`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Program Course_has_Program` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Program Course_has_Program` (
  `Program Course_id` INT NOT NULL,
  `Program_id` INT NOT NULL,
  PRIMARY KEY (`Program Course_id`, `Program_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`organization`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`organization` ;

CREATE TABLE IF NOT EXISTS `mydb`.`organization` (
  `organization_id` INT NOT NULL,
  `org code` VARCHAR(45) NULL,
  PRIMARY KEY (`organization_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
