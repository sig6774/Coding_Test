/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/

/*
1. 3번 붙여서 있는 애들을 조회해야 하나?
*/

SELECT distinct(a.num) as ConsecutiveNums 
FROM Logs as a 
left join Logs as b 
on a.id = b.id+1
left join Logs as c 
on b.id = c.id+1 
where a.num = b.num and b.num = a.num and c.num = a.num 
;