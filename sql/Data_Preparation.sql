/*===================================================
  Data Preparation
  Online Retail Customer Segmentation Analysis
===================================================*/

/*------------------------------*--------------------
  Combine Tra*saction Data
  Combines records from both years into a single query.
---------------------------------------------------*/

SELECT *
FROM [Year 2009-2010]

UNION ALL

SELECT *
FROM [Year 2010-2011];

/* Save As: qry_AllTransactions */


/*---------------------------------------------------
  Clean Transaction Data
  Removes:
  - Missing Customer IDs
  - Negative quantities (returns/cancellations)
  - Zero-price transactions
---------------------------------------------------*/

SELECT *
FROM qry_AllTransactions
WHERE [Customer ID] Is Not Null
    AND Quantity > 0
    AND Price > 0;

/* Save As: qry_CleanTransactions */
