
delete from yesterday;

INSERT INTO yesterday SELECT * FROM today;

delete from today;
