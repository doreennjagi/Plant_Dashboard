# 🌱 Plants Revenue & Growth Optimization Dashboard

## Dataset
The project leverages a **relational plant sales dataset**, structured in a typical business intelligence schema:

- **Plants_FACT.csv** – Transactional data: `Sales_USD`, `Price_USD`, `COGS_USD`, `quantity`, `Date_Time`, `Product_id`, `Account_id`  
- **PlantsHierarchy_DIM.csv** – Product metadata: `Product_Family`, `Product_Group`, `Product_Name`, `Product_Size`, `Produt_Type`  
- **Accounts_DIM.csv** – Customer and geographic info: `Account`, `country2`, `latitude2`, `longitude`, `Postal_code`, `street_name`  

This dataset captures **sales performance, product characteristics, and customer location**, providing the foundation for actionable business insights.

## Problem Statement
The company lacked a **centralized view of plant sales performance**, making it difficult to:  

1. Identify which products and regions are **most profitable**  
2. Detect sales trends to **forecast demand**  
3. Optimize **inventory and supply chain decisions**  
4. Target high-value customers and markets efficiently  

The goal of this project was to **build a dashboard that solves these problems** by turning raw data into actionable insights.

## Process

### 1. Data Preparation & Cleaning
- Checked for missing values, corrected inconsistent `Account_id`s, and ensured all fact table entries mapped to valid dimensions.  
- Converted `Date_Time` to a proper datetime format for trend analysis.  
- Standardized categorical columns in `PlantsHierarchy_DIM` and `Accounts_DIM`.

### 2. Data Modeling
- Defined **relationships** between Fact and Dimension tables:  
  - `Plants_FACT.Product_id` → `PlantsHierarchy_DIM.Product_Name_id`  
  - `Plants_FACT.Account_id` → `Accounts_DIM.Account_id`  
- Created a **star schema** for efficient reporting and slicing.

### 3. KPI Definition & Calculation
- Gross Profit: `Sales_USD - COGS_USD`  
- Profit Margin %: `(Sales_USD - COGS_USD) / Sales_USD * 100`  
- Quantity Trends: Aggregated daily/monthly sales volume  
- Product & Region Performance: Calculated total sales, profit, and quantity by hierarchy and geography

### 4. Dashboard Design & Visualization
- **Revenue & Profit Analysis:** Heatmaps by product family and region  
- **Trend Analysis:** Line charts showing monthly sales and growth trends  
- **Drill-Down Analytics:** Hierarchy from Product_Family → Product_Group → Product_Name  
- **Geospatial Analysis:** Map visualizations for top-performing accounts and countries  
- **Interactive KPIs:** Dynamic slicers for product type, size, and region

### 5. Insights & Actionable Outcomes
- Identified **high-margin products** to prioritize for marketing and inventory  
- Highlighted **underperforming regions** for targeted sales campaigns  
- Detected seasonal **sales peaks** to optimize stock levels  
- Provided **executive-ready KPIs** for real-time decision-making  

## Tools & Technologies
- **Power BI Desktop** – Dashboard creation and interactive visualizations  
- **DAX (Data Analysis Expressions)** – Custom measures for profit, margin, and growth metrics  
- **Data Modeling** – Fact-Dimension relationships for accurate, drill-down reporting  

## Key Learnings
- Applied **end-to-end BI workflow**: from data cleaning and modeling to visualization and insights  
- Developed **solution-focused dashboards** that guide business decisions rather than just highlight problems  
- Gained expertise in **hierarchical and geospatial analysis** for actionable insights  
- Built dashboards **optimized for desktop and mobile stakeholders**, enabling on-the-go decision-making
