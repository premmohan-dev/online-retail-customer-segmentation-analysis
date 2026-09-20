/*===================================================
  Research Question 3
  How do customer spending and purchasing frequency
  vary across customers?
===================================================*/

SELECT
    [Customer ID],
    Round(Sum(Quantity * Price), 2) AS TotalSpend,
    Count(Invoice) AS PurchaseCount
FROM qry_CleanTransactions
GROUP BY [Customer ID]
ORDER BY Round(Sum(Quantity * Price), 2) DESC;
