# Online Retail Customer Segmentation Analysis

## Overview

This analysis explores sales performance, customer purchasing behavior, and customer segmentation using transaction data from an online retail business. The project combines SQL analysis, data visualization, and clustering techniques to identify revenue insights, purchasing patterns, and distinct customer groups.

## Objectives

- Analyze sales revenue across countries and products.
- Identify purchasing patterns among retail customers.
- Examine differences in customer spending and order frequency.
- Explore customer behavior using transaction-level sales data.
- Segment customers into distinct groups based on purchasing behavior.
- Demonstrate how customer segmentation can provide insights into customer value and engagement.

## Dataset

This analysis uses the Online Retail II dataset from the UCI Machine Learning Repository. The dataset was created by Daqing Chen and was donated to the UCI Machine Learning Repository on September 20, 2019.

The data contains transactional data from a UK-based, registered, non-store online retail business between December 1, 2009 and December 9, 2011. The company primarily sells unique all-occasion giftware products, and many of its customers are wholesalers.

The dataset includes over 1 million transaction records and contains detailed information about customer purchases, products, quantities sold, pricing, transaction dates, and customer locations. It is commonly used for business analytics, customer behavior analysis, sales analysis, and customer segmentation.

### Key Variables

- Invoice Number (InvoiceNo)
- Product Code (StockCode)
- Product Description
- Quantity Purchased
- Invoice Date
- Unit Price
- Customer ID
- Country

### Additional Variables

- Revenue
- Total Customer Spend
- Order Count
- Average Order Value
- Customer Segment

The dataset contains some missing values related to customer identification informaiton. This will be addressed during the data preparation process.

## Research Questions

### 1) Which countries generate the most sales revenue?

<img width="989" height="590" alt="RQ1_CountryRevenue" src="https://github.com/user-attachments/assets/5cb30058-78e7-409f-9556-6a18fe058a97" />

### Key Findings

The United Kingdom generated the most sales revenue by a wide margin, bringing in approximately £14.7 million. The next highest-revenue countries were EIRE (£621,631) and the Netherlands (£554,232), but their sales were much lower than those of the United Kingdom. Overall, most sales came from customers located in the United Kingdom.

### 2) Which products generate the highest sales revenue?

<img width="989" height="590" alt="RQ2_ProductRevenue" src="https://github.com/user-attachments/assets/8c076f0c-ecea-4466-a2ae-34427b05d883" />

### Key Findings

The REGENCY CAKESTAND 3 TIER generated the highest sales revenue at £286,486.30, followed by the WHITE HANGING HEART T-LIGHT HOLDER at £252,072.46. Several of the highest-revenue products were decorative giftware and home décor items, suggesting these products were among the retailer's most successful offerings.

### 3) How do customer purchasing patterns vary by spending and order frequency?

### Key Findings

Customer spending and purchasing activity varied widely across the customer base. While many customers made relatively few purchases, a small group of customers generated substantially higher spending and purchase counts. These differences suggest that customers can be grouped into distinct segments based on their purchasing behavior.

### 4) Can customers be grouped into distinct segments based on purchasing behavior?

### Key Findings

## Methods

- Data cleaning and preparation in Microsoft Excel
- SQL analysis in Microsoft Access
- Exploratory data analysis in Python
- Data visualization using Python libraries
- Customer segmentation using K-Means clustering
- Interpretation of customer behavior and segmentation results

## Tools and Technologies

- Microsoft Excel
- Microsoft Access
- SQL
- Python
- Pandas
- Matplotlib
- Scikit-learn

## SQL Analysis

## Conclusion

## How to Use This Project
