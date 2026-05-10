/*
You are given two tables, teams
content_copy
 and matches
content_copy
, with the following structures:

  create table teams (
      team_id integer not null,
      team_name varchar(30) not null,
      unique(team_id)
  );

  create table matches (
      match_id integer not null,
      host_team integer not null,
      guest_team integer not null,
      host_goals integer not null,
      guest_goals integer not null,
      unique(match_id)
  );

content_copy
Each record in the table teams
content_copy
 represents a single soccer team. Each record in the table matches
content_copy
 represents a finished match between two teams. Teams (host_team
content_copy
, guest_team
content_copy
) are represented by their IDs in the teams
content_copy
 table (team_id
content_copy
). No team plays a match against itself. You know the result of each match (that is, the number of goals scored by each team).

You would like to compute the total number of points each team has scored after all the matches described in the table. The scoring rules are as follows:

If a team wins a match (scores strictly more goals than the other team), it receives three points.
If a team draws a match (scores exactly the same number of goals as the opponent), it receives one point.
If a team loses a match (scores fewer goals than the opponent), it receives no points.
Write an SQL query that returns a ranking of all teams (team_id
content_copy
) described in the table teams
content_copy
. For each team you should provide its name and the number of points it received after all described matches (num_points
content_copy
). The table should be ordered by num_points
content_copy
 (in decreasing order). In case of a tie, order the rows by team_id
content_copy
 (in increasing order).

For example, for:

  teams:

   team_id | team_name
  ---------+---------------
   10      | Give
   20      | Never
   30      | You
   40      | Up
   50      | Gonna


  matches:

   match_id | host_team | guest_team | host_goals | guest_goals
  ----------+-----------+------------+------------+-------------
   1        | 30        | 20         | 1          | 0
   2        | 10        | 20         | 1          | 2
   3        | 20        | 50         | 2          | 2
   4        | 10        | 30         | 1          | 0
   5        | 30        | 50         | 0          | 1

content_copy
your query should return:

   team_id | team_name | num_points
  ---------+-----------+------------
   20      | Never     | 4
   50      | Gonna     | 4
   10      | Give      | 3
   30      | You       | 3
   40      | Up        | 0
*/

/*
1. matches 테이블에서 host_team 컬럼 기준으로 host_goals sum 
2. matches 테이블에서 guest_team 컬럼 기준으로 guest_goals sum
3. 1,2번 테이블 union all
4. 3번 테이블과 teams 테이블을 join해서 team_id, team_name, num_points(sum) 추출  
*/

-- select a.team_id, b.team_name as team_name, sum(a.goals) as num_points 
-- from (
-- select host_team as team_id, sum(host_goals) as goals 
-- from matches 
-- group by host_team
-- union all 
-- select guest_team as team_id, sum(guest_goals) as goals 
-- from matches 
-- group by guest_team
-- ) as a 
-- join teams as b 
-- on a.team_id = b.team_id
-- group by a.team_id, b.team_name
-- order by num_points desc, team_id asc
-- ;

/*
1. case when을 통해 얻은 승점 및 팀을 의미하는 컬럼 추가 
2. teams와 host 기준 얻은 승점 추출, guest 기준 얻은 승점 추출 
3. 두개를 union all 하여 최종 승점 추출 
4. teams 테이블과 join하여 team_id, team_name, num_points 추출 
*/


with q as (select match_id
    , host_team
    , guest_team
    , host_goals
    , guest_goals
    , case when host_goals > guest_goals
        then 3
    when host_goals = guest_goals
        then 1 
    else 0 end as host_num_points 
    , case when host_goals > guest_goals
        then host_team
    when host_goals = guest_goals
        then host_team 
    else null end as host_team_id
    , case when host_goals < guest_goals
        then 3
    when host_goals = guest_goals
        then 1 
    else 0 end as guest_num_points 
    , case when host_goals < guest_goals
        then guest_team
    when host_goals = guest_goals
        then guest_team 
    else null end as guest_team_id
from matches)
, 
host_result as (
    select host_team_id as team_id, sum(host_num_points) as num_points  
    from q
    where host_team_id is not null 
    group by host_team_id
)
,
guest_result as (
    select guest_team_id as team_id, sum(guest_num_points) as num_points  
    from q
    where guest_team_id is not null 
    group by guest_team_id   
)

select  b.team_id
    , b.team_name
    , case when a.team_id is not null 
    then a.num_points 
    else 0 
    end as num_points
from (
    select c.team_id
        , sum(c.num_points) as num_points
        from (
            select * 
            from host_result
            union all 
            select * 
            from guest_result
            ) as c 
    group by c.team_id
) as a 
right join teams as b 
on a.team_id = b.team_id
order by num_points desc, b.team_id asc
;