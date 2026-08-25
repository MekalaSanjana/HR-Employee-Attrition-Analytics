SELECT
    Attrition,
    COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Attrition;