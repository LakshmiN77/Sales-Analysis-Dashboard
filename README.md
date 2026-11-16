Sales Analysis Dashboard

## Project Overview

The Sales Analysis Dashboard is a data analytics project that transforms sales data into meaningful business insights. It uses Python for data cleaning, MySQL for SQL-based analysis, and Power BI for interactive visualization.

The project helps analyze sales performance, profitability, order volume, product categories, regional performance, and monthly sales trends.

## Objectives

- Clean and prepare sales data for analysis.
- Analyze revenue and profitability using SQL queries.
- Identify high-performing product categories and regions.
- Examine monthly sales trends and top-selling products.
- Build an interactive dashboard to explore business performance.

## Technologies Used
 Python: Pandas, Matplotlib
 Database:  MySQL
 SQL: Aggregations, GROUP BY, ORDER BY, DISTINCT, date functions, and LIMIT
 Business Intelligence: Power BI
 Data Modeling and Calculations: DAX
 Version Control: Git and GitHub

## Project Workflow

1. **Data Preparation**:** Clean the original Superstore dataset using Python, handle duplicate records and relevant missing values, convert date and numeric fields, and export the cleaned dataset.
2. **SQL Analysis:** Import the cleaned CSV into MySQL and execute queries to calculate sales, profit, order counts, category performance, regional profitability, monthly trends, and top products.
3. **Dashboard Development:** Build KPI cards, charts, and interactive slicers in Power BI using the cleaned dataset and DAX measures.
4. **Business Analysis:** Compare performance across categories and regions and examine sales and profitability trends.

## Key Features

- Total Sales, Total Profit, Total Orders, and Profit Margin KPI cards.
- Monthly sales trend visualization.
- Sales comparison across product categories.
- Regional profit comparison.
- Interactive filters for Region, Category, and Order Date.
- SQL queries for product, category, and regional analysis.

## SQL Business Questions

- What are the overall sales, profit, order count, and profit margin?
- Which product categories generate the highest sales?
- Which regions contribute the most profit?
- How do sales and profit change monthly?
- Which products generate the highest sales?
- Which sub-categories have the strongest and weakest profitability?
- How does profit margin vary across regions?

## Project Structure
 
SalesPerform/
├── data/
│   └── Sample - Superstore.csv
├── output/
│   └── superstore_clean.csv
├── sales_dash.pbix
├── sales_analysis.sql
├── salesAnalisys.py
└── README.md

## How to Run
1. Install Python and the required packages, including Pandas and Matplotlib.
2. Run the Python analysis script to prepare the cleaned dataset.
3. Create a MySQL database named `retail_sales` and import the cleaned CSV into a table named `Superstore`.
4. Open `retail_sales_analysis.sql` in MySQL Workbench and execute the queries.
5. Open `Retail_Sales_Dashboard.pbix` in Power BI Desktop to explore the dashboard.

## Learning Outcomes

- Data cleaning and preparation using Python.
- Writing SQL queries for business analysis.
- Creating DAX measures and interactive Power BI visuals.
- Translating raw sales data into business-focused insights.
- Organizing and documenting an end-to-end analytics project.

## Data Source

The project uses the Sample Superstore retail dataset. Include the dataset source and applicable attribution or license information when redistributing the data.

