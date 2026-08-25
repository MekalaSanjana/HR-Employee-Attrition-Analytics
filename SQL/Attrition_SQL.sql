SELECT COUNT(*) AS TotalEmployees
FROM employees;

SELECT Attrition, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Attrition;