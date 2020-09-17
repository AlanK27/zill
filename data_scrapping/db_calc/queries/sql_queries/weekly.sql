drop table if exists week1;
create table week1 (
	with weekly as (
		select * from main
		where 
			date > subdate(curdate(), interval 1 week)
	),
    amax as ( 
		select m1.date, m1.address, m1.location, max(m1.price) as price
		from weekly m1, weekly m2
		where
			m1.address = m2.address
		group by 
			m2.address, m1.price, m1.location
		having
			count(m2.address) > 1 and
			m1.price = max(m2.price)
	),
    amin as (
		select m1.date, m1.address, m1.location, min(m1.price) as price
		from weekly m1, weekly m2
		where
			m1.address = m2.address
		group by 
			m2.address, m1.price, m1.location
		having
			count(m2.address) > 1 and
			m1.price = min(m2.price)
	),
    week1 as (    
    select * from amax 
    union all
    select * from amin
    )
    select m1.date, m1.address, m1.location, m1.price
	from week1 m1, week1 m2
	where
    m1.address = m2.address and
	m1.location = m2.location and
    m1.price != m2.price
    );