/*
SQL Schema
Pandas Schema
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
*/

/*
1. managerId가 null이 아닌 데이터 추출  
2. id와 managerId를 join하여 manager salary보다 큰 사원 salary 추출 
*/

with emp_tbl as (
    select id, name, salary, managerId
        from Employee 
    where managerId is not null 
),
total_tbl as (
    select id, name, salary, managerId
        from Employee 
)
select a.name as Employee 
from emp_tbl as a 
join total_tbl as b 
on a.managerId = b.id 
where a.salary > b.salary
;