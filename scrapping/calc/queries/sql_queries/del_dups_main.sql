drop table if exists del_dup;
create table del_dup(
	with main2 as (
	select * from main
	where main.date > subdate(curdate(), interval 2 day))
	select m1.*
	from 
		main2 m1, main2 m2
	where
		m1.address = m2.address and
		m1.location = m2.location and
		m1.price = m2.price
	group by
		m1.address, m1.price
);