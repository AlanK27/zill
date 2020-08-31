
CREATE TABLE IF NOT EXISTS zill (
    dates date,
    addrs varchar(150),
    bedroom int,
    sqft int,
    bathroom int,
    parking int,
    price float(2),
    rental_in float(2),
    rent float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
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
    rent float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
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
    rent float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
);

CREATE TABLE IF NOT EXISTS main (
    dates date,
    addrs varchar(150),
    bedroom int,
    sqft int,
    bathroom int,
    parking int,
    price float(2),
    rental_in float(2),
    rent float(2),
    year int,
    price_sq float(2),
    neighbor varchar(5)
);

-- create table karz (
--     id BIGSERIAL NOT NULL PRIMARY KEY,
--     make VARCHAR(100) NOT NULL,
--     model VARCHAR(100) NOT NULL, 
--     price NUMERIC(19,2) NOT NULL
-- );

-- insert into karz (id, make, model, price) values (1, 'Ford', 'E80', '1598.43');
-- insert into karz (id, make, model, price) values (2, 'Subaru', 'XT', '1922.49');
-- insert into karz (id, make, model, price) values (3, 'Kia', 'Spectra', '2386.15');
-- insert into karz (id, make, model, price) values (4, 'Chrysler', '300M', '2001.74');
-- insert into karz (id, make, model, price) values (5, 'Mitsubishi', 'Diamante', '9157.33');



-- create table karz1 (
--     id BIGSERIAL NOT NULL PRIMARY KEY,
--     make VARCHAR(100) NOT NULL,
--     model VARCHAR(100) NOT NULL, 
--     price NUMERIC(19,2) NOT NULL
-- );

-- insert into karz1 (id, make, model, price) values (1, 'Xord1111', 'E250', '1598.43');
-- insert into karz1 (id, make, model, price) values (2, 'Chrysler111', '300M', '2001.74');
-- insert into karz1 (id, make, model, price) values (3, 'Kia1111', 'Spectra', '2386.15');
-- insert into karz1 (id, make, model, price) values (4, 'Subaru1111', 'XT', '1922.49');












-- insert into today (id, date, addrs, bedroom, parking, price, rental_in, rent, year_built, price_sq, neighbor) values (1, 3-3-18 'Kia1111', 'Spectra', '2386.15');
-- insert into today (id, date, addrs, bedroom, parking, price, rental_in, rent, year_built, price_sq, neighbor) values (2, 'Subaru1111', 'XT', '1922.49');

-- insert into yesterday (id, date, addrs, bedroom, parking, price, rental_in, rent, year_built, price_sq, neighbor) values (3, 'Kia1111', 'Spectra', '2386.15');
-- insert into yesterday (id, date, addrs, bedroom, parking, price, rental_in, rent, year_built, price_sq, neighbor) values (4, 'Subaru1111', 'XT', '1922.49');