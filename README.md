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

<img width="989" height="590" alt="RQ3_CustomerBehavior" src="https://github.com/user-attachments/assets/64e573f5-60f8-458d-806c-b29f3f60e39d" />

### Key Findings

Customer spending and purchasing activity varied widely across the customer base. While many customers made relatively few purchases, a small group of customers generated substantially higher spending and purchase counts. These differences suggest that customers can be grouped into distinct segments based on their purchasing behavior.

### 4) Can customers be grouped into distinct segments based on purchasing behavior?

<img width="989" height="590" alt="RQ4_CustomerSegmentation" src="https://github.com/user-attachments/assets/ee7e6479-efa2-4974-8a82-c4e3b561d04e" />

### Key Findings

K-Means clustering identified four distinct customer segments based on spending and purchasing activity. Most customers belonged to lower-spending and lower-activity segments, while smaller groups demonstrated substantially higher spending and purchase frequency. These results suggest that customers exhibit different purchasing behaviors and may benefit from targeted marketing and customer engagement strategies.

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

The SQL queries included in this analysis were developed and tested in Microsoft Access. Two years of transaction data were combined into a single dataset and cleaned by removing records with missing customer IDs, negative quantities, and zero-price transactions. SQL was used to calculate sales revenue by country and product, summarize customer purchasing behavior, and prepare the customer-level dataset used for customer segmentation. SQL served as the primary tool for data preparation and aggregation before visualization and clustering analysis.

## Python Analysis

Python was used to create visualizations and perform customer segmentation using K-Means clustering.

### RQ1 Visualization

A horizontal bar chart was created to compare sales revenue across countries. The visualization highlighted the United Kingdom as the company's primary source of revenue.

### RQ2 Visualization

A horizontal bar chart was developed to display the products generating the highest sales revenue. The chart helped identify the retailer's most successful products and product categories.

### RQ3 Visualization

A scatter plot was created to examine the relationship between customer spending and purchasing activity. The visualization showed that while most customers spent relatively little and made fewer purchases, a smaller group of customers generated substantially higher spending and purchase counts.

### RQ4 Customer Segmentation

K-Means clustering was applied using customer spending and purchase activity data. Customer segmentation identified four customer groups based on spending and purchase activity. Most customers spent less and made fewer purchases, while a smaller group of customers spent more and purchased more often. This shows that customers have different purchasing behaviors and can be grouped into distinct segments.

## Conclusion

This analysis examined over 1 million online retail transactions to explore sales performance, customer purchasing behavior, and customer segmentation.

The key findings were:

1. The United Kingdom generated the highest sales revenue by a substantial margin, accounting for the majority of revenue in the dataset.
2. Decorative giftware and home decor products were among the highest-revenue items sold by the retailer.
3. Customer spending and purchasing activity varied considerably across the customer base, with a small number of customers generating significantly higher spending and purchase activity.
4. Customer segmentation identified four distinct customer groups based on spending and purchasing behavior.

Overall, the results demonstrate how transaction data can be used to better understand sales performance, customer behavior, and customer segments. These insights can support business decisions related to product strategy, customer engagement, and targeted marketing efforts.

## How to Use This Project

1. Download the Online Retail II dataset from the UCI Machine Learning Repository (link provided in `data` folder).
2. Import both dataset worksheets into Microsoft Access.
3. Run the queries in `Data_Preparation.sql` to combine and clean the transaction data.
4. Execute the SQL queries in the `sql` folder to answer Research Questions 1 through 3.
5. Export the query results to Microsoft Excel.

### Alternative Option:
The query results used in the Python analysis are already included in the `data` folder as Excel files. These files can be used directly to reproduce the visualizations and customer segmentation analysis without re-running the Microsoft Access queries.

6. Use the Python scripts in the `python` folder to generate visualizations and perform customer segmentation analysis.
7. Review the charts and findings to understand sales performance, customer purchasing behavior, and customer segments within the online retail dataset.
