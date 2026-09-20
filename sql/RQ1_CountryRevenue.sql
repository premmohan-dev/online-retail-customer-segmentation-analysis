/*===================================================
  Research Question 1
  Which countries generate the most sales revenue?
===================================================*/

SELECT
    Country,
    Round(Sum(Quantity * Price), 2) AS TotalRevenue
FROM qry_CleanTransactions
GROUP BY Country
ORDER BY Round(Sum(Quantity * Price), 2) DESC;
