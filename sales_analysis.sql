
USE sales;

SELECT
    COUNT(*) AS Total_Rows,
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(
        100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0),
        2
    ) AS Profit_Margin_Percent
FROM Superstore;

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY Region
ORDER BY Total_Profit DESC;


SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Sales_Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales,
    ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM Superstore
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY Sales_Month;


SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;


SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(
        100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0),
        2
    ) AS Profit_Margin_Percent
FROM Superstore
GROUP BY Region
ORDER BY Profit_Margin_Percent DESC;

