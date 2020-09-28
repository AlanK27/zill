CREATE DATABASE IF NOT EXISTS rfin_db;
CREATE TABLE IF NOT EXISTS rfin_db.main (
    date date ,
    address varchar(255),
    location varchar(255), 
    price int,
    beds decimal(10,2), 
    baths decimal(10,2), 
    sqft decimal(10,2), 
    per_sqft decimal(10,2)
);
CREATE TABLE IF NOT EXISTS rfin_db.today like rfin_db.main;
CREATE TABLE IF NOT EXISTS rfin_db.yesterday like rfin_db.main;
CREATE TABLE IF NOT EXISTS rfin_db.month1 (
    date date,
    address varchar(255),
    location varchar(255),
    price bigint
);
CREATE TABLE IF NOT EXISTS rfin_db.month6 like rfin_db.month1;
CREATE TABLE IF NOT EXISTS rfin_db.week1 like rfin_db.month1;