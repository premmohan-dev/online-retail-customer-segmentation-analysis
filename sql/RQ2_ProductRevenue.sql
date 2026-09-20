/*===================================================
  Research Question 2
  Which products generate the highest sales revenue?
===================================================*/

SELECT
    Description,
    Round(Sum(Quantity * Price), 2) AS TotalRevenue
FROM qry_CleanTransactions
WHERE Description <> 'Manual'
GROUP BY Description
ORDER BY Round(Sum(Quantity * Price), 2) DESC;
