CREATE TABLE IF NOT EXISTS main (
    dates date,
    addrs varchar(150),
    bedroom int,
    sqft int,
    bathroom int,
    parking int,
    price float(2),
    rental_in float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
);
CREATE TABLE IF NOT EXISTS month1 (
    date date,
    address varchar(255) ,
    location varchar(255) ,
    price int
);
CREATE TABLE IF NOT EXISTS month6 (
    date date,
    address varchar(255) ,
    location varchar(255) ,
    price int
);
CREATE TABLE IF NOT EXISTS today (
    dates date,
    addrs varchar(150),
    bedroom int,
    sqft int,
    bathroom int,
    parking int,
    price float(2),
    rental_in float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
);
CREATE TABLE IF NOT EXISTS week1 (
    date date,
    address varchar(255) ,
    location varchar(255) ,
    price int
);
CREATE TABLE IF NOT EXISTS yesterday (
    dates date,
    addrs varchar(150),
    bedroom int,
    sqft int,
    bathroom int,
    parking int,
    price float(2),
    rental_in float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
);