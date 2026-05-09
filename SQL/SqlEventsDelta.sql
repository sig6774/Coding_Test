/*
Given a table events
content_copy
 with the following structure:

  create table events (
      event_type integer not null,
      value integer not null,
      time timestamp not null,
      unique(event_type, time)
  );

content_copy
write an SQL query that, for each event_type
content_copy
 that has been registered more than once, returns the difference between the latest (i.e. the most recent in terms of time
content_copy
) and the second latest value
content_copy
. The table should be ordered by event_type
content_copy
 (in ascending order).

For example, given the following data:

   event_type | value      | time
  ------------+------------+--------------------
   2          | 5          | 2015-05-09 12:42:00
   4          | -42        | 2015-05-09 13:19:57
   2          | 2          | 2015-05-09 14:48:30
   2          | 7          | 2015-05-09 12:54:39
   3          | 16         | 2015-05-09 13:19:57
   3          | 20         | 2015-05-09 15:01:09

content_copy
your query should return the following rowset:

   event_type | value
  ------------+-----------
   2          | -5
   3          | 4

content_copy
For the event_type
content_copy
 2, the latest value
content_copy
 is 2 and the second latest value
content_copy
 is 7, so the difference between them is −5.

The names of the columns in the rowset don't matter, but their order does.
*/

-- Implement your solution here
-- event_type를 통해 정렬을 하는데 기준은 time 

with rnk_tbl as (
    select event_type, value, rank() over(partition by event_type order by time desc) as rnk 
    from events
)
select a.event_type, sum(a.value - b.value) AS value 
from rnk_tbl as a 
join rnk_tbl as b 
on a.event_type = b.event_type
where a.rnk = 1 and b.rnk = 2
group by a.event_type
order by a.event_type asc;