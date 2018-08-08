use hwdb;

 
select Name from Data a 
    where Chinese_Score>=(
		select avg(Chinese_Score) as avgch 
		from Data b 
		where a.class=b.class 
		group by class); 