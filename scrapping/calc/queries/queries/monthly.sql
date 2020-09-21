-- Table is created displaying the max and min based on the previous month
-- duplicates needs to be cleared
drop table if exists month{};
create table month{0} (
	with monthly as (
		select * from main
		where 
			date > subdate(curdate(), interval {0} month)
	),
    amax as ( 
		select m1.date, m1.address, m1.location, max(m1.price) as price
		from monthly m1, monthly m2
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
		from monthly m1, monthly m2
		where
			m1.address = m2.address
		group by 
			m2.address, m1.price, m1.location
		having
			count(m2.address) > 1 and
			m1.price = min(m2.price)
	),
    month1 as (    
    select * from amax 
    union all
    select * from amin
    )
-- remove duplicates
    select m1.date, m1.address, m1.location, m1.price
	from month1 m1, month1 m2
	where
    m1.address = m2.address and
	m1.location = m2.location and
    m1.price != m2.price
);
-- insert most recent price of addresses listed above
-- insert into month1 (
-- 	with monthlly as (
-- 			select date, address, price
-- 			from main
-- 			where date > subdate(curdate(), interval 1 month)
-- 		)

-- 		select m1.date, m1.address, m1.price
-- 		from monthlly m1, monthlly m2
-- 		where 
-- 			m1.address = m2.address and
-- 			m1.date = m2.date and
-- 			m1.price = m2.price
-- 		group by 
-- 			m1.address
-- 		having 
-- 			m1.date = max(m2.date) and
-- 			(m1.date, m1.address) in (
-- 				select date, address 
-- 				from month1
-- 				group by address
-- 			)
-- )