--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
select e1.Name as 'Employee' from Employee e1, Employee e2 where e1.Salary > e2.Salary and e1.ManagerId = e2.Id
-- @lc code=end

