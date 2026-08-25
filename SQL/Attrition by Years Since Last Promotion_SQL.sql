SELECT
    CASE
        WHEN YearsSinceLastPromotion BETWEEN 0 AND 2 THEN '0-2 Years'
        WHEN YearsSinceLastPromotion BETWEEN 3 AND 5 THEN '3-5 Years'
        WHEN YearsSinceLastPromotion BETWEEN 6 AND 10 THEN '6-10 Years'
        ELSE '10+ Years'
    END AS PromotionGroup,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionCount,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY
    CASE
        WHEN YearsSinceLastPromotion BETWEEN 0 AND 2 THEN '0-2 Years'
        WHEN YearsSinceLastPromotion BETWEEN 3 AND 5 THEN '3-5 Years'
        WHEN YearsSinceLastPromotion BETWEEN 6 AND 10 THEN '6-10 Years'
        ELSE '10+ Years'
    END
ORDER BY
    CASE
        WHEN PromotionGroup = '0-2 Years' THEN 1
        WHEN PromotionGroup = '3-5 Years' THEN 2
        WHEN PromotionGroup = '6-10 Years' THEN 3
        ELSE 4
    END;