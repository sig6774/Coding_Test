/*
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

The result format is in the following example.

 

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation: 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
*/

/*
1. 각 사용자의 event_date 첫번쨰 이후 2번째 값이 그 다음날인지 확인 후 다음 날이면 count 
2. 전체 player id 와 구한 count 나누기
*/
with q as (
select player_id
    , event_date
    , row_number() over (partition by player_id order by event_date asc) as rnk
from Activity
)
select round(sum(d.case_test) / count(d.case_test),2)as fraction
from (
select case when c.second_login_date = date_add(c.first_login_date, interval 1 day) 
        then 1
        else 0
        end as case_test
from (
select a.player_id, a.event_date as first_login_date, b.event_date as second_login_date
from (select player_id, event_date from q where rnk = 1) as a 
left join (select player_id, event_date from q where rnk = 2) as b 
on a.player_id = b.player_id
) as c
) as d 
;

-- 참고 풀이 
SELECT
    ROUND(
    COUNT(A1.player_id)
    / (SELECT COUNT(DISTINCT A3.player_id) FROM Activity A3), 2) AS fraction
FROM
    Activity A1
WHERE
    (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) IN (
    SELECT
        A2.player_id,
        MIN(A2.event_date)
    FROM
        Activity A2
    GROUP BY
        A2.player_id
);